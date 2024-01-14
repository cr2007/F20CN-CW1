"""
This module contains functions to calculate the Index of Coincidence (IoC) for a given message.
The IoC is a measure of how similar the frequency distribution of letters in a message is to the
expected frequency distribution of letters in the language the message is written in.
A higher IoC value indicates a higher likelihood that the message is written in the language.

Functions:
    get_letter_count(message: str) -> dict:
        Returns a dictionary with keys of single letters and values of the count of how many times
        they appear in the message parameter.

    calculate_index_of_coincidence(message: str, debug: bool = False) -> float:
        Calculates the Index of Coincidence (IoC) for a given message.
"""

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'                # All letters in English

# Source: https://inventwithpython.com/cracking/chapter19.html
def get_letter_count(cipher_message: str) -> dict:
    """
    Returns a dictionary with keys of single letters and values of the count of how many times they
    appear in the message parameter.

    Args:
        message (str): The string to count the letters of.

    Returns:
        dict: A dictionary with keys of single letters and values of the count of how many times
        they appear in the message parameter.

    Raises:
        TypeError: If the message parameter is not a string.
    """

    # Check that the message is a string
    if not isinstance(cipher_message, str):
        raise TypeError("Message must be a string.")

    # Initialises the dictionary with all letters and a value of 0.
    letter_count: dict = {letter: 0 for letter in LETTERS}

    # Count the frequency of each letter in the message
    for letter in cipher_message.upper():
        letter_count[letter] += 1 if letter in LETTERS else 0

    # Return the dictionary
    return letter_count


def calculate_index_of_coincidence(cipher_message: str, debug: bool = False) -> float:
    """
    Calculates the Index of Coincidence (IoC) for a given message.

    The IoC is a measure of how similar the frequency distribution of letters in
    a message is to the expected frequency distribution of letters in the
    language the message is written in. A higher IoC value indicates a higher
    likelihood that the message is written in the language.

    Args:
        message (str): The message to calculate the IoC for.
        debug (bool, optional): Whether to print debug information to the
        console. Defaults to False.

    Returns:
        float: The calculated IoC value, rounded to 4 decimal places.

    Raises:
        TypeError: If the message argument is not a string.

    """

    # Check that the message is a string
    if not isinstance(cipher_message, str):
        raise TypeError("Message must be a string.")

    # Get the length of the message
    message_length: int = len(cipher_message)

    # Debug Code
    if debug:
        print(f"(DEBUG) Message length: {message_length}")

    # Get a dictionary of each letter and its frequency count:
    letter_to_freq: dict = get_letter_count(cipher_message)

    # Calculate the numerator of the Index of Coincidence
    index_of_coincidence: float = sum( probability * (probability-1) for probability in
                                      letter_to_freq.values() )

    # Divide by the denominator
    index_of_coincidence /= ( message_length * (message_length - 1) )

    # Debug Statement
    if debug:
        print(f"(DEBUG) Index of Coincidence: {index_of_coincidence}")

    # Return the calculated IoC value, rounded to 4 decimal places
    return round(index_of_coincidence, 4)


def key_length_guess(cipher_message: str, key_length_guess: int, debug: bool = False):
    """
    Guesses the key length of a given message by calculating the Index of Coincidence (IoC) for each
    sub-message obtained by splitting the message into segments of length equal to the key length.
    The function then calculates the average IoC of the sub-messages and compares it to the IoC of
    English text (0.0686). If the difference between the two is less than 0.01, the key length is
    considered a possible key length.

    Args:
        message (str): The message to guess the key length of.
        key_length (int): The length of the key to guess.
        debug (bool, optional): Whether to print debug information to the console. Defaults to False

    Raises:
        TypeError: If the message argument is not a string.

    Example:
        >>> message = "Vjku ku c vqigvjkpi vjg qh vjgct yjgp"
        >>> key_length_guess(message, 6)
        2
    """

    # Split the message into sub-messages based on the key length
    sub_messages: list[str] = [cipher_message[i::key_length_guess] for i in range(key_length_guess)]

    # Get the IoC of each sub-message
    sub_message_iocs = [calculate_index_of_coincidence(sub_message) for sub_message in sub_messages]
    if debug:
        print(f"IoC for Key Length {key_length_guess} = {sub_message_iocs}")

    # Calculate the average IoC of the sub-messages
    average_ioc = sum(sub_message_iocs) / len(sub_message_iocs)
    print(f"Average IoC for Key Length {key_length_guess} = {round(average_ioc, 4)}")

    ioc_english: float = 0.0686 # IoC of English text

    # Calculate the difference between the average IoC and the IoC of English language text
    ioc_difference: float = abs(average_ioc - ioc_english)
    if debug:
        print(f"IoC Difference for Key Length {key_length_guess} = {round(ioc_difference, 4)}\n")

    # If the difference is less than 0.01, the key length is considered a possible key length
    if ioc_difference < 0.01:
        print(f"{key_length_guess} is a possible key length.\n")
    else:
        print(f"{key_length_guess} is not a possible key length.\n")

# ---------------------------- #

#### Original Text ####
    # YoucannotworryaboutupsettingeverypersonyoucomeacrossbutyoumustbeselectivelycruelIfyoursuperiorisafallingstarthereisnothingtofearfromoutshininghimDonotbemercifulyourmasterhadnosuchscruplesinhisowncoldbloodedclimbtothetopGaugehisstrengthIfheisweakdiscreetlyhastenhisdownfallOutclooutchannoutsmarthimatkeymomentsIfheisveryweakandreadytofallletnaturetakeitscourseDonotriskoutshiningafeeblesuperioritmightappearcruelorspitefulButifyourmasterisfirminhispositionyetyouknowyourselftobethemorecapablehideyourtimeandbepatientItisthenaturalcourseofthingsthatpowereventuallyfadesandweakensYourmasterwillfallsomedayandifyouplayitrightyouwilloutliveandsomedayoutshinehim

# ---------------------------- #

### Encrypted Message with Key Length 5 ###
# message = "PogcpenatlfrdypsogtjgsqtiznsekvrkptisannfuoobvaordjsnuipogmjjtnehvlqcizvqlntrgeaZfkojisgptiiarxjaraacizghkadtwvrqiheofhxegfouvadfgfmauijhunxegtibUozoiseyegtiruapogrbrsfegyapndjuohhtrgpavsunwzsawctoxdqcoadtucxibstatwvtapVrusewzsetgvnstwZftexjwqazuiecgveflnyaettehussfwzfpclAuitlaojkctaceogthdadtwzmmtzvyyobvnfsXwhqihmedylvawacurqasptafpclxeieafugvtmktztecdlreeSfnatgzswojksticznsauvenltjubegzodiidishirpbepicdutcodseztqfjcBgtxwyaugdaettiiefximunwzsbohztuocpefydlkzolpogrhvlrtdsefhtdoderrpmbavhudtpogrizmqacubqppkiqniZtusiyezailrmlrfudstfffhxegetwrtbolvrqvtetgaacyrasvsmnsnemktesKojimmsivriiacfmlajoyesrymnszfkojglmyxkrugwkyaulzlxojkluvtrnpsddepanfufswznqhxd"

# ---------------------------- #

### Encrypted Message with Key Length 3 ###
# message2 = "EoedowvsoieqerquhqiruegrrlevsuecqiifpodrnkfttvrpzvqisufnmiypvvuteizlxjuotequiztoztemcizxyalruetqetufnezfkfumcrqrdkyahvazvsfrbxzstvddvpgkafzozwodueovpfzozRnprskfusvtacdqiazuaoyiqmeelcovseztawtqebqtoyvsuecdvaeznscypzfrzcgctffdujggzsqpogicgenuegQmedpozvkzfwepoggrmttutepvcqgtufnbvrezsfznbcakznseaumemedkfudlnfyedzswffeveyznskhqiazbeekhkgooiifvwtzctnixcsqmedvlkciyztkfudioadtadazvuhvrUesgthorsqjifzsnvtfvrffoieubkomgpqrrfyetfnqjtdfggvodsefkedkhqiebvnfrnfiosleZftaelknixcyalbqrdyzrqufaiyalrriazbnqjsnltyfsfnozuedwuxrnpjtdrnsvorrlxpognixcbqrbxvtatozkizlekfudjtdrtmxeyj"

# ---------------------------- #

# Prompt the user to enter the ciphertext and store it in the 'message' variable.
try:
    message: str = input("Enter your ciphertext: ")

    while True:
        try:
            # Prompt the user to enter their key length guess and store it in the 'key_length' variable.
            key_length = int(input("Enter your key length guess (0 to exit): "))
            print("") # Blank Line

            # Checks if the user input is complete
            if key_length == 0:
                print("Exiting...") # Print a message indicating that the program is exiting.
                break # Exit the loop
            else: # Otherwise
                key_length_guess(message, key_length)
        except ValueError:
            print("Invalid Input. Please enter a number.")
except KeyboardInterrupt:
    # Enter a message when the user presses Ctrl+C and exits the program
    print("\nExiting Program...")
    print("Have a nice day :)")
