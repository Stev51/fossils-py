import os, csv
from unittest import case

import mon.species as species
import mon.types as types

cwd: str = os.getcwd()
SPECIES_FILE: str = cwd + "\\data\\dex.csv"
TYPES_FILE: str = cwd + "\\data\\types.csv"

def verify_mon(m: dict):

	flag: bool = True

	for trait in ("Name", "HP", "P. Attack", "P. Defense", "S. Attack", "S. Defense", "Speed", "Type #1"):
		if m[trait] == "":
			flag = False

	return flag

def import_types() -> None:

	types.STRONG = {}
	types.WEAK = {}
	types.NEGATE = {}
	data: list = []

	with open(TYPES_FILE, mode='r') as f:
		reader = csv.DictReader(f)
		for row in reader:
			data.append(row)

	for type_dict in data:

		t: str = type_dict["DEFENDING"]
		if t in types.Types.type_strs:

			strong: list[int] = []
			weak: list[int] = []
			negate: list[int] = []

			for defender in types.Types.type_strs[1:]:

				val: str = type_dict[defender]
				match val:
					case "2x":
						strong.append(types.Types.str_to_type(defender))
					case "½x":
						weak.append(types.Types.str_to_type(defender))
					case "0x":
						negate.append(types.Types.str_to_type(defender))
					case _:
						if val != "": print(f"Unknown Case: {val}")

			types.STRONG[t] = strong
			types.WEAK[t] = weak
			types.NEGATE[t] = negate

	print("Finished importing types!")

def import_species() -> None:

	species.mons = {}
	data: list = []

	with open(SPECIES_FILE, mode='r') as f:
		reader = csv.DictReader(f)
		for row in reader:
			data.append(row)

	for m in data:
		if verify_mon(m):

			new_mon: dict = {}

			new_mon["Name"] = m["Name"]

			new_mon["HP"] = int(m["HP"])
			new_mon["ATK"] = int(m["P. Attack"])
			new_mon["DEF"] = int(m["P. Defense"])
			new_mon["SPA"] = int(m["S. Attack"])
			new_mon["SPD"] = int(m["S. Defense"])
			new_mon["SPE"] = int(m["Speed"])

			new_mon["Type1"] = types.Types.str_to_type(m["Type #1"])
			if m["Type #2"] == "":
				new_mon["Type2"] = None
			else:
				new_mon["Type2"] = types.Types.str_to_type(m["Type #2"])

			new_mon["LvlUpMoves"] = {1: [0, 1, 2]}

			species.mons[m["ID #"]] = new_mon

	print("Finished importing species!")
