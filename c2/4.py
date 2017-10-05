import sys

def main():
	maxwidth, strFormat = process_options()
	print_start()
	count = 0
	while True:
		try:
			line = input()
			if count == 0:
				color = "lightgreen"
			elif count % 2:
				color = "white"
			else:
				color = "lightyellow"
			print_line(line, color, maxwidth, strFormat)
			count += 1
		except EOFError:
			break
	print_end()

def print_start():
	print("<table border='1'>")

def print_end():
	print("</table>")

def print_line(line, color, maxwidth, strFormat):
	print("<tr bgcolor='{0}'>".format(color))
	fields = extract_fields(line)	
	for field in fields:
		if not field:
			print("<td></td>")
		else:
			number = field.replace(",", "")
			try:
				x = float(number)
				print("<td allign='right'>{0:{1}}</td>".format(round(x), strFormat))
			except ValueError:
				field = field.title()
				field = field.replace(" And ", " and ")
				field = escape_html(field)
				if(len(field) <= maxwidth):
					print("<td>{0}</td>".format(field))
				else:
					print("<td>{0:.{1}}...</td>".format(field, maxwidth))
	print("</tr>")

def extract_fields(line):
	fields = []
	field = ""
	quote = None
	for c in line:
		if c in "\"'":
			if quote is None:
				quote = c
			elif quote == c:
				quote = None
			else:
				field += c
			continue
		if quote is None and c == ",":
			fields.append(field)
			field = ""
		else:
			field += c
	if field:
		fields.append(field)
	return fields


def escape_html(text):
	text = text.replace("&", "&amp;")
	text = text.replace("<", "&lt;")
	text = text.replace(">", "&gt;")
	return text

def process_options():
	if len(sys.argv) == 1:
		return (100, '.0f')
	if len(sys.argv) == 2:
		if(sys.argv[1] in ['-h', '--help']):
			print('usage: {0} [maxwidth] [format]'.format(sys.argv[0]))
			return
		else:
			try:
				return (int(sys.argv[1]), '.0f')
			except FormatError:
				print('Failure input')
				return (100, '.0f')
	try:
		return (int(sys.argv[1]), sys.argv[2])
	except FormatError:
		print('Failure input')
		return (100, sys.argv[2])
			
main()