# Please write a program which prints out the following story. The user gives a name and a year, which should be
# inserted into the printout.
#
# Please type in a name: Mary
# Please type in a year: 1572
#
# Mary is a valiant knight, born in the year 1572. One morning Mary woke up to an awful racket: a dragon was approaching
# the village. Only Mary could save the village's residents.
#
# The story should change according to the input given by the user.

name = input("Please type in a name: ")
year = input("Please type in a year: ")

print("{} is a valiant knight, born in the year {}. One morning {} woke up to an awful racket: a dragon was"
      " approaching the village. Only {} could save the village's residents.".format(name, year, name, name))
