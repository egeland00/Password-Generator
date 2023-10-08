import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

def generate_password(length, use_symbols, use_numbers, use_capitals):
    """
    Generates a password based on the given criteria.

    Parameters:
    - length: The desired length of the password.
    - use_symbols: A boolean to decide if symbols (special characters) should be used.
    - use_numbers: A boolean to decide if numbers should be used.
    - use_capitals: A boolean to decide if capital letters should be used.

    Returns:
    - A string representing the generated password.
    """
    characters = ascii_lowercase  # Start with only lowercase letters
    password = []  # To build the password step by step

    if use_capitals:
        characters += ascii_uppercase
        password.append(random.choice(ascii_uppercase))
        
    if use_symbols:
        characters += punctuation
        password.append(random.choice(punctuation))
        
    if use_numbers:
        characters += digits
        password.append(random.choice(digits))

    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)
    
    return ''.join(password[:length])
