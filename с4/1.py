import os

def main():
	

def get_string(message, name = "string", default = None, minimum_length = 0, maximum_length = 80):
	message += ": " if default is None else "[{0}]: ".format(default)
	while True:
		try:
			line = input(message)
			if not line:
				if default is not None:
					return default
				if minimum_length ==0:
					return ""
				else:
					raise ValueError("{0} may not be empty".format(name))
			if not (minimum_length <= len(line) <= maximum_length):
				raise ValueError("{0} must have at least {1} and"
					"at most {2} characters".format(name, minimum_length, maximum_length))
			return line
		except ValueError as err:
			print("ERROR", err)

def get_integer(message, name = "integer", default = None, minimum = 0, maximum = 100, allow_zero = True):
	message += ": " if default is None else "[{0}]: ".format(default)
	while True:
		try:
			try:
				line = input(message)
				if not line and default is not None:
					number = default
				else:
					number = int(line)
			except ValueError as err:
				raise ValueError("Can not covert line '{0}' to integer".format(line))
			if not (minimum <= number <= maximum):
				raise ValueError("number {0} must be between {1} and {2}".format(number, minimum, maximum))
			return number
		except ValueError as err:
			print("Error", err)

main()

