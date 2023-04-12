# re — Regular expression operations¶
# https://docs.python.org/3/library/re.html

import re

# Input data
string = 'It is a sentence. Each sentence consists of words'
pattern = 'sentence'

# Search method
if re.search(pattern, string):
    print('Match')
    print('Position: ' + str(re.search(pattern, string).span()))
    print(re.search(pattern, string).start())
    print(re.search(pattern, string).end())
else:
    print('No match')

# Match method
print(re.match(pattern, string))

# Find all method
print(re.findall(pattern, string))

# Split method
print(re.split(r'\.', string))