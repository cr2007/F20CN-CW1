"""
This module contains functions to calculate the Index of Coincidence (IoC) for a given message. The IoC is a measure of how similar the frequency distribution of letters in a message is to the expected frequency distribution of letters in the language the message is written in. A higher IoC value indicates a higher likelihood that the message is written in the language.

Functions:
	get_letter_count(message: str) -> dict:
		Returns a dictionary with keys of single letters and values of the count of how many times they appear in the message parameter.

	calculate_index_of_coincidence(message: str, debug: bool = False) -> float:
		Calculates the Index of Coincidence (IoC) for a given message.
"""

ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'  # Most common letters in English
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # All letters in English

def get_letter_count(message: str) -> dict:
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

	# Check that the message is a string
	if not isinstance(message, str):
		raise TypeError("Message must be a string.")

	# Initialises the dictionary with all letters and a value of 0.
	letter_count: dict = {letter: 0 for letter in LETTERS}

	# Count the frequency of each letter in the message
	for letter in message.upper():
		letter_count[letter] += 1 if letter in LETTERS else 0

	# Return the dictionary
	return letter_count


def calculate_index_of_coincidence(message: str, debug: bool = False) -> float:
	"""
	Calculates the Index of Coincidence (IoC) for a given message.

	The IoC is a measure of how similar the frequency distribution of letters in a message is to the expected frequency
	distribution of letters in the language the message is written in. A higher IoC value indicates a higher likelihood
	that the message is written in the language.

	Args:
		message (str): The message to calculate the IoC for.
		debug (bool, optional): Whether to print debug information to the console. Defaults to False.

	Returns:
		float: The calculated IoC value, rounded to 4 decimal places.

	Raises:
		TypeError: If the message argument is not a string.

	"""

	# Check that the message is a string
	if not isinstance(message, str):
		raise TypeError("Message must be a string.")

	# Get the length of the message
	message_length: str = len(message)

	# Debug Code
	if debug:
		print(f"(DEBUG) Message length: {message_length}")

	# Get a dictionary of each letter and its frequency count:
	letter_to_freq: dict = get_letter_count(message)

	# Calculate the numerator of the Index of Coincidence
	index_of_coincidence: float = sum( probability * (probability-1) for probability in letter_to_freq.values() )

	# Divide by the denominator
	index_of_coincidence /= ( message_length * (message_length - 1) )

	# Debug Statement
	if debug:
		print(f"(DEBUG) Index of Coincidence: {index_of_coincidence}")

	# Return the calculated IoC value, rounded to 4 decimal places
	return round(index_of_coincidence, 4)


def key_length_guess(message: str, key_length: int, debug: bool = False):
	"""
	Guesses the key length of a given message by calculating the Index of Coincidence (IoC) for each sub-message
	obtained by splitting the message into segments of length equal to the key length. The function then calculates
	the average IoC of the sub-messages and compares it to the IoC of English text (0.0686). If the difference
	between the two is less than 0.01, the key length is considered a possible key length.

	Args:
		message (str): The message to guess the key length of.
		key_length (int): The length of the key to guess.
		debug (bool, optional): Whether to print debug information to the console. Defaults to False.

	Raises:
		TypeError: If the message argument is not a string.

	Example:
		>>> message = "Vjku ku c vqigvjkpi vjg qh vjgct yjgp"
		>>> key_length_guess(message, 6)
		2
	"""

	# Split the message into sub-messages based on the key length
	sub_messages = [message[i::key_length] for i in range(key_length)]

	# Get the IoC of each sub-message
	sub_message_iocs = [calculate_index_of_coincidence(sub_message) for sub_message in sub_messages]
	if debug:
		print(f"IoC for Key Length {key_length} = {sub_message_iocs}")

	# Get the average IoC of the sub-messages
	average_ioc = sum(sub_message_iocs) / len(sub_message_iocs)
	if debug:
		print(f"Average IoC for Key Length {key_length} = {round(average_ioc, 4)}")

	# Get the closest key length
	ioc_english = 0.0686
	difference = abs(average_ioc - ioc_english)
	if debug:
		print(f"IoC Difference for Key Length {key_length} = {round(difference, 4)}\n")

	# Check if the difference between the average IoC and the IoC of English is less than 0.01
	if abs(average_ioc - ioc_english) < 0.01:
		print(f"Key Length {key_length} is a possible key length.\n")


message = "PogcpenatlfrdypsogtjgsqtiznsekvrkptisannfuoobvaordjsnuipogmjjtnehvlqcizvqlntrgeaZfkojisgptiiarxjaraacizghkadtwvrqiheofhxegfouvadfgfmauijhunxegtibUozoiseyegtiruapogrbrsfegyapndjuohhtrgpavsunwzsawctoxdqcoadtucxibstatwvtapVrusewzsetgvnstwZftexjwqazuiecgveflnyaettehussfwzfpclAuitlaojkctaceogthdadtwzmmtzvyyobvnfsXwhqihmedylvawacurqasptafpclxeieafugvtmktztecdlreeSfnatgzswojksticznsauvenltjubegzodiidishirpbepicdutcodseztqfjcBgtxwyaugdaettiiefximunwzsbohztuocpefydlkzolpogrhvlrtdsefhtdoderrpmbavhudtpogrizmqacubqppkiqniZtusiyezailrmlrfudstfffhxegetwrtbolvrqvtetgaacyrasvsmnsnemktesKojimmsivriiacfmlajoyesrymnszfkojglmyxkrugwkyaulzlxojkluvtrnpsddepanfufswznqhxd"

# print(get_letter_count(message))
# print(get_frequency_order(message))
# print(calculate_index_of_coincidence(message, True))
key_length_guess(message, 4, True)
key_length_guess(message, 5)
key_length_guess(message, 6)