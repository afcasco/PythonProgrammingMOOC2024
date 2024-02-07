# Please write a program which asks for the names and ages of two persons. The program should then print out the
# name of the elder.
#
# Some examples of expected behaviour:
#
# Sample output
# Person 1:
# Name: Alan
# Age: 26
# Person 2:
# Name: Ada
# Age: 27
# The elder is Ada
#
# Sample output
# Person 1:
# Name: Bill
# Age: 1
# Person 2:
# Name: Jean
# Age: 1
# Bill and Jean are the same age


print("Person 1: ")
name1 = input("Name: ")
age1 = int(input("Age: "))

print("Person 2: ")
name2 = input("Name: ")
age2 = int(input("Age: "))

if age1 == age2:
    message = f"{name1} and {name2} are the same age"
elif age1 > age2:
    message = f"The elder is {name1}"
else:
    message = f"The elder is {name2}"

print(message)