import random

import mon.manager as manager
import mon.species as mon_species
import mon.natures as natures
import mon.types as types

def starter_stat(base_stat: int, iv: int) -> int:

	possibility: int = round((base_stat / float(manager.MAX_BASE_STAT)) * float(manager.MAX_START_STAT))

	if iv > 0:
		possibility += 1
	elif iv < 0:
		possibility -= 1

	return max(1, possibility)

def stat_increase(base_stat: int, level: int, iv: int) -> int:
	
	base_increase: float = (base_stat / float(manager.MAX_BASE_STAT)) * float(manager.MAX_START_STAT)
	lvl_mod: float = (level / float(manager.MAX_LEVEL))
	iv_mod: float = (iv / float(manager.MAX_IV)) * 0.2 + 1.0
	rando_mod: float = manager.rando_mod()
	possibility: float = base_increase * lvl_mod * iv_mod * rando_mod
	
	if possibility < 1.0:
		if random.random() < possibility:
			return 1
		else:
			return 0
	else:
		return round(possibility)

class Mon:
	
	def __init__(self, species: str, name: str = "", lvl: int = 1, ivs: list[int] = None, force_neutral_nature: bool = False):

		template: dict = mon_species.mons[species]
		self.species: str = template["Name"]
		
		self.LVL: int = 1
		self.type: list[int] = [template["Type1"], template["Type2"]]
		
		self.id: int = manager.id_counter
		self.id_str: str = manager.id_display(self.id)
		manager.id_counter += 1
		
		self.name: str = name
		if name == "":
			self.name = self.species
		
		self.BaseHP: int = template["HP"]
		self.BaseATK: int = template["ATK"]
		self.BaseDEF: int = template["DEF"]
		self.BaseSPA: int = template["SPA"]
		self.BaseSPD: int = template["SPD"]
		self.BaseSPE: int = template["SPE"]

		reset_ivs: bool = False
		if ivs is None:
			reset_ivs = True
		elif len(ivs) < 6:
			reset_ivs = True
		if reset_ivs:
			ivs = [0] * 6
		
		nature_template: dict = natures.natures[0]
		if not force_neutral_nature:
			nature_template = random.choice(natures.natures)

		self.nature: str = nature_template["name"]
		
		good_iv: int = nature_template["good_iv"]
		if good_iv is not None:
			ivs[good_iv] += 1
		
		bad_iv: int = nature_template["bad_iv"]
		if bad_iv is not None:
			ivs[bad_iv] -= 1
		
		self.HP_IV: int = ivs[0]
		self.ATK_IV: int = ivs[1]
		self.DEF_IV: int = ivs[2]
		self.SPA_IV: int = ivs[3]
		self.SPD_IV: int = ivs[4]
		self.SPE_IV: int = ivs[5]

		self.HP: int = round(starter_stat(self.BaseHP, self.HP_IV) * manager.HP_MOD)
		self.ATK: int = starter_stat(self.BaseATK, self.ATK_IV)
		self.DEF: int = starter_stat(self.BaseDEF, self.DEF_IV)
		self.SPA: int = starter_stat(self.BaseSPA, self.SPA_IV)
		self.SPD: int = starter_stat(self.BaseSPD, self.SPD_IV)
		self.SPE: int = starter_stat(self.BaseSPE, self.SPE_IV)

		self.current_HP: int = self.HP
		self.fainted: bool = False

		self.lvl_up_moves: dict[int, list[int]] = template["LvlUpMoves"]
		self.moves: list[int] = []

		new_moves: list[int] = []
		for l in range(1, lvl+1):
			if l in self.lvl_up_moves:
				new_moves += self.lvl_up_moves[l]
		if len(new_moves) > 4:
			new_moves = new_moves[-4:]
		for m in new_moves:
			self.moves.append(m)

		if lvl > manager.MAX_LEVEL:
			lvl = manager.MAX_LEVEL
		for lvlup in range(2, lvl + 1):
			self.level_up_stats()
		
		manager.monsters[self.id_str] = self
	
	def __str__(self):

		out: list[str] = []
		
		out.append(f"=== {self.name} ===\n\n")

		out.append(f"{"ID:":<12}{self.id_str}\n")
		out.append(f"{"SPECIES:":<12}{self.species}\n")
		out.append(f"{"LVL:":<12}{self.LVL}\n")
		out.append(f"{"NATURE:":<12}{self.nature}\n\n")

		out.append(f"TYPE: {types.Types.type_to_str(self.type[0])}")
		if self.type[1] is not None:
			out.append(f" / {types.Types.type_to_str(self.type[1])}")
		out.append("\n\n")
		
		out.append(f"{"HP:":<12}{self.HP}\n")
		out.append(f"{"ATK:":<12}{self.ATK}\n")
		out.append(f"{"DEF:":<12}{self.DEF}\n")
		out.append(f"{"SPA:":<12}{self.SPA}\n")
		out.append(f"{"SPD:":<12}{self.SPD}\n")
		out.append(f"{"SPE:":<12}{self.SPE}\n\n")
		
		out.append(f"{"IV HP:":<12}{self.HP_IV}\n")
		out.append(f"{"IV ATK:":<12}{self.ATK_IV}\n")
		out.append(f"{"IV DEF:":<12}{self.DEF_IV}\n")
		out.append(f"{"IV SPA:":<12}{self.SPA_IV}\n")
		out.append(f"{"IV SPD:":<12}{self.SPD_IV}\n")
		out.append(f"{"IV SPE:":<12}{self.SPE_IV}\n\n")
		
		out.append(f"{"BASE HP:":<12}{self.BaseHP}\n")
		out.append(f"{"BASE ATK:":<12}{self.BaseATK}\n")
		out.append(f"{"BASE DEF:":<12}{self.BaseDEF}\n")
		out.append(f"{"BASE SPA:":<12}{self.BaseSPA}\n")
		out.append(f"{"BASE SPD:":<12}{self.BaseSPD}\n")
		out.append(f"{"BASE SPE:":<12}{self.BaseSPE}\n\n")
		
		out.append("====")
		for i in range(len(self.name)):
			out.append("=")
		out.append("====")
		
		return ''.join(out)
	
	def level_up_stats(self) -> None:
		
		if self.LVL >= manager.MAX_LEVEL:
			return

		old_hp_ratio: float = float(self.current_HP) / float(self.HP)
		
		self.LVL += 1
		
		self.HP += round(stat_increase(self.BaseHP, self.LVL, self.HP_IV) * manager.HP_MOD)
		self.ATK += stat_increase(self.BaseATK, self.LVL, self.ATK_IV)
		self.DEF += stat_increase(self.BaseDEF, self.LVL, self.DEF_IV)
		self.SPA += stat_increase(self.BaseSPA, self.LVL, self.SPA_IV)
		self.SPD += stat_increase(self.BaseSPD, self.LVL, self.SPD_IV)
		self.SPE += stat_increase(self.BaseSPE, self.LVL, self.SPE_IV)

		if not self.fainted:
			self.current_HP = max(1, round(old_hp_ratio * self.HP))

	def take_damage(self, dmg: int) -> None:

		self.current_HP -= dmg

		if self.current_HP <= 0:
			self.current_HP = 0
			self.fainted = True
