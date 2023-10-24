
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
		letter_count[letter] += 1 if letter in LETTERS else 0

	return letter_count


def calculate_index_of_conincidence(message: str, debug: bool=False) -> float:
	# TODO: Implement this function

	message_length: str = len(message)

	# Debug Code
	if debug:
		print(f"(DEBUG) Message length: {message_length}")

	# First, get a dictionary of each letter and its frequency count:
	letter_to_freq = get_letter_count(message)

	# Initialises the Index of Coincidence variable with the numerator
	index_of_coincidence = sum( probability * (probability-1) for probability in letter_to_freq.values() )

	# Divide by the denominator
	index_of_coincidence /= ( message_length * (message_length - 1) )

	# Debug Statement
	if debug:
		print(F"(DEBUG) Index of Coincidence: {index_of_coincidence}")

	return round(index_of_coincidence, 4)
