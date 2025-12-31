import requests

import imports.imports as imports

def download_file(url: str, file: str) -> None:

	response = requests.get(url)

	if response.status_code != 200:
		print(f"Error {response.status_code} while downloading {file}")
		return

	with open(file, 'wb') as f:
		f.write(response.content)
	print(f"Finished downloading {file}")

def download_types() -> None:

	url: str = "https://docs.google.com/spreadsheets/d/1Me38tg1ykTpc3r0SBHDIu151y2NJq1o6D2TWgNQ6aqM/export?format=csv&gid=0"

	download_file(url, imports.TYPES_FILE)
	imports.import_types()

def download_species() -> None:

	url: str = "https://docs.google.com/spreadsheets/d/1Me38tg1ykTpc3r0SBHDIu151y2NJq1o6D2TWgNQ6aqM/export?format=csv&gid=2146593786"

	download_file(url, imports.SPECIES_FILE)
	imports.import_species()
