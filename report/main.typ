// F20CN Coursework 1 Report Document

#import "lib.typ": template
#import "@preview/codly:1.2.0": *
#import "@preview/codly-languages:0.1.1": *
#show: codly-init.with()

#set document(author: "Chandrashekhar R", title: "F20CN Coursework 1 Report - CSK")

#show: template.with()

#text(size: 28pt, font: "Dubai", weight: "medium", "F20CN Coursework 1")\

#text(size: 11pt, font: "Segoe UI", "Course: Computer Network Security")

#link("https://teams.microsoft.com/l/chat/0/0?users=cr2007@hw.ac.uk")[Chandrashekhar Ramaprasad]
(#link("mailto:cr2007@hw.ac.uk?subject=F20CN%20Coursework%201")[cr2007])\
H00356126

\
\

#set align(left)

#outline(indent: 1em)

#pagebreak()

#heading("Task 1: Verifying Key Length Guesses: Vigenère Cipher")

#heading(level: 2, "Pseudo-Code")\

/* ```
message = input("Enter your ciphertext: ")

WHILE True DO
  keyLength = input("Enter your key length guess (0 to exit): ")

  IF (keyLength == 0) THEN
    print "Exiting"
    BREAK
  ELSE
    keyLengthGuess(message, keyLength)
  END IF
END WHILE

FUNCTION keyLengthGuess(cipherMessage, keyLengthGuess)
  FOR i in range(keyLengthGuess)

  subMessageIOC = []

  FOR subMessage in subMessages DO
    // Calculates the Index of Coincidence
    subMessageIOC.append( calculateIOC(subMessage) )

  averageIOC = sum(subMessageIOC) / len(subMessageIOC)

  // (Approximate) IoC value of the English language
  englishIOC = 0.0686

  // Gets absolute difference between averageIOC and englishIOC
  difference = abs(averageIOC - englishIOC)

  IF difference < 0.01:
    PRINT keyLengthGuess + " is a possible key length."
  ELSE:
    PRINT keyLengthGuess + " is not a possible key length."
``` */

#figure(
  image("images/Task1-PseudoCode.png", height: 10.36cm, alt: "Task 1 Pseudo-code"),
  caption: "Task 1 code in the form of Pseudocode",
)

The initial step in determining the key length for the Vigenère Cipher involves calculating the (average) Index of Coincidence (IoC) of the ciphertext, utilizing the key length provided by the user.
The ciphertext is subsequently partitioned into sub-messages by extracting every n#super[th] element in the ciphertext, with n representing the guessed key length.
These sub-messages are then collected into a list and forwarded to a dedicated function for IoC calculation.
The IoC is a metric that quantifies the likelihood of randomly selecting two identical letters from a given text and is assessed based on the frequency analysis of the ciphertext.
Notably, the code for the frequency analysis function was referenced from Chapter 19: "Frequency Analysis" in the book titled "#link("https://inventwithpython.com/cracking/chapter19.html")[Cracking Codes with Python]." #cite(<Cracking-The-Code-Python-Book>)

After computing the IoC values for all the sub-messages, the average IoC value is determined and stored in a designated variable.
It is worth noting that the #underline("approximate IoC value") for English text is known to be around $0.0686$.
The program proceeds to assess the disparity between the calculated average IoC and the expected IoC for English text.
If the average IoC closely approximates the English value of $approx 0.0686$, the program acknowledges the key length guess as highly plausible and provides a corresponding confirmation message.
In cases where the average IoC diverges significantly from the English IoC value, the program issues a message indicating that the guessed key length is not feasible.

#pagebreak()

#heading(level: 2, "Testing")

#figure(
  image("images/Task1-Testing.png"),
  caption: "The testing results from the program as specified in the coursework specification",
) \

During the testing phase, I initiated the experiment by selecting a text containing approximately 600 characters.
This text was subsequently encrypted using the Vigenère cipher, employing the first five characters of my surname as the encryption key.
These characters were entered into the program as prompted.

Following this initial setup, I proceeded to evaluate potential key lengths by inputting values of 4, 5, and 6 into the program.
The program then diligently computed and displayed the (average) Index of Coincidence (IoC) values for each of these key length guesses.
However, it was only for the key length of *5* that the program provided an affirmative indication of a possible match, thereby confirming it as the likely key length.

\

#line(length: 100%)

#pagebreak()

#heading("Task 2: Known-plaintext attack: Symmetric Cipher")

#heading(level: 2, "Pseudo-Code")

/* ```
IF fileArgument IS NOT PRESENT:
  PRINT "Error: No file argument provided."
  PRINT "usage ./cr2007-task2.sh <file>"
  EXIT
END IF

LET in = $1 // Variable for Input File

LET dictionaryFile = "words.txt"
LET knownPrefix = "Our shared secret and word is:"

LET lineNumber = 0

WHILE read(password in dictionaryFile):
  lineNumber++

  FOR i IN (1..9):
    // Appends the digit to the password
    combinedPassword = ${password}${i}

    // Runs the decrypt command
    decryptedText = $(openssl enc -aes-128-cbc -d -in $in -k "${combinedPassword}" -nosalt -md sha256 2> /dev/null | tr -d '\0')

    // Checks if the prefix partially matches the prefix
    IF (decryptedText == *knownPrefix*):
      PRINT "Decrypted Successfully!"
      PRINT "Password found: " + combinedPassword
      PRINT "Plaintext: " + decryptedText
      EXIT
    ELSE:
      PRINT "Password: ${combinedPassword} - Not the Password"
    END IF
  END FOR
END WHILE

PRINT "Password not in the dictionary"
PRINT "Decryption failed"
EXIT
``` */

#figure(
  caption: "Task 2 Pseudo-Code",
  image("images/Task2-PseudoCode.png", alt: "Task 2 Pseudo-code", height: 15.11cm),
)

The shell script validates the presence of a ciphertext file as an argument at the outset; without it, the program halts, emphasizing the necessity of a ciphertext for decryption.
Subsequently, it initializes variables, such as the input file, dictionary file, and a known decryption text prefix.

The script systematically generates passwords by appending single digits (0-9) to dictionary words and decrypts the input file using the `openssl` command.
If the known prefix is found, the script prints the password and decrypted text, concluding with a success message.

Conversely, if the prefix remains absent, the script notifies that the password is incorrect.
In cases where the password isn't found in the dictionary or the prefix isn't present in the decrypted text, the script exits with a message that the decryption failed and exits with an error message.

#line(length: 100%)

#pagebreak()

#heading("Testing", level: 2)

#figure(
  image("images/Task2-Testing.png", alt: "Screenshot of Task 2 Testing"),
  caption: "A screenshot of the shell script output once the ciphertext has been decrypted",
)
\

In the test results, the program executed a thorough brute-force process, exhaustively exploring all potential password combinations until it successfully unveiled the decrypted message aligning with the predetermined prefix.
The output of the program included the password used, the specific dictionary file line position corresponding to this password, and the decrypted plaintext.

This sequence of operations ensured the extraction of the desired message, effectively capturing the essence of the decryption process.

#line(length: 100%)

#align(center, table(
  columns: 2,
  align: left,
  fill: (x, _) =>
  if calc.even(x) { rgb("#262626") } else { white },
  table.cell("Recovered Plaintext"),
  table.cell(`Our shared secret word is: sworn`, align: center),
  table.cell("Key"),
  table.cell(`sworn0`, align: center),
))

#line(length: 100%)

#heading("Appendix")

#heading("Task 1", level: 2)

#heading("Python Code", level: 3)

The code is also publicly available on GitHub: #link("https://github.com/cr2007/F20CN-CW1")

#figure(caption: "Docstring for the Task 1 module and creating a constant with all the 26 alphabets", [```python"""
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
  ```])

#figure(
  caption: "Does a frequency analysis on the ciphertext and returns a dictionary with the letters and the number of times they appear",
  [```python def get_letter_count(cipher_message: str) -> dict:

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
    ```],
)

#figure(
  caption: "A function that calculates the Index of Coincidence for a given message",
  [```python def calculate_index_of_coincidence(
      cipher_message: str,
      debug: bool = False
    ) -> float:

      # Check that the message is a string
      if not isinstance(cipher_message, str):
          raise TypeError("Message must be a string.")

      # Get the length of the message
      message_length: str = len(cipher_message)

      # Debug Code
      if debug:
          print(f"(DEBUG) Message length: {message_length}")

      # Get a dictionary of each letter and its frequency count:
      letter_to_freq: dict = get_letter_count(cipher_message)

      # Calculate the numerator of the Index of Coincidence
      index_of_coincidence: float = index_of_coincidence: float = sum(
            probability * (probability-1)
            for probability
            in letter_to_freq.values()
      )

      # Divide by the denominator
      index_of_coincidence /= ( message_length * (message_length - 1) )

      # Debug Statement
      if debug:
          print(f"(DEBUG) Index of Coincidence: {index_of_coincidence}")

      # Return the calculated IoC value, rounded to 4 decimal places
      return round(index_of_coincidence, 4)
    ```],
)

#figure(
  caption: "A function that calculates the Index of Coincidence for a given message",
  [```python def calculate_index_of_coincidence(
      cipher_message: str,
      debug: bool = False
    ) -> float:

      # Check that the message is a string
      if not isinstance(cipher_message, str):
          raise TypeError("Message must be a string.")

      # Get the length of the message
      message_length: str = len(cipher_message)

      # Debug Code
      if debug:
          print(f"(DEBUG) Message length: {message_length}")

      # Get a dictionary of each letter and its frequency count:
      letter_to_freq: dict = get_letter_count(cipher_message)

      # Calculate the numerator of the Index of Coincidence
      index_of_coincidence: float = index_of_coincidence: float = sum(
            probability * (probability-1)
            for probability
            in letter_to_freq.values()
      )

      # Divide by the denominator
      index_of_coincidence /= ( message_length * (message_length - 1) )

      # Debug Statement
      if debug:
          print(f"(DEBUG) Index of Coincidence: {index_of_coincidence}")

      # Return the calculated IoC value, rounded to 4 decimal places
      return round(index_of_coincidence, 4)
    ```],
)

#figure(
  caption: "Guesses whether the key length of a message by calculating the Index of Coincidence",
  [```python def key_length_guess(
      cipher_message: str,
      key_length_guess: int,
      debug: bool = False
    ):

      # Split the message into sub-messages based on the key length
      sub_messages: list[str] = [
                cipher_message[i::key_length_guess]
                for i
                in range(key_length_guess)
      ]

      # Get the IoC of each sub-message
      sub_message_iocs = [
            calculate_index_of_coincidence(sub_message)
            for sub_message
            in sub_messages
      ]

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
    ```],
)

#figure(
  caption: "Main executing code that takes the user input for the ciphertext and the key length guess and calls the other functions till the user wishes to exit",
  [```python # Prompt the user to enter the ciphertext and store it in the 'message' variable.
  message = input("Enter your ciphertext: ")

  while True:
      # Prompt the user to enter their key length guess and store it in the 'key_length' variable.
      key_length = int(input("Enter your key length guess (0 to exit): "))
      print("") # Blank Line

      # Checks if the user input is complete
      if key_length == 0:
          print("Exiting...") # Print a message indicating that the program is exiting.
          break # Exit the loop
      else: # Otherwise
          key_length_guess(message, key_length)
    ```],
)

#heading("Testing", level: 3)

#heading("Screenshot", level: 4)

#figure(
  caption: "A screenshot of my encryption of my plaintext on the Rumkin site",
  link("https://rumkin.com/tools/cipher/vigenere/")[
    #rect(image("images/Appendix-Task1-Testing.png", alt: "Screenshot of the encrypted plaintext"), stroke: 0.5pt)
  ]
)

#heading("Plaintext", level: 4)

#par(justify: true,)[
  YoucannotworryaboutupsettingeverypersonyoucomeacrossbutyoumustbeselectivelycruelIfyoursuperiorisafallingstarthereisnothingtofearfromoutshininghimDonotbemercifulyourmasterhadnosuchscruplesinhisowncoldbloodedclimbtothetopGaugehisstrengthIfheisweakdiscreetlyhastenhisdownfallOutclooutchannoutsmarthimatkeymomentsIfheisveryweakandreadytofallletnaturetakeitscourseDonotriskoutshiningafeeblesuperioritmightappearcruelorspitefulButifyourmasterisfirminhispositionyetyouknowyourselftobethemorecapablehideyourtimeandbepatientItisthenaturalcourseofthingsthatpowereventuallyfadesandweakensYourmasterwillfallsomedayandifyouplayitrightyouwilloutliveandsomedayoutshinehim
]

#heading("Ciphertext", level: 4)

Pogcp enatl frdyp sogtj gsqti znsek vrkpt isann fuoob vaord jsnui\
pogmj jtneh vlqci zvqln trgea Zfkoj isgpt iiarx jaraa cizgh kadtw\
vrqih eofhx egfou vadfg fmaui jhunx egtib Uozoi seyeg tirua pogrb\
rsfeg yapnd juohh trgpa vsunw zsawc toxdq coadt ucxib statw vtapV\
rusew zsetg vnstw Zftex jwqaz uiecg vefln yaett ehuss fwzfp clAui\
tlaoj kctac eogth dadtw zmmtz vyyob vnfsX whqih medyl vawac urqas\
ptafp clxei eafug vtmkt ztecd lreeS fnatg zswoj kstic znsau venlt\
jubeg zodii dishi rpbep icdut codse ztqfj cBgtx wyaug daett iiefx\
imunw zsboh ztuoc pefyd lkzol pogrh vlrtd sefht doder rpmba vhudt\
pogri zmqac ubqpp kiqni Ztusi yezai lrmlr fudst fffhx egetw rtbol\
vrqvt etgaa cyras vsmns nemkt esKoj immsi vriia cfmla joyes rymns\
zfkoj glmyx krugw kyaul zlxoj kluvt rnpsd depan fufsw znqhx d\

#line(length: 100%)

#heading(level: 2, "Task 2")

#heading(level: 3, "Shell Code")

#figure(caption: "Checking if the file argument was provided", [```sh #!/bin/bash

# CHANDRASHEKHAR RAMAPRASAD (cr2007)
# This script decrypts a file using a password that is a combination of a word from a dictionary and a digit
# The script takes a single argument, which is the name of the file to decrypt

# Make sure the script has execute permissions
# chmod +x cr2007-task2.sh

# -----------------------------------------------------------------------------
# Run the script with the name of the file to decrypt as the first argument
# Usage: ./cr2007-task2.sh <cipherfile>
# -----------------------------------------------------------------------------

# Check if file argument is provided
if [ -z "$1" ]; then
    echo -e "\e[31;1mError:\e[0m No file argument (\e[33mciphertext\e[0m) provided."
    echo "Usage: ./cr2007-task2.sh <file>"
    exit 1
fi
```])

#line(length: 100%)

#figure(
  caption: "Initialising variables before the loop",
  [```sh # Link filedescriptor 10 with stdin to save the current state of stdin
  exec 10<&0
  # Replace stdin with a file supplied as a first argument to read from the file instead of standard input
  exec < $1

  # Remember the name of the input file for later use
  in=$1


  # Initialize variables for the dictionary file and the known prefix of the decrypted text
  dictionary_file="words.txt"     # the file containing the list of words to use as passwords

  known_prefix="Our shared secret word is:" # the prefix of the decrypted text that we are looking for

  line_number=0
  ```],
)

#line(length: 100%)

#figure(
  caption: "The loop sequence that brute-forces every single password generated from the dictionary file and decrypts the input file using the openssl command",
  [```sh # Iterate through the dictionary file to try different passwords
  while read -r password; do
      line_number=$((line_number+1))
      # Generate passwords by appending digits to the words in the dictionary
      for digit in {0..9}; do
          # Append the digit to the current password
          combined_password="${password}${digit}"

          # Decrypt the input file using the current password
          decrypted_text=$(openssl enc -aes-128-cbc -d -in $in -k "${combined_password}" -nosalt -md sha256 2> /dev/null | tr -d '\0')

          # Check if the decrypted text contains the known prefix
          if [[ "$decrypted_text" == *"$known_prefix"* ]]; then
              # Print the password and decrypted text if the prefix is found
              echo -e "\e[32;1mDecryption Success!\e[0m"
              echo "Password found: ${combined_password} (line ${line_number} in ${dictionary_file})"
              echo -e "Plaintext: ${decrypted_text}"
              exit 0
              else
              # Print a message if the prefix is not found
              echo "Password '${combined_password}' - Not the Password"
          fi

      done
  done < "${dictionary_file}"
  ```],
)

#figure(
  caption: "Error message if none of the passwords in the dictionary file were able to decrypt the input file",
  [```sh # Print a message if the password is not found in the dictionary or the prefix is not present in the decrypted text
  echo "Password not found in the dictionary, or the prefix is not present in the decrypted text"

  # Print a message if decryption fails with all passwords in the word list
  echo "Decryption failed with all passwords in the word list"
  exit 1
  ```],
)

#line(length: 100%)

// --------------------------------


#bibliography("bibliography.bib", style: "harvard-cite-them-right")
