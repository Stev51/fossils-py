class Stat:
	HP: int = 0
	ATK: int = 1
	DEF: int = 2
	SPA: int = 3
	SPD: int = 4
	SPE: int = 5

natures = [
	{
		"name": "NEUTRAL1",
		"good_iv": None,
		"bad_iv": None
	},
	{
		"name": "NEUTRAL2",
		"good_iv": None,
		"bad_iv": None
	},
	{
		"name": "+HP/-ATK",
		"good_iv": Stat.HP,
		"bad_iv": Stat.ATK
	},
	{
		"name": "+HP/-DEF",
		"good_iv": Stat.HP,
		"bad_iv": Stat.DEF
	},
	{
		"name": "+HP/-SPA",
		"good_iv": Stat.HP,
		"bad_iv": Stat.SPA
	},
	{
		"name": "+HP/-SPD",
		"good_iv": Stat.HP,
		"bad_iv": Stat.SPD
	},
	{
		"name": "+HP/-SPE",
		"good_iv": Stat.HP,
		"bad_iv": Stat.SPE
	},
	{
		"name": "+ATK/-HP",
		"good_iv": Stat.ATK,
		"bad_iv": Stat.HP
	},
	{
		"name": "+ATK/-DEF",
		"good_iv": Stat.ATK,
		"bad_iv": Stat.DEF
	},
	{
		"name": "+ATK/-SPA",
		"good_iv": Stat.ATK,
		"bad_iv": Stat.SPA
	},
	{
		"name": "+ATK/-SPD",
		"good_iv": Stat.ATK,
		"bad_iv": Stat.SPD
	},
	{
		"name": "+ATK/-SPE",
		"good_iv": Stat.ATK,
		"bad_iv": Stat.SPE
	},
	{
		"name": "+DEF/-HP",
		"good_iv": Stat.DEF,
		"bad_iv": Stat.HP
	},
	{
		"name": "+DEF/-ATK",
		"good_iv": Stat.DEF,
		"bad_iv": Stat.ATK
	},
	{
		"name": "+DEF/-SPA",
		"good_iv": Stat.DEF,
		"bad_iv": Stat.SPA
	},
	{
		"name": "+DEF/-SPD",
		"good_iv": Stat.DEF,
		"bad_iv": Stat.SPD
	},
	{
		"name": "+DEF/-SPE",
		"good_iv": Stat.DEF,
		"bad_iv": Stat.SPE
	},
	{
		"name": "+SPA/-HP",
		"good_iv": Stat.SPA,
		"bad_iv": Stat.HP
	},
	{
		"name": "+SPA/-ATK",
		"good_iv": Stat.SPA,
		"bad_iv": Stat.ATK
	},
	{
		"name": "+SPA/-DEF",
		"good_iv": Stat.SPA,
		"bad_iv": Stat.DEF
	},
	{
		"name": "+SPA/-SPD",
		"good_iv": Stat.SPA,
		"bad_iv": Stat.SPD
	},
	{
		"name": "+SPA/-SPE",
		"good_iv": Stat.SPA,
		"bad_iv": Stat.SPE
	},
	{
		"name": "+SPD/-HP",
		"good_iv": Stat.SPD,
		"bad_iv": Stat.HP
	},
	{
		"name": "+SPD/-ATK",
		"good_iv": Stat.SPD,
		"bad_iv": Stat.ATK
	},
	{
		"name": "+SPD/-DEF",
		"good_iv": Stat.SPD,
		"bad_iv": Stat.DEF
	},
	{
		"name": "+SPD/-SPA",
		"good_iv": Stat.SPD,
		"bad_iv": Stat.SPA
	},
	{
		"name": "+SPD/-SPE",
		"good_iv": Stat.SPD,
		"bad_iv": Stat.SPE
	},
	{
		"name": "+SPE/-HP",
		"good_iv": Stat.SPE,
		"bad_iv": Stat.HP
	},
	{
		"name": "+SPE/-ATK",
		"good_iv": Stat.SPE,
		"bad_iv": Stat.ATK
	},
	{
		"name": "+SPE/-DEF",
		"good_iv": Stat.SPE,
		"bad_iv": Stat.DEF
	},
	{
		"name": "+SPE/-SPA",
		"good_iv": Stat.SPE,
		"bad_iv": Stat.SPA
	},
	{
		"name": "+SPE/-SPD",
		"good_iv": Stat.SPE,
		"bad_iv": Stat.SPD
	}
]
