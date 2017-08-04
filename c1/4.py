import random
import sys

articles = ['the', 'a']
nouns = ['cat', 'dog', 'man', 'woman']
verbs = ['sang', 'ran', 'jumped']
adverbs = ['loudly', 'quietly', 'well', 'badly']

i = 0
try:
	count = int(sys.argv[1])
	if 1 > count > 10:		
		count = 5
except ValueError:
	count = 5
except IndexError:
	count = 5

while i < count:
	i += 1
	article = random.choice(articles)
	noun = random.choice(nouns)
	verb = random.choice(verbs)
	adverb = random.choice(adverbs)
	if random.randint(0, 1) == 0:
		print(article, noun, verb)
	else:
		print(article, noun, verb, adverb)




