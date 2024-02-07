# Please write a program which asks the user for their age. The program should then print out a message based on
# whether the user is of age or not, using 18 as the age of maturity.
#
# Some examples of expected behaviour:
#
# Sample output
# How old are you? 12
# You are not of age!
#
# Sample output
# How old are you? 32
# You are of age!

age = int(input("How old are you? "))

message = "You are not of age!" if age < 18 else "You are of age!"
print(message)
