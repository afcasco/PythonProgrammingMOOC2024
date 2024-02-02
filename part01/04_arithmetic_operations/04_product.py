# This program asks the user for three numbers. The program then prints out their product, that is, the numbers
# multiplied by each other. There is, however, something wrong with the program - it doesn('t work quite right, as you'
# ' can see if you run it. Please fix it.)
#
# An example of the expected execution of the program:
# Sample output
#
# Please type in the first number: 2
# Please type in the second number: 3
# Please type in the third number: 5
# The product is 30

# Fix the code
number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))

product = number1 * number2 * number3

print("The product is", product)
