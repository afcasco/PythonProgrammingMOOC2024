# Please write a program which asks the user to type in a sentence. The program then prints
# out the first letter of each word in the sentence, each letter on a separate line.
#
# An example of expected behaviour:
# Sample output
#
# Please type in a sentence: Humpty Dumpty sat on a wall
# H
# D
# s
# o
# a
# w

import re

sentence = input("Please type in a sentence: ")

found = re.finditer(' ', sentence)

print(sentence[0])

for match in found:
    print(sentence[match.start() + 1])
