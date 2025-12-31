import mon.types as types

def print_species(s_id: str) -> None:

	s: dict = mons[s_id]
	out: list[str] = []

	out.append(f"=== {s["Name"]} ===\n\n")

	out.append(f"{"TYPE:":<6}{types.Types.type_to_str(s["Type1"])}")
	if s["Type2"] is not None:
		out.append(f" / {types.Types.type_to_str(s["Type2"])}")
	out.append("\n\n")

	out.append(f"{"HP:":<6}{s["HP"]}\n")
	out.append(f"{"ATK:":<6}{s["ATK"]}\n")
	out.append(f"{"DEF:":<6}{s["DEF"]}\n")
	out.append(f"{"SPA:":<6}{s["SPA"]}\n")
	out.append(f"{"SPD:":<6}{s["SPD"]}\n")
	out.append(f"{"SPE:":<6}{s["SPE"]}\n\n")

	out.append("====")
	for i in range(len(s["Name"])):
		out.append("=")
	out.append("====")

	print(''.join(out))

mons = {}
