# Please write a new version of the program in the previous exercise. In addition to the result it should
# also print out the calculation performed:
# Sample output
#
# Limit: 2
# The consecutive sum: 1 + 2 = 3
# Sample output
#
# Limit: 10
# The consecutive sum: 1 + 2 + 3 + 4 = 10
# Sample output
#
# Limit: 18
# The consecutive sum: 1 + 2 + 3 + 4 + 5 + 6 = 21
#
# You may assume the number typed in by the user is always equal to 2 or higher.

limit = int(input("Limit: "))

result = 0

i = 1

message = "The consecutive sum: "
while i <= limit:

    if result < limit:
        message += str(i)
        result += i
    i += 1
    if result < limit:
        message += " + "

message += f" = {result}"

print(message)
