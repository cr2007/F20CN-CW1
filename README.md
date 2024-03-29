# Computer Network Security (F20CN)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/cr2007/F20CN-CW1)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://f20cn-cw1.streamlit.app)

<div align="center">
  <img alt="Python" title="Python Programming Language" src="https://img.shields.io/badge/Python-informational?style=flat-sqaure&logo=python&logoColor=white&color=3776ab">
  <img alt="Bash" title="Bourne Again SHell" src="https://img.shields.io/badge/Bash-informational?style=flat-sqaure&logo=gnubash&logoColor=white&color=4EAA25">
</div>

## Coursework 1

This repository contains the code and report for Coursework 1. The coursework consists of 2 tasks related to cryptography and network security.

### Task 1: Verifying Key Length Guesses: Vigenere Cipher

This task is written in Python and implements a function that guesses the key length of a ciphertext encrypted with the Vigenere cipher.

Tasks:
- [X] Write a Python program
  - [X] Input a ciphertext (encrypted with a Vigenere cipher) and guess of one or more possible key lengths
  - [X] Output
    - [X] Value of the Index of Coincidence (IC) for each key length guess
    - [X] Indication of which key length guess is most likely to be correct
      - This will be the key length guess where the IC value is closest to the known value of the IC for English language
text
- [X] Testing
  - [X] Find a plaintext example of English text (at least 1000 words in length)
  - [X] Encrypt it with the Vigenere cipher at https://rumkin.com/tools/cipher/vigenere with the **Cipher** key equal to the first 5 characters of your surname
  - [X] The results for the key length guesses should be 4, 5, and 6.

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
  - [ ] Create a loop to read each line and use it as a password? In bash
