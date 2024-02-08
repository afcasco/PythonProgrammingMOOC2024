# Generally, any year that is divisible by four is a leap year. However, if the year is additionally divisible by 100,
# it is a leap year only if it also divisible by 400.
#
# Please write a program which asks the user for a year, and then prints out whether that year is a leap
# year or not.
#
# Some examples:
# Sample output
#
# Please type in a year: 2011
# That year is not a leap year.
# Sample output
#
# Please type in a year: 2020
# That year is a leap year.
# Sample output
#
# Please type in a year: 1800
# That year is not a leap year.


year = int(input("Please type in a year: "))

leap = False

if year % 4 == 0:
    leap = True
    if year % 100 == 0:
        if year % 400 == 0:
            leap = True
        else:
            leap = False

message = "That year is a leap year." if leap else "That year is not a leap year."

print(message)

