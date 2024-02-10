# Please write a program which prints out all the even numbers between two and thirty, using a loop.
# Print each number on a separate line.
#
# The beginning of your output should look like this:
# Sample output
#
# 2
# 4
# 6
# 8
# etc...

for x in range(2, 30 + 1):
    if x % 2 == 0:
        print(x)
