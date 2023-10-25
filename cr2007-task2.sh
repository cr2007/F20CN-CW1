#!/bin/bash

# Link filedescriptor 10 with stdin
exec 10<&0
# stdin replaced with a file supplied as a first argument
exec < $1

# remember the name of the input file
in=$1

# init
dictionary_file="words_shortened.txt"

known_prefix="Our shared secret word is:"

while read -r password; do
    for digit in {0..9}; do
        combined_password="${password}${digit}"

        echo "Trying password: ${combined_password}"
        decrypted_text=$(openssl enc -aes-128-cbc -d -in $in -k "${combined_password}" -nosalt -md sha256 2> /dev/null)
        echo "Decrypted text: ${decrypted_text} with length ${#decrypted_text}"


        if [[ "$decrypted_text" == *"$known_prefix"* ]]; then
            echo "Password found: ${combined_password}"
            echo -e "Plaintext: ${decrypted_text}"
            exit 0
        else
            echo "Password ${combined_password} failed"
            echo "Decrypted text: ${decrypted_text}"
            # echo "Known prefix: ${known_prefix}"
        fi

    done
done < "${dictionary_file}"

echo "Password not found in the dictionary, or the prefix is not present in the decrypted text"




echo "Decryption failed with all passwords in the word list"
exit 1