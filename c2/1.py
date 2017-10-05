import unicodedata
import sys

def print_unicode_table(words):
	print("decimal  hex  chr {0:^40}".format("name"))
	print("------- ----- --- {0:-<40}".format(""))

	code = ord(" ")
	end = sys.maxunicode

	while code < end:
		c = chr(code)
		name = unicodedata.name(c, "*** unknown ***")
		isAllWords = True
		for word in words:
			isAllWords = isAllWords and word.lower() in name.lower()		
		if isAllWords:	
			print("{0:7} {0:5X} {0:^3c} {1}".format(code, name.title()))
		code += 1

words = []

if len(sys.argv) > 1:
	if sys.argv[1] in ('-h', '--help'):
		print("usage : {0} [string] [string] ...".format(sys.argv[0]))
		words = None
	else:
		words = sys.argv[1:]
		print(words)
if words is not None:
	print_unicode_table(words)

