# Please write a program which asks the user to type in an upper limit. The program then prints out numbers so that each subsequent number is the previous one doubled, starting from the number 1. That is, the program prints out powers of two in
# order.
#
# The execution of the program finishes when the next number to be printed would be greater than the limit set by
# the user. No numbers greater than the limit should be printed.
# Sample output
#
# Upper limit: 8
# 1
# 2
# 4
# 8
# Sample output
#
# Upper limit: 20
# 1
# 2
# 4
# 8
# 16
# Sample output
#
# Upper limit: 100
# 1
# 2
# 4
# 8
# 16
# 32
# 64
#
# Please don't use the value True as the condition of your while loop in this exercise!
#
# What are powers of two? The first power of two is the number 1. The next one is 1 times 2, which is 2.
# The next is 2 times 2, which is 4. The next is 4 times 2, which is 8, and so forth. Each power in the sequence
# is multiplied by two to produce the next one.

upper_limit = int(input("Upper limit: "))

current = 1

while current <= upper_limit:
    print(current)
    current *= 2
