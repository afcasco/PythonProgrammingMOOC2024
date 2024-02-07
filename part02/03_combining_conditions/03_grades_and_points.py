# The table below outlines the grade boundaries on a certain university course. Please write a program
# which asks for the amount of points received and then prints out the grade attained according to the table.
# points	grade
# < 0	impossible!
# 0-49	fail
# 50-59	1
# 60-69	2
# 70-79	3
# 80-89	4
# 90-100	5
# > 100	impossible!
#
# Some examples:
# Sample output
#
# How many points [0-100]: 37
# Grade: fail
# Sample output
#
# How many points [0-100]: 76
# Grade: 3
# Sample output
#
# How many points [0-100]: -3
# Grade: impossible!

points = int(input("How many points [0-100]: "))

grade = "impossible!"

if 0 <= points < 50:
    grade = "fail"
elif 50 <= points < 60:
    grade = 1
elif 60 <= points < 70:
    grade = 2
elif 70 <= points < 80:
    grade = 3
elif 80 <= points < 90:
    grade = 4
elif 90 <= points <= 100:
    grade = 5
else:
    grade = "impossible!"

print("Grade: " + str(grade))
