numbers = []
data = [0, 0]
lines = ['count = ', ' sum = ', ' lowest = ', ' highest = ', ' mean = ', ' mediana = ']

while True:
	try:
		a = input("enter a number or Enter to finish: ")
		if a: 
			numbers.append(int(a))
			data[0] += 1;
			data[1] += int(a)

			try:
				if int(a) < data[2]:
					data[2] = int(a)
				if int(a) > data[3]:
					data[3] = int(a);
			except IndexError:
				data.append(int(a))
				data.append(int(a))
		else:
			break
	except ValueError:
		print()
data.append(data[1] / data[0])		
print('numbers: ', numbers)
i = 1 
while i < len(numbers):
	j = 1
	while j < len(numbers):
		if(numbers[j] < numbers[j-1]):
			numbers[j-1], numbers[j] = numbers[j], numbers[j-1]
		j += 1
	i += 1

if int(len(numbers) / 2) != len(numbers) / 2:
	data.append(numbers[int(len(numbers) / 2)])
else:
	data.append((numbers[int(len(numbers) / 2)] + numbers[int(len(numbers) / 2) - 1]) / 2)

print('sorted numbers: ', numbers)

i = 0
line = ''

while i < len(lines):
	line += lines[i]
	line += str(data[i])
	i += 1
print(line)