#   Name: Zhiyuan Lu
#   ID: 1579058
#   CMPUT 274, Fall 2018
#
#   Weekly Exercise #1: password validator
# --------------------------------

import string
import random
def validate(password):
    """ Analyzes an input password to determine if it is "Secure",
    "Insecure", or "Invalid" based on the assignment description
    criteria.

    Arguments:
        password (string): a string of characters

    Returns:
        result (string): either "Secure", "Insecure", or "Invalid".
    """
    forbid_character_list = [" ", "-", "_"]
    special_character = "!#\$\%&'()*+,./:;<=>?@[]^`{|}"
    password_upper = False
    password_islower = False
    password_isdigit = False
    password_special = False
    if len(password) < 8:
        return "Invalid"
    
    for i in forbid_character_list:
        if i in password:
            return "Invalid"

    for j in password:

        if j.isupper():
            password_upper = True

        if j.islower():
            password_islower = True

        if j.isdigit():
            password_isdigit = True

        if j in special_character:
            password_special = True

    if password_upper and password_islower and password_isdigit and password_special:
        return "Secure"
    else:
        return "Insecure"


def generate(n):
    """ Generates a password of length n which is guaranteed to
    be Secure according to the given criteria.

    Arguments:
        n (integer): the length of the password to generate, n >= 8.

    Returns:
        secure_password (string): a Secure password of length n.
    """
    if n < 8:
        print("A secure password should contain 8 or more characters")
    special_char = "!#$%&’()*+,./:;<=>?@[]^‘{|}~"
    pwd = ""
    char_type = [string.ascii_uppercase, string.ascii_lowercase, string.digits, special_char]
    # generate the password until one is valid
    # however, in most of the case, the loop would only run once
    while True:
        pwd = ''.join(random.choices(''.join(char_type), k=n))
        if validate(pwd) == "Secure":
            return pwd  


if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 validator.py". This can be useful for
    # testing your implementations by calling them here.

    Validate = validate(input("Enter a string>"))
    # Validate = validate("helloworld!")
    print(Validate)
    n = int(input("Enter a password length>"))
    res = generate(n)
    print(res)