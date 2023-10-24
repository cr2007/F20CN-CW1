
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_letter_count(message) -> dict:
	"""
	Returns a dictionary with keys of single letters and values of the count
	of how many times they appear in the message parameter.

	Args:
		message (str): The string to count the letters of.

	Returns:
		dict: A dictionary with keys of single letters and values of the count
		of how many times they appear in the message parameter.

	Raises:
		TypeError: If the message parameter is not a string.
	"""

	# Initialises the dictionary with all letters and a value of 0.
	letter_count = {letter: 0 for letter in LETTERS}
	
	for letter in message.upper():
		if letter in LETTERS:
			letter_count[letter] += 1

	return letter_count


def get_item_at_index_zero(items):
	"""Returns the item at index zero.

	Args:
		items (list): A list of items.

	Returns:
		any: The first item in the given list.

	Raises:
		IndexError: If the given list is empty.
	"""
	return items[0]


def get_frequency_order(message: str) -> list[tuple]:
	"""
	Returns a list of tuples containing the characters in the message parameter
	and their frequency, sorted by frequency in descending order.

	Args:
		message (str): The string to count the letters of.

	Returns:
		list[tuple]: A list of tuples containing the character and its frequency,
		sorted by frequency in descending order.

	Raises:
		TypeError: If the message parameter is not a string.
	"""

	# First, get a dictionary of each letter and its frequency count:
	letterToFreq = get_letter_count(message)

	# Second, make a dictionary of each frequency count to the letter(s)
	# with that frequency:
	freq_to_letter = {}
	for letter in LETTERS:
		if letterToFreq[letter] not in freq_to_letter:
			freq_to_letter[letterToFreq[letter]] = [letter]
		else:
			freq_to_letter[letterToFreq[letter]].append(letter)

	# Third, put each list of letters in reverse "ETAOIN" order, and then
	# convert it to a string:
	for freq in freq_to_letter:
		freq_to_letter[freq].sort(key=ETAOIN.find, reverse=True)
		freq_to_letter[freq] = ''.join(freq_to_letter[freq])

	# Fourth, convert the freqToLetter dictionary to a list of
	# tuple pairs (key, value), and then sort them:
	freq_pairs = list(freq_to_letter.items())
	freq_pairs.sort(key=get_item_at_index_zero, reverse=True)

	# Fifth, now that the letters are ordered by frequency, extract all
	# the letters for the final string:
	# freq_order = []
	freq_dict = {}
	for freq_pair in freq_pairs:
		# freqOrder.append(freqPair[1])
		freq_dict[freq_pair[0]] = freq_pair[1]

	# return ''.join(freqOrder)
	# return freqDict
	return freq_pairs
