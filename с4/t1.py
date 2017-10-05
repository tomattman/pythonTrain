import datetime
import xml.sax.saxutils

COPYRIGHT_TEMPLATE = "copyright (c) {0} {1}. All rights reserved."
STYLESHEET_TEMPLATE = ('<link rel="stylesheet" type"text/css"'
					   'media="all" href="{0}" />\n')
HTML_TEMPLATE = """<?xml version="1.0"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" \
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
<title>{title}</title>
<!-- {copyright} -->
<meta name="Description" content="{description}" />
<meta name="Keywords" content="{keywords}" />
<meta equiv="content-type" content="text/html; charset=utf-8" />
{stylesheet}\
</head>
<body>
</body>
</html>
"""

class CanselledError(Exception): pass

def main():
	information = dict(name = None, year = datetime.date.today().year,
		filename = None, title = None, description = None, keywords = None, stylesheet = None)
	while True:
		try:
			print("\nMake HTML Skeleton\n")
			populate_inormation(information)
			make_html_skeleton(**information)
		except CanselledError:
			print("Canseled")
		if (get_string("\nCreate another (y/n)?", default="y").lower() not in {"y", "yes"}):
			break

def populate_inormation(information):
	name = get_string("Enter your name (for copyright)", "name", information["name"])

	if not name:
		raise CanselledError()
	year = get_integer("Enter copyright year", "year", information["year"], 2000, datetime.date.today().year + 1, True)

	if year == 0:
		raise CanselledError()

	filename = get_string("Enter filename", "filename")
	if not filename:
		raise CanselledError()
	if not filename.endswith((".htm", ".html")):
		filename += ".html"

	title = get_string("Enter title", "title")
	description = get_string("Enter description", "description")
	keywords = get_string("Enter keywords", "keywords").split()
	stylesheet = get_string("Enter stylesheet paths", "stylesheet")

	information.update(name = name, year = year, filename = filename, title = title, description = description,
		keywords = keywords, stylesheet = stylesheet)

def make_html_skeleton(year, name, title, description, keywords, stylesheet, filename):
	copyright = COPYRIGHT_TEMPLATE.format(year, xml.sax.saxutils.escape(name))
	title = xml.sax.saxutils.escape(title)
	description = xml.sax.saxutils.escape(description)
	keywords = ",".join([xml.sax.saxutils.escape(k) for k in keywords]) if keywords else ""
	stylesheet = (STYLESHEET_TEMPLATE.format(stylesheet) if stylesheet else "")
	html = HTML_TEMPLATE.format(title = title, copyright = copyright, description = description,
		keywords = keywords, stylesheet = stylesheet)

	fh = None
	try:
		fh = open(filename, "w", encoding="utf-8")
		fh.write(html)
	except EnvironmentError as err:
		print("Error", err)
	else:
		print("Saved skeleton", filename)
	finally:
		if fh is not None:
			fh.close()

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

