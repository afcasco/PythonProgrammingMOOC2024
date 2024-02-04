# Programming exercise:
# Loyalty bonus
# Points:
#
# 0
#
# /
#
# 1
#
# This program calculates the end of year bonus a customer receives on their loyalty card. The bonus is calculated
# with the following formula:
#
#     If there are less than a hundred points on the card, the bonus is 10 %
#     In any other case the bonus is 15 %
#
# The program should work like this:
# Sample output
#
# How many points are on your card? 55
# Your bonus is 10 %
# You now have 60.5 points
#
# But there is a problem with the program, so with some inputs it doesn't work quite right:
# Sample output
#
# How many points are on your card? 95
# Your bonus is 10 %
# Your bonus is 15 %
# You now have 120.175 points
#
# Please fix the program so that there is always either a 10 % or a 15 % bonus, but never both.

points = int(input("How many points are on your card? "))

bonus = 10 if points < 100 else 15

print(f"Your bonus is {bonus} %")

print("You now have {:0.20f} points".format(points + points * bonus / 100))
