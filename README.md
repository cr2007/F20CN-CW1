# Computer Network Security (F20CN)

## Coursework 1

### Task 1: Verifying Key Length Guesses: Vigenere Cipher

Tasks:
- [ ] Write a Python program
  - [ ] Input a ciphertext (encrypted with a Vigenere cipher) and guess of one or more possible key lengths
  - [ ] Output
    - [ ] Value of the Index of Coincidence (IC) for each key length guess
    - [ ] Indication of which key length guess is most likely to be correct
      - This will be
the key length guess where the IC value is closest to the known value of the IC for English language
text
- [ ] Testing
  - [ ] Find a plaintext example of English text (at least 1000 words in length)
  - [ ] Encrypt it with the Vigenere cipher at https://rumkin.com/tools/cipher/vigenere with the **Cipher** key equal to the first 5 characters of your surname
  - [ ] The results for the key length guesses should be 4, 5, and 6.

IC formula

$$
IC = \frac{\sum_{i=1}^{26}f_i * (f_i-1)}{L * (L-1)}
$$

where $f_i$ is the frequency of the $i^{\text{th}}$ letter of the alphabet in the column, and $L$ is the total number of letters in the column.<br>
Note that $IC_{\text{english}} \approx 0.0686$.

### Task 2: Verifying Key Length Guesses: Substitution Cipher

Tasks:

- [ ] Write a Shell Script
  - [ ] Find the
    - [ ] Password
    - [ ] Remainder of the plaintext
  - [ ] Call the `openssl` command and check the resulting file
