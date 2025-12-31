class Types:

	TYPELESS: int = -1
	NORMAL: int = 0
	PLANT: int = 1
	WATER: int = 2
	FIRE: int = 3
	AIR: int = 4
	EARTH: int = 5
	GEO: int = 6
	METAL: int = 7
	LIGHTNING: int = 8
	ICE: int = 9
	TOXIC: int = 10
	SOUND: int = 11
	FIGHT: int = 12
	DARK: int = 13
	SPIRIT: int = 14

	type_ints: list[int] = [TYPELESS, NORMAL, PLANT, WATER, FIRE, AIR, EARTH, GEO, METAL, LIGHTNING, ICE, TOXIC, SOUND, FIGHT, DARK, SPIRIT]
	type_strs: list[str] = []

	def type_to_str(t: int) -> str:
		match t:
			case Types.NORMAL:
				return "Normal"
			case Types.PLANT:
				return "Plant"
			case Types.WATER:
				return "Water"
			case Types.FIRE:
				return "Fire"
			case Types.AIR:
				return "Air"
			case Types.EARTH:
				return "Earth"
			case Types.GEO:
				return "Geo"
			case Types.METAL:
				return "Metal"
			case Types.LIGHTNING:
				return "Lightning"
			case Types.ICE:
				return "Ice"
			case Types.TOXIC:
				return "Toxic"
			case Types.SOUND:
				return "Sound"
			case Types.FIGHT:
				return "Fight"
			case Types.DARK:
				return "Dark"
			case Types.SPIRIT:
				return "Spirit"
			case _:
				return "TYPELESS"

	def str_to_type(s: str) -> int:
		match s:
			case "Normal":
				return Types.NORMAL
			case "Plant":
				return Types.PLANT
			case "Water":
				return Types.WATER
			case "Fire":
				return Types.FIRE
			case "Air":
				return Types.AIR
			case "Earth":
				return Types.EARTH
			case "Geo":
				return Types.GEO
			case "Metal":
				return Types.METAL
			case "Lightning":
				return Types.LIGHTNING
			case "Ice":
				return Types.ICE
			case "Toxic":
				return Types.TOXIC
			case "Sound":
				return Types.SOUND
			case "Fight":
				return Types.FIGHT
			case "Dark":
				return Types.DARK
			case "Spirit":
				return Types.SPIRIT
			case _:
				return Types.TYPELESS

for t in Types.type_ints:
	Types.type_strs.append(Types.type_to_str(t))

# Offensively strong against
STRONG: dict[int, list[int]] = {}

# Offensively weak against
WEAK: dict[int, list[int]] = {}

# Offensively negated by
NEGATE: dict[int, list[int]] = {}

'''
# Offensively strong against
STRONG: dict[int, list[int]] = {
	Types.TYPELESS: [],
	Types.NORMAL: [],
	Types.PLANT: [
		Types.WATER,
		Types.EARTH,
		Types.GEO
	],
	Types.WATER: [
		Types.FIRE,
		Types.EARTH,
		Types.GEO
	],
	Types.FIRE: [
		Types.PLANT,
		Types.METAL,
		Types.ICE
	],
	Types.AIR: [
		Types.EARTH
	],
	Types.EARTH: [
		Types.FIRE,
		Types.GEO,
		Types.METAL,
		Types.LIGHTNING,
		Types.TOXIC
	],
	Types.GEO: [
		Types.FIRE,
		Types.ICE
	],
	Types.METAL: [
		Types.PLANT,
		Types.GEO,
		Types.ICE
	],
	Types.LIGHTNING: [
		Types.WATER,
		Types.AIR,
		Types.METAL
	],
	Types.ICE: [
		Types.PLANT,
		Types.AIR,
		Types.EARTH
	],
	Types.TOXIC: [
		Types.PLANT
	],
	Types.SOUND: [
		Types.AIR,
		Types.ICE
	],
	Types.FIGHT: [
		Types.NORMAL,
		Types.GEO,
		Types.METAL,
		Types.ICE,
		Types.DARK
	],
	Types.DARK: [
		Types.SPIRIT
	],
	Types.SPIRIT: [
		Types.METAL,
		Types.FIGHT,
		Types.SPIRIT
	]
}

# Offensively weak against
WEAK: dict[int, list[int]] = {
	Types.TYPELESS: [],
	Types.NORMAL: [
		Types.GEO,
		Types.METAL
	],
	Types.PLANT: [
		Types.PLANT,
		Types.FIRE,
		Types.METAL,
		Types.ICE,
		Types.TOXIC
	],
	Types.WATER: [
		Types.PLANT,
		Types.WATER,
		Types.ICE
	],
	Types.FIRE: [
		Types.WATER,
		Types.FIRE,
		Types.EARTH
	],
	Types.AIR: [
		Types.AIR,
		Types.METAL,
		Types.LIGHTNING,
		Types.ICE
	],
	Types.EARTH: [
		Types.PLANT,
		Types.EARTH,
		Types.ICE
	],
	Types.GEO: [
		Types.METAL
	],
	Types.METAL: [
		Types.FIRE,
		Types.LIGHTNING
	],
	Types.LIGHTNING: [
		Types.GEO,
		Types.LIGHTNING
	],
	Types.ICE: [
		Types.FIRE,
		Types.METAL,
		Types.ICE
	],
	Types.TOXIC: [
		Types.EARTH,
		Types.TOXIC
	],
	Types.SOUND: [],
	Types.FIGHT: [
		Types.TOXIC,
		Types.SPIRIT
	],
	Types.DARK: [
		Types.FIGHT,
		Types.DARK
	],
	Types.SPIRIT: [
		Types.DARK
	]
}

# Offensively negated by
NEGATE: dict[int, list[int]] = {
	Types.TYPELESS: [],
	Types.NORMAL: [
		Types.SPIRIT
	],
	Types.PLANT: [],
	Types.WATER: [],
	Types.FIRE: [],
	Types.AIR: [],
	Types.EARTH: [
		Types.AIR
	],
	Types.GEO: [],
	Types.METAL: [],
	Types.LIGHTNING: [
		Types.EARTH
	],
	Types.ICE: [],
	Types.TOXIC: [
		Types.METAL
	],
	Types.SOUND: [],
	Types.FIGHT: [],
	Types.DARK: [],
	Types.SPIRIT: [
		Types.NORMAL
	]
}
'''
