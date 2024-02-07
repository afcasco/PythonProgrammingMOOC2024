# Please write a program which asks for the user('s name. If the name is Huey, Dewey or Louie,
# the program should recognise' the user as one of Donald Duck')s nephews.
#
# In a similar fashion, if the name is Morty or Ferdie, the program should recognise the user as one of Mickey Mouse('s
# '
# 'nephews.)
#
# Some examples:
# Sample output
#
# Please type in your name: Morty
# I think you might be one of Mickey Mouse's nephews.
# Sample output
#
# Please type in your name: Huey
# I think you might be one of Donald Duck's nephews.
# Sample output
#
# Please type in your name: Ken
# You're not a nephew of any character I know of.

name = input("Please type in your name: ")

donaldNephews = ["Huey", "Dewey", "Louie"]
mickeyNephews = ["Morty", "Ferdie"]

if name in donaldNephews:
    print("I think you might be one of Donald Duck's nephews.")
elif name in mickeyNephews:
    print("I think you might be one of Mickey Mouse's nephews")
else:
    print("not a nephew of any character I know of")
