import ast
from collections.abc import Callable

import terminal.terminal as terminal
import terminal.battle_output as battle_output
import imports.download as download
import mon.manager as mon_manager
import mon.mon as mon
import mon.species as mon_species
import mon.battle_manager as battle_manager

commands: list[str] = []
command_to_desc: dict[str, str] = {}
command_to_func: dict[str, Callable] = {}

def command(name: str, desc: str, func: Callable, pseudonyms: list[str] = None) -> None:
	
	commands.append(name)
	command_to_desc[name] = desc
	command_to_func[name] = func

	if pseudonyms is not None:
		for pseudo in pseudonyms:
			command_to_func[pseudo] = func

def func_help(args: list[str]) -> None:
	terminal.print_commands()
command("help", "Prints this list.", func_help, pseudonyms=["h"])

def func_quit(args: list[str]) -> None:
	terminal.terminal_active = False
command("quit", "Ends the terminal. (a.k.a. \"exit\")", func_quit, pseudonyms=["exit", "q", "e"])

def func_quick_setup(args: list[str]) -> None:

	print("Running quick setup!")

	func_new_team(["2"])

	func_new(["1", "10", "GoodWater"])
	func_team_add(["0", "0"])
	func_new(["4", "10", "GoodPlant"])
	func_team_add(["0", "1"])
	func_new(["7", "10", "GoodFire"])
	func_team_add(["0", "2"])

	func_new(["7", "10", "BadFire"])
	func_team_add(["1", "3"])
	func_new(["4", "10", "BadPlant"])
	func_team_add(["1", "4"])
	func_new(["1", "10", "BadWater"])
	func_team_add(["1", "5"])

	func_new_battle(["0", "1", "1"])

command("quick_setup", "Runs a hardcoded set of setup commands.", func_quick_setup)

def func_refresh(args: list[str]) -> None:
	download.download_types()
	download.download_species()
command("refresh", "Downloads data from Google Sheets.", func_refresh, pseudonyms=["r"])

def func_new(args: list[str]) -> None:
	
	if len(args) < 1:
		print("Need to supply a species ID.")
		return
	
	species: str = mon_manager.species_id(args[0])
	
	if species not in mon_species.mons:
		print(f"Species not found with ID `{species}`.")
		return
	
	lvl: int = 1
	nickname: str = ""
	ivs: list[int] = []
	force_neutral: bool = False
	
	if len(args) >= 2:
		lvl = int(args[1])
	if len(args) >= 3:
		nickname = args[2]
	if len(args) >= 4:
		ivs = ast.literal_eval(args[3])
	if len(args) >= 5:
		force_neutral = True
	
	new_mon: mon.Mon = mon.Mon(species, name=nickname, lvl=lvl, ivs=ivs, force_neutral_nature=force_neutral)
	print(f"New {new_mon.species} created with monster ID {new_mon.id_str}!")

command("new", "Creates a new monster. Requires the species ID. Optional parameters in order:\n\t- level\n\t- nickname\n\t- ivs (list)\n\t- force neutral nature flag", func_new, pseudonyms=["n"])

def func_mon(args: list[str]) -> None:
	
	if len(args) < 1:
		print("Need to supply a monster ID.")
		return
	
	mon_id: str = mon_manager.id_display(args[0])
	
	if mon_id in mon_manager.monsters:
		print(mon_manager.monsters[mon_id])
	else:
		print(f"Monster with ID `{mon_id}` not found.")

command("mon", "Displays a monster's info. Give the ID number to check.", func_mon, pseudonyms=["m"])

def func_mons(args: list[str]) -> None:
	
	end: int = len(mon_manager.monsters)
	
	for index, id_str in enumerate(mon_manager.monsters.keys(), start=1):
		print(f"{id_str}", end='')
		if index != end:
			print('\t', end='')
			if index % 4 == 0:
				print()
	
	print()

command("mons", "Lists all registered mon ids. (a.k.a. \"ids\", \"list\")", func_mons, pseudonyms=["ids", "list"])

def func_iv(args: list[str]) -> None:

	if len(args) < 7:
		print("Need to supply monster ID and six IV values.")
		return

	mon_id: str = mon_manager.id_display(args[0])

	if mon_id not in mon_manager.monsters:
		print(f"Monster with ID `{mon_id}` not found.")
		return

	monster: mon.Mon = mon_manager.monsters[mon_id]

	monster.HP_IV = int(args[1])
	monster.ATK_IV = int(args[2])
	monster.DEF_IV = int(args[3])
	monster.SPA_IV = int(args[4])
	monster.SPD_IV = int(args[5])
	monster.SPE_IV = int(args[6])

	print(f"Set {monster.name}'s IV values!")

command("iv", "Set a monster's IVs. Requires the monster ID and six IV values.", func_iv)

def func_heal(args: list[str]) -> None:

	counter: int = 0
	for m in mon_manager.monsters.values():
		m.current_HP = m.HP
		counter += 1

	print("Fully healed all {counter} monsters!")

command("heal", "Heals all created monsters.", func_heal)

def func_team(args: list[str]) -> None:

	if len(args) < 1:
		print("Must supply team ID.")
		return

	team_id: int = int(args[0])

	if team_id not in terminal.teams:
		print(f"No team found with id {team_id}.")
		return

	team = terminal.teams[team_id]

	print("=== Team Member IDs ===")
	for m in team:
		print(m)
	print("=======================")

command("team", "Shows the members of a team. Supply the team ID.", func_team, pseudonyms=["t"])

def func_new_team(args: list[str]) -> None:

	num: int = 1
	if len(args) >= 1:
		num = int(args[0])

	for i in range(num):
		print(f"Created new team with ID {terminal.new_team()}.")

command("new_team", "Creates a new team which you can fill with monsters. Optionally supply number of teams to create.", func_new_team)

def func_team_add(args: list[str]) -> None:

	if len(args) < 2:
		print("Need to supply team ID and monster ID.")
		return

	team_id: int = int(args[0])
	mon_id: str = mon_manager.id_display(args[1])

	if team_id not in terminal.teams:
		print(f"No team found with ID {team_id}.")
		return

	team = terminal.teams[team_id]

	if mon_id not in mon_manager.monsters:
		print(f"No monster found with ID {mon_id}.")
		return

	team.append(mon_id)
	print(f"Added monster {mon_id} to team {team_id}!")

command("team_add", "Add a monster to a team. Supply the team ID and the monster ID.", func_team_add)

def func_team_rm(args: list[str]) -> None:

	if len(args) < 2:
		print("Need to supply team ID and monster ID.")
		return

	team_id: int = int(args[0])
	mon_id: str = mon_manager.id_display(args[1])

	if team_id not in terminal.teams:
		print(f"No team found with ID {team_id}.")
		return

	team = terminal.teams[team_id]

	if mon_id not in team:
		print(f"Monster ID {mon_id} not found in team {team_id}.")
		return

	team.remove(mon_id)
	print(f"Removed monster {mon_id} from team {team_id}!")

command("team_rm", "Remove a monster from a team. Supply the team ID and the monster ID.", func_team_rm, pseudonyms=["team_remove"])

def func_teams(args: list[str]) -> None:

	max_teams: int = len(terminal.teams)
	for index, team_id in enumerate(terminal.teams.keys(), start=1):
		print(f"{team_id}", end='')
		if index != max_teams:
			print(", ", end='')
	print()

command("teams", "List all created team ids.", func_teams)

def func_new_battle(args: list[str]) -> None:

	if len(args) < 3:
		print("Need to supply player team ID, enemy team ID, and AI class (0 = wild battle, 1 = regular trainer battle, 2 = smart trainer battle).")
		return

	player_index: int = int(args[0])
	enemy_index: int = int(args[1])
	ai_class: int = int(args[2])

	if ai_class < 0 or ai_class > 2:
		print("AI class must be in range 0-2.")
		return

	if player_index not in terminal.teams:
		print(f"No team found with ID {player_index}.")
		return

	if enemy_index not in terminal.teams:
		print(f"No team found with ID {enemy_index}.")
		return

	player_team_ref: list[str] = terminal.teams[player_index]
	player_team: list[mon.Mon] = []
	for id_num in player_team_ref:
		player_team.append(mon_manager.monsters[mon_manager.id_display(id_num)])

	enemy_team_ref: list[str] = terminal.teams[enemy_index]
	enemy_team: list[mon.Mon] = []
	for id_num in enemy_team_ref:
		enemy_team.append(mon_manager.monsters[mon_manager.id_display(id_num)])

	terminal.current_battle = battle_manager.BattleManager(player_team, enemy_team, ai_class)

command("new_battle", "Start a new battle. Supply the player team, enemy team, and AI class (0 = wild battle, 1 = regular trainer battle, 2 = smart trainer battle).", func_new_battle)

def func_battle(args: list[str]) -> None:

	act: str = "h"
	if len(args) >= 1:
		act = args[0]

	if act == "h":

		print("Battle Commands:")
		print("\t- [1-4]: Make an attack using the numbered move slot.")
		print("\t- s[1-6]: Switch to a different team member.")

	elif terminal.current_battle is None:
		print("No current battle. Create one with \"new_battle\" command.")
	else:

		ret_info: battle_manager.RetInfo = None

		match act:

			case "1":
				ret_info = terminal.current_battle.input(True, 0, False, None)
			case "2":
				ret_info = terminal.current_battle.input(True, 1, False, None)
			case "3":
				ret_info = terminal.current_battle.input(True, 2, False, None)
			case "4":
				ret_info = terminal.current_battle.input(True, 3, False, None)

			case "s1":
				ret_info = terminal.current_battle.input(False, None, True, 0)
			case "s2":
				ret_info = terminal.current_battle.input(False, None, True, 1)
			case "s3":
				ret_info = terminal.current_battle.input(False, None, True, 2)
			case "s4":
				ret_info = terminal.current_battle.input(False, None, True, 3)
			case "s5":
				ret_info = terminal.current_battle.input(False, None, True, 4)
			case "s6":
				ret_info = terminal.current_battle.input(False, None, True, 5)

			case _:
				print("Unrecognized action. Check \"battle h\" for help.")
				return

		battle_output.battle_print(ret_info)

command("battle", "Take an action in the current battle. Run \"battle help\" to see options.", func_battle, pseudonyms=["b"])

def func_species(args: list[str]) -> None:

	if len(args) >= 1:

		s_id = mon_manager.species_id(args[0])

		if s_id not in mon_species.mons:
			print(f"No species found with ID {s_id}.")
			return

		mon_species.print_species(s_id)

	else:

		for s_id, s in mon_species.mons.items():
			print(f"{s_id}:\t{s["Name"]}")

command("species", "Lists all available species, or supply a species ID to see its details.", func_species, pseudonyms=["s"])
