import os
import shutil
import Entities

root = "target\\"

meta_folder = "META-INF\\vault"
resource_folder = "jcr_root\\"

def main():
	translations = read_data("properties.txt")
	translations.print_()

def make_directory_tree(resource_path):
	print()	

def read_data(filename):
	fh = None
	obj_map = None
	translations = None
	try:
		fh = open(filename, encoding="utf8")
		for lino, line in enumerate(fh):
			line = line.rstrip()
			if not line and obj_map is None:
				continue
			if not line:
				if len(obj_map) == 1 and obj_map.get("dictionary_path") is not None:	
					translations = Entities.TranslationList(obj_map.get("dictionary_path"))
					obj_map = None
				else:
					tr = Entities.Translation(**obj_map)
					translations.add_item(tr)
					obj_map = None
			else:
				if obj_map is None:
					obj_map = {}
				key, value = line.split("=", maxsplit=1)
				obj_map[key] = value
		if obj_map is not None:
			tr = Entities.Translation(**obj_map)
			translations.add_item(tr)
		return translations

	except ValueError as err:
		print("Error in line {}".format(lino))
		print(err)
	finally:
		if fh is not None:
			fh.close()

main()

