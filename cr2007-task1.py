
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


def calculate_index_of_conincidence(message: str, debug: bool = False) -> float:
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

	message_length: str = len(message)

	# Debug Code
	if debug:
		print(f"(DEBUG) Message length: {message_length}")

	# First, get a dictionary of each letter and its frequency count:
	letter_to_freq: dict = get_letter_count(message)

	# Initialises the Index of Coincidence variable with the numerator
	index_of_coincidence: float = sum( probability * (probability-1) for probability in letter_to_freq.values() )

	# Divide by the denominator
	index_of_coincidence /= ( message_length * (message_length - 1) )

	# Debug Statement
	if debug:
		print(F"(DEBUG) Index of Coincidence: {index_of_coincidence}")

	return round(index_of_coincidence, 4)


message = "PogcpenatlfrdypsogtjgsqtiznsekvrkptisannfuoobvaordjsnuipogmjjtnehvlqcizvqlntrgeaZfkojisgptiiarxjaraacizghkadtwvrqiheofhxegfouvadfgfmauijhunxegtibUozoiseyegtiruapogrbrsfegyapndjuohhtrgpavsunwzsawctoxdqcoadtucxibstatwvtapVrusewzsetgvnstwZftexjwqazuiecgveflnyaettehussfwzfpclAuitlaojkctaceogthdadtwzmmtzvyyobvnfsXwhqihmedylvawacurqasptafpclxeieafugvtmktztecdlreeSfnatgzswojksticznsauvenltjubegzodiidishirpbepicdutcodseztqfjcBgtxwyaugdaettiiefximunwzsbohztuocpefydlkzolpogrhvlrtdsefhtdoderrpmbavhudtpogrizmqacubqppkiqniZtusiyezailrmlrfudstfffhxegetwrtbolvrqvtetgaacyrasvsmnsnemktesKojimmsivriiacfmlajoyesrymnszfkojglmyxkrugwkyaulzlxojkluvtrnpsddepanfufswznqhxd"

# print(get_letter_count(message))
# print(get_frequency_order(message))
print(calculate_index_of_conincidence(message, True))

