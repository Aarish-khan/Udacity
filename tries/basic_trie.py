basic_trie = {
	
	'a':{ 'word_end':True, 'd':{'word_end':False, 'd':{'word_end':True}}},

	'h':{'word_end':False, 'i':{'word_end':True}}
}


print('Is "a"   a word: {}'.format(basic_trie['a']['word_end']))
print('Is "ad"  a word: {}'.format(basic_trie['a']['d']['word_end']))
print('Is "add" a word: {}'.format(basic_trie['a']['d']['d']['word_end']))

print('Is "hi" a word: {}'.format(basic_trie['h']['i']['word_end']))


def is_word(word):

	current_node = basic_trie

	for char in word:
		if char not in current_node:
			return False

		current_node = current_node[char]

	return current_node['word_end']


test_word = ['ap', 'add']

for word in test_word:
	if is_word(word):
		print('"{}" is a valid word'.format(word))
	else:
		print('"{}" is not a valid word'.format(word))
