
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


def calculate_index_of_conincidence(message: str):
	# TODO: Implement this function

	message_length = len(message)
	print(f"Message length: {message_length}")

	# First, get a dictionary of each letter and its frequency count:
	letter_to_freq = get_letter_count(message)

	# Calculate probability of each letter
	# Initialise dictionary that stores the probability of each letter taken from letter_to_freq
	# letter_probability: dict = {letter: letter_to_freq[letter] / message_length for letter in letter_to_freq}
	# print(letter_probability)

	# Initialises the Index of Coincidence variable with the numerator
	total = sum( probability * (probability-1) for probability in letter_to_freq.values() )
	# for letter, probability in letter_probability.items():
	# 	total += probability**2

	# Divide by the denominator
	total /= ( message_length * (message_length - 1) )

	print(total)
	return round(total, 4)
