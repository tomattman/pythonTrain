import cmath
import math
import sys

def get_float(message, allow_zero):
	x = None
	while x is None:
		try:
			x = float(input(message))
			if not allow_zero and abs(x) < sys.float_info.epsilon:
				print('Zero not allowed')
				x = None
		except FormatError as err:
			print(err)
	return x

print("ax\N{SUPERSCRIPT TWO} + bx + c = 0");
a = get_float('input a : ', False)
b = get_float('input b : ', True)
c = get_float('input c : ', True)

x1 = None
x2 = None

dicriminant = (b ** 2) - (4 * a * c)
if dicriminant == 0:
	x1 = -(b / (2 * a))
else:
	if dicriminant > 0:
		root = math.sqrt(dicriminant)
	else:
		root = cmath.sqrt(dicriminant)
	x1 = (-b + root) / (2 * a)
	x2 = (-b - root) / (2 * a)

line = "{0} x\N{SUPERSCRIPT TWO}".format(a)
if b != 0:
	line += " {0:+} x".format(b)
if c != 0:
	line += " {0:+}".format(c)
line += " = 0"
print(line)
print("\N{RIGHTWARDS ARROW} x = {0}".format(x1))
if x2 is not None:
	print('or')
	print("\N{RIGHTWARDS ARROW} x = {0}".format(x2))



