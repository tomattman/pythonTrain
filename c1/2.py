numbers = []
data = [0, 0]
lines = ['count = ', ' sum = ', ' lowest = ', ' highest = ', ' mean = ']

while True:
	try:
		a = input("enter a number or Enter to finish: ")
		if a: 
			numbers.append(a)
			data[0] += 1;
			data[1] += int(a)

			try:
				if int(a) < data[2]:
					data[2] = int(a)
				if int(a) > data[3]:
					data[3] = int(a);
			except IndexError:
				data.append(a)
				data.append(a)
		else:
			break
	except ValueError:
data.append(data[1] / data[0])		
print('numbers: ', numbers)

i = 0
line = ''

while i < len(lines):
	line += lines[i]
	line += str(data[i])
	i += 1
print(line)