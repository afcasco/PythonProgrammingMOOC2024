# Please write a program which asks the user for their name and year of birth. The program then prints out a message as
# follows:
# Sample output
#
# What is your name? Frances Fictitious
# Which year were you born? 1990
# Hi Frances Fictitious, you will be 31 years old at the end of the year 2021
import datetime

name = input("What is your name? ")
year = int(input("Which year were you born? "))
print(f"Hi {name}, you will be {2021-year} years old at the end of the year 2021")
