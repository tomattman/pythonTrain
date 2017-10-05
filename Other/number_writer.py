import json

numbers = [1, 2, 3, 5, 8, 13, 21]

filename = "numbers.json"
def print_data(data):
	with open(filename, 'w') as f_obj:
		json.dump(data, f_obj)

def load_numbers():
	with open(filename, 'r') as f_obj:
		numbers1 = json.load(f_obj)
	print(numbers1)