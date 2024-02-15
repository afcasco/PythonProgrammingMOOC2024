# Please write a program which asks the user for a string and then prints out a frame of * characters with the
# word in the centre. The width of the frame should be 30 characters. You may assume the input string will always
# fit inside the frame.
#
# If the length of the input string is an odd number, you may print out the word in either of the two possible
# centre locations.
# Sample output
#
# Word: testing
#
# ******************************
# *          testing           *
# ******************************
#
# Sample output
#
# Word: python
#
# ******************************
# *           python           *
# ******************************


string = input("Word: ")

left_offset = (29 - len(string)) // 2

right_offset = left_offset if len(string) % 2 == 0 else left_offset - 1

print("*" * 30)
print(f"*{' ' * left_offset}{string}{' ' * right_offset}*")
print("*" * 30)
