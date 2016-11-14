import operator

def word_counter(filename):
	file = open(filename)
	dictionary = {}
	for word in file.read().lower().split():
		word = word.strip(',-.:;?!')
		if not word=='':
			if word not in dictionary:
				dictionary[word] = 1
			else:
				dictionary[word] += 1
	file.close()
	s_dict = sorted(dictionary.items(), key=operator.itemgetter(1))
	return s_dict
print(word_counter('inwokacja.txt'))
