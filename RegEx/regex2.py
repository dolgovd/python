# re — Regular expression operations¶
# https://docs.python.org/3/library/re.html

import re

# Input data
string = '''It is a sentence. 
Here is another sentence.
This sentence includes numbers: 1, 2, 4, 5, 6, 7, 8, 9, 0, Y10
An done more with symbols: "!", "@", "-", "&", "?", "_"
a\\b\tc
И это тоже предложение
'''
# Get words, digits, and "_"
# pattern = r'\w+'

# Get only letters
# pattern = r'[th]+'

# Get cyrillic and digits
# pattern = r'[а-я0-9]+'

# # Get digits and symbol "-"
# pattern = r'[\d-]+'

# print(re.findall(pattern, string))

# email: name@gmail.com
def validate_email(email):
    return bool(re.match(r'^.+@\w+\.[a-z]{2,6}$', email, re.IGNORECASE))

print(validate_email('name@gmail.com'))
print(validate_email('name@gmail.infonet'))