import os, random

import imports.imports as imports
import terminal.terminal as terminal

def main() -> None:

	random.seed()

	if os.path.exists(imports.TYPES_FILE):
		imports.import_types()
	if os.path.exists(imports.SPECIES_FILE):
		imports.import_species()

	terminal.run()
	#input("Press any key to close\n")

if __name__ == "__main__":
	main()
