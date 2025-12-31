import mon.types as types

class Categories:

	PHYSICAL: int = 0
	SPECIAL: int = 1
	STATUS: int = 2

	def to_str(c: int) -> str:
		match c:
			case Categories.PHYSICAL:
				return "Physical"
			case Categories.SPECIAL:
				return "Special"
			case Categories.STATUS:
				return "Status"
			case _:
				return "UNKNOWN_CATEGORY"

moves: dict = {}

class Move:

	def __init__(self, move_id: int, name: str, move_type: int, power: int, accuracy: float, category: int):

		self.id: int = move_id
		self.name: str = name
		self.type: int = move_type
		self.power: int = power
		self.accuracy: float = accuracy
		self.category: int = category

		if category == Categories.STATUS:
			self.power = None

		moves[move_id] = self

	def __str__(self):
		return f"{self.name} ( {self.power} POW / {self.accuracy} ACC / {Categories.to_str(self.category)} / {types.Types.type_to_str(self.type)} )"
