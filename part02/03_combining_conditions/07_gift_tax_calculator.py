# Some say paying taxes makes Finns happy, so let's see if the secret of happiness lies in one of the taxes set out in Finnish tax code.
#
# According to the Finnish Tax Administration, a gift is a transfer of property to another person against no compensation
# or payment. If the total value of the gifts you receive from the same donor in the course of 3 years is €5,000 or more,
# you must pay gift tax.
#
# When the gift is received from a close relative or a family member, the amount of tax to be paid is determined by the
# following table, which is also available on this website:
# Value of gift	Tax at the lower limit	Tax rate for the exceeding part (%)
# 5 000 — 25 000	100	8
# 25 000 — 55 000	1 700	10
# 55 000 — 200 000	4 700	12
# 200 000 — 1 000 000	22 100	15
# 1 000 000 —	142 100	17
#
# So, for a gift of 6 000 euros the recipient pays a tax of 180 euros (100 + (6 000 - 5 000) * 0.08). Similarly, for a
# gift of 75 000 euros the recipient pays a tax of 7 100 euros (4 700 + (75 000 - 55 000) * 0.12).
#
# Please write a program which calculates the correct amount of tax for a gift from a close relative. Have a look at the
# examples below to see what is expected. Notice the lack of thousands separators in the input values - you may assume
# there will be no spaces or other thousands separators in the numbers in the input, as we haven('t yet covered dealing'
#                                                                                                ' with these.)
# Sample output
#
# Value of gift: 3500
# No tax!
# Sample output
#
# Value of gift: 5000
# Amount of tax: 100.0 euros
# Sample output
#
# Value of gift: 27500
# Amount of tax: 1950.0 euros

year = int(input("Please type in a year: "))

if year % 4 == 0:

    if year % 100 == 0:
        if year % 400 == 0:
            print("That year is a leap year.")
        else:
            print("That year is not a leap year.")
