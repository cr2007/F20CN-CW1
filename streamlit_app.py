import importlib
import streamlit as st

cr2007_task1 = importlib.import_module("cr2007-task1")

st.set_page_config(
    page_title="F20CN CW1 - Task 1",
    page_icon="🔐",
    menu_items= {
        "About": (
            "Task 1 - Coursework 1 of Computer Network Security "
            "([F20CN](https://curriculum.hw.ac.uk/coursedetails/F20CN?termcode=202324))\n"
            "**Source Code:** https://github.com/cr2007/F20CN-CW1"""
            )
    }
)

def main():
    st.title("F20CN Coursework 1", help="Task 1 of the F20CN Coursework 1")

    st.subheader("Task 1: Verifying Key Length Guesses: Vigenère Cipher")

    # Prompt the user to enter the ciphertext and store it in the 'message' variable.
    message: str = st.text_input("Enter your ciphertext: ",
                        placeholder="Ciphertext", help="Encrypted message")

    # Try block to catch ValueError (if the user enters a non-integer value)
    try:
        # Prompt the user to enter their key length guess
        # and store it in the 'key_length' variable.
        key_length: float = st.number_input("Enter your key length",
                                    help="Number of bits in a key", step=1, min_value=1)

        debug_mode: bool = st.checkbox("Debug Mode", help="Enable debug mode to see the" +
                                "Index of Coincidence values")

        if st.button("Submit", type="primary"):
            if message != "":
                with st.spinner("Calculating..."):
                    cr2007_task1.key_length_guess(message, int(key_length), debug=debug_mode)
            else:
                st.info("Please enter a ciphertext", icon="⚠️")
    except ValueError:
        print("Invalid Input. Please enter a number.")

if __name__ == "__main__":
    main()
