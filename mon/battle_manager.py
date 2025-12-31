import random

import mon.manager as manager
import mon.mon as mon
import mon.move as move
import mon.types as types

BASIC_CRIT_CHANCE: float = 1.0 / 16.0
SUPER_CRIT_CHANCE: float = 1.0 / 64.0

class BattleState:
	RUNNING: int = 0
	SWITCH_NEEDED: int = 1
	ENEMY_FAINTED: int = 2
	FINISHED: int = 3

class AIClass:
	WILD: int = 0
	TRAINER_BASIC: int = 1
	TRAINER_SMART: int = 2

class InputInfo:
	def __init__(self, attacking: bool, move_index: int, switch: bool, switch_index: int):
		self.attacking: bool = attacking
		self.move_index: int = move_index
		self.switch: bool = switch
		self.switch_index: int = switch_index

class TurnInfo:
	def __init__(self, damage: int, effectiveness_stage: int, crit_stage: int, miss: bool):
		self.damage: int = damage
		self.effectiveness_stage: int = effectiveness_stage
		self.crit_stage: int = crit_stage
		self.miss: bool = miss

class RetInfo:
	def __init__(self):
		...

def print_turn_details(ret_info: TurnInfo, player_turn: bool, player_mon_name: str, enemy_mon_name: str) -> None:

	if ret_info.miss:
		print("The attack missed!!!")
	else:

		match ret_info.crit_stage:
			case 1:
				print("A critical hit!")
			case 2:
				print("A SUPER critical hit!!!")

		if ret_info.effectiveness_stage < 0:

			if player_turn:
				print(f"It didn't affect the enemy {enemy_mon_name}!")
			else:
				print(f"It didn't affect {player_mon_name}!")

		else:

			match ret_info.effectiveness_stage:
				case 1:
					print("It was extremely ineffective...")
				case 2:
					print("It was ineffective...")
				case 4:
					print("It was very effective!")
				case 5:
					print("It was extremely effective!!!")

	if player_turn:
		print(f"The enemy {enemy_mon_name} took {ret_info.damage} damage!")
	else:
		print(f"{player_mon_name} took {ret_info.damage} damage!")

class BattleManager:

	def __init__(self, player_team: list[mon.Mon], enemy_team: list[mon.Mon], enemy_ai_class: int):

		self.player_team: list[mon.Mon] = player_team
		self.enemy_team: list[mon.Mon] = enemy_team
		self.ai_class: int = enemy_ai_class

		self.current_player_mon: mon.Mon = player_team[0]
		self.current_enemy_mon: mon.Mon = enemy_team[0]

		self.state: int = BattleState.RUNNING

		self.print_state()

	def input(self, attacking: bool, move_index: int, switch: bool, switch_index: int) -> RetInfo:

		ii: InputInfo = InputInfo(attacking, move_index, switch, switch_index)

		match self.state:
			case BattleState.RUNNING:

				if attacking:
					if len(self.current_player_mon.moves) <= move_index:
						#print(f"{self.current_player_mon.name} does not have a move in slot {move_index + 1}.")
						return RetInfo(errored=True, bad_slot=True)

				if switch:
					if not self.usable_mon(self.player_team[switch_index]):
						#print(f"{self.player_team[switch_index].name} is not usable in battle.")
						return RetInfo(errored=True, bad_switch=True)

				self.advance_turn(ii)

				self.print_state()

			case BattleState.SWITCH_NEEDED:

				if switch:

					if not self.usable_mon(self.player_team[switch_index]):
						print(f"{self.player_team[switch_index].name} is not usable in battle.")
						return

					self.switch_to(switch_index)
					self.state = BattleState.RUNNING

					self.print_state()

				else:

					print("You need to switch to a new monster!")

			case BattleState.FINISHED:

				print("The battle is already ended!")

	def advance_turn(self, ii: InputInfo) -> None:

		if ii.attacking:

			player_acting_speed: int = self.current_player_mon.SPE
			enemy_acting_speed: int = self.current_enemy_mon.SPE

			if player_acting_speed == enemy_acting_speed:
				enemy_acting_speed += random.choice([-1, 1])

			if enemy_acting_speed > player_acting_speed:

				self.take_enemy_turn()

				if self.state == BattleState.RUNNING:
					self.take_player_turn(ii.move_index)

			else:

				self.take_player_turn(ii.move_index)

				if self.state == BattleState.RUNNING:
					self.take_enemy_turn()

		if self.state == BattleState.ENEMY_FAINTED:
			self.state = BattleState.RUNNING

		elif ii.switch:

			self.switch_to(ii.switch_index)
			self.take_enemy_turn()

	def take_player_turn(self, move_index: int) -> None:

		attack: move.Move = move.moves[self.current_player_mon.moves[move_index]]
		ret_info: TurnInfo = self.perform_attack(self.current_player_mon, self.current_enemy_mon, attack)

		print(f"{self.current_player_mon.name} used {attack.name}!")
		print_turn_details(ret_info, True, self.current_player_mon.name, self.current_enemy_mon.name)

		self.verify_enemy_state()

	def take_enemy_turn(self) -> None:

		attack: move.Move = move.moves[self.current_player_mon.moves[self.pick_enemy_move()]]
		ret_info: TurnInfo = self.perform_attack(self.current_enemy_mon, self.current_player_mon, attack)

		print(f"The enemy {self.current_enemy_mon.name} used {attack.name}!")
		print_turn_details(ret_info, False, self.current_player_mon.name, self.current_enemy_mon.name)

		self.verify_player_state()

	def verify_player_state(self) -> None:

		if self.current_player_mon.current_HP <= 0:

			print(f"{self.current_player_mon.name} has fainted!")

			if self.usable_mons_left(self.player_team):

				print("Pick a new monster to switch to!")
				self.state = BattleState.SWITCH_NEEDED

			else:

				print("You are out of usable monsters!\nThe enemy won the battle!")
				self.state = BattleState.FINISHED

	def verify_enemy_state(self) -> None:

		if self.current_enemy_mon.current_HP <= 0:

			print(f"{self.current_enemy_mon.name} has fainted!")

			if self.usable_mons_left(self.enemy_team):

				self.enemy_switch_to(self.pick_enemy_switch())
				self.state = BattleState.ENEMY_FAINTED

			else:

				print("The enemy is out of usable monsters!\nYou won the battle!!!")
				self.state = BattleState.FINISHED

	def switch_to(self, index: int) -> None:

		self.current_player_mon = self.player_team[index]
		print(f"Switched out to {self.current_player_mon.name}!")

	def enemy_switch_to(self, index: int) -> None:

		self.current_enemy_mon = self.enemy_team[index]
		print(f"The enemy switched out their monster to {self.current_enemy_mon.name}!")

	def perform_attack(self, attacker: mon.Mon, defender: mon.Mon, m: move.Move) -> TurnInfo:

		lvl: float = float(attacker.LVL)
		pwr: float = float(m.power)

		atk: float = 0.0
		dfn: float = 0.0
		match m.category:
			case move.Categories.PHYSICAL:
				atk = float(attacker.ATK)
				dfn = float(defender.DEF)
			case move.Categories.SPECIAL:
				atk = float(attacker.SPA)
				dfn = float(defender.SPD)

		crit: float = 1.0
		crit_stage: int = 0
		crit_chance: float = random.random()
		if crit_chance < SUPER_CRIT_CHANCE:
			crit = 2.0
			crit_stage = 2
		elif crit_chance < BASIC_CRIT_CHANCE:
			crit = 1.5
			crit_stage = 1

		stab: float = 1.0
		if m.type == attacker.type[0] or m.type == attacker.type[1]:
			stab = 1.5

		effectiveness: float = 1.0
		effectiveness_stage: int = 3
		for t in defender.type:
			if t in types.STRONG[m.type]:
				effectiveness *= 2.0
				effectiveness_stage += 1
			if t in types.WEAK[m.type]:
				effectiveness *= 0.5
				effectiveness_stage -= 1
			if t in types.NEGATE[m.type]:
				effectiveness *= 0.0
				effectiveness_stage *= -1

		rando: float = manager.rando_mod()

		damage_calc: int = round( ((((((2.0 * lvl) / 5.0) + 2.0) * pwr * (atk / dfn)) / 50.0) + 2.0) * crit * stab * effectiveness * rando )

		miss: bool = False
		if random.random() >= m.accuracy:
			miss = True

		damage: int = max(1, damage_calc)
		if effectiveness_stage < 0 or miss == True:
			damage = 0

		defender.take_damage(damage)

		return TurnInfo(damage=damage, effectiveness_stage=effectiveness_stage, crit_stage=crit_stage, miss=miss)

	def usable_mon(self, m: mon.Mon) -> bool:
		return not m.fainted

	def usable_mons_left(self, team: list[mon.Mon]) -> bool:

		output: bool = False

		for m in team:
			output = output or self.usable_mon(m)

		return output

	def pick_enemy_move(self) -> int:

		return 0

	def pick_enemy_switch(self) -> int:

		for i, m in enumerate(self.enemy_team):
			if self.usable_mon(m):
				return i

		return -1

	def print_state(self) -> None:

		print("=== BATTLE STATE ===")
		print()

		print("--- Enemy Monster ---")
		print(f"{self.current_enemy_mon.name} ({self.current_enemy_mon.species}) [Lvl. {self.current_enemy_mon.LVL}]")
		print(f"HP: {self.current_enemy_mon.current_HP} / {self.current_enemy_mon.HP}")
		print("---------------------")
		print()

		print("--- Your Monster ---")
		print(f"{self.current_player_mon.name} ({self.current_player_mon.species}) [Lvl. {self.current_player_mon.LVL}]")
		print(f"HP: {self.current_player_mon.current_HP} / {self.current_player_mon.HP}")
		print("--------------------")
		print()

		print("--- Move Options: ---")

		for i, m in enumerate(self.current_player_mon.moves, start=1):
			print(f"{i}: ", end='')
			tmp: move.Move = move.moves[m]
			print(tmp)

		print("---------------------")
		print()

		print("====================")
