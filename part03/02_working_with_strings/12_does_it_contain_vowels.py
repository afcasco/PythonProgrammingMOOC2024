# Please write a program which asks the user to input a string. The program then prints out different
# messages if the string contains any of the vowels a, e or o.
#
# You may assume the input will be in lowercase entirely. Have a look at the examples below.
# Sample output
#
# Please type in a string: hello there
# a not found
# e found
# o found
# Sample output
#
# Please type in a string: hiya
# a found
# e not found
# o not found

import re

vowels = "aeo"

string = input("Please type in a string: ")

for letter in vowels:
    if re.search(letter, string):
        print(f"{letter} found")
    else:
        print(f"{letter} not found")
