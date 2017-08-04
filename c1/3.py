import random

articles = ['the', 'a']
nouns = ['cat', 'dog', 'man', 'woman']
verbs = ['sang', 'ran', 'jumped']
adverbs = ['loudly', 'quietly', 'well', 'badly']

i = 0

while i < 5:
	i += 1
	article = random.choice(articles)
	noun = random.choice(nouns)
	verb = random.choice(verbs)
	adverb = random.choice(adverbs)
	if random.randint(0, 1) == 0:
		print(article, noun, verb)
	else:
		print(article, noun, verb, adverb)




