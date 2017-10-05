for line in open("1.txt"):
	for num_line in line.split():
		print(chr(int(num_line, 2)), end = "")