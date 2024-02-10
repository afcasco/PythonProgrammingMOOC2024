# Please change the program from the previous exercise so that the user gets to input also the base which
# is multiplied (in the previous program the base was always 2).
# Sample output
#
# Upper limit: 27
# Base: 3
# 1
# 3
# 9
# 27
# Sample output
#
# Upper limit: 1234567
# Base: 10
# 1
# 10
# 100
# 1000
# 10000
# 100000
# 1000000
#
# Please don't use the value True as the condition of your while loop in this exercise!

upper_limit = int(input("Upper limit: "))
base = int(input("Base: "))

current = 1

while current <= upper_limit:
    print(current)
    current *= base
