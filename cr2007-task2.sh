#!/bin/bash

# CHANDRASHEKHAR RAMAPRASAD (cr2007)
# This script decrypts a file using a password that is a combination of a word from a dictionary and a digit
# The script takes a single argument, which is the name of the file to decrypt

# Make sure the script has execute permissions
# chmod +x cr2007-task2.sh

# -----------------------------------------------------------------------------
# Run the script with the name of the file to decrypt as the first argument
# Usage: ./cr2007-task2.sh <cipherfile>
# -----------------------------------------------------------------------------


# Link filedescriptor 10 with stdin to save the current state of stdin
exec 10<&0
# Replace stdin with a file supplied as a first argument to read from the file instead of standard input
exec < $1

# Remember the name of the input file for later use
in=$1

# Initialize variables for the dictionary file and the known prefix of the decrypted text
dictionary_file="words_shortened.txt"     # the file containing the list of words to use as passwords
known_prefix="Our shared secret word is:" # the prefix of the decrypted text that we are looking for

# Iterate through the dictionary file to try different passwords
while read -r password; do
    # Generate passwords by appending digits to the words in the dictionary
    for digit in {0..9}; do
        combined_password="${password}${digit}"

        # Decrypt the input file using the current password
        decrypted_text=$(openssl enc -aes-128-cbc -d -in $in -k "${combined_password}" -nosalt -md sha256 2> /dev/null | tr -d '\0')

        # Check if the decrypted text contains the known prefix
        if [[ "$decrypted_text" == *"$known_prefix"* ]]; then
            # Print the password and decrypted text if the prefix is found
            echo "Password found: ${combined_password}"
            echo -e "Plaintext: ${decrypted_text}"
            exit 0
        fi

    done
done < "${dictionary_file}"

# Print a message if the password is not found in the dictionary or the prefix is not present in the decrypted text
echo "Password not found in the dictionary, or the prefix is not present in the decrypted text"

# Print a message if decryption fails with all passwords in the word list
echo "Decryption failed with all passwords in the word list"
exit 1