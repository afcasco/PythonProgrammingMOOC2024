# Please write a program which asks the user for a number. The program then prints out all integer
# numbers greater than zero but smaller than the input.
# Sample output
#
# Upper limit: 5
# 1
# 2
# 3
# 4
#
# Please don't use the value True as the condition of your while loop in this exercise!

max_num = int(input("Upper limit: "))

for x in range(1, max_num):
    print(x)
