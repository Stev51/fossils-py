import terminal.commands as commands
import mon.battle_manager as battle_manager

terminal_active: bool = False
current_battle: battle_manager.BattleManager = None

team_id_counter = 0
teams: dict[int, list[str]] = {}

def new_team() -> int:
	global team_id_counter
	new_id: int = team_id_counter
	team_id_counter += 1
	teams[new_id] = []
	return new_id

def print_commands() -> None:
	print("=== COMMANDS ===")
	for name in commands.commands:
		print(f"> {name}:\n\t{commands.command_to_desc[name]}")
	print("================")

def run() -> None:

	global terminal_active
	
	terminal_active = True
	
	print_commands()
	
	while terminal_active:
		
		inp: list[str] = input("> ").split()

		if len(inp) == 0:
			continue
		
		com: str = inp[0]
		args: list[str] = inp[1:]
		
		if com in commands.command_to_func:
			commands.command_to_func[com](args)
		else:
			print("Command not recognized.")
