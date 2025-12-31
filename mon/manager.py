import random

import mon.mon as mon

MAX_LEVEL: int = 100
MAX_BASE_STAT: int = 200
MAX_START_STAT: int = 10
MAX_IV: int = 30
HP_MOD: float = 3.0

id_counter: int = 0
monsters: dict[str, mon.Mon] = {}

def id_display(mon_id: int|str) -> str:
	return str(mon_id).zfill(6)

def species_id(s_id: int|str) -> str:
	return str(s_id).zfill(3)

def rando_mod() -> float:
	return random.randint(85, 115) / 100.0
