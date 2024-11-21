#age=input("What is your age?\n")
#age=int(age)
#if age>17:print("You are too old")

grade=input("What grade are you in?\n")

# The line `grade=str(grade)` is converting the input value of `grade` to a string data type. This is
# done to ensure that any input provided by the user is treated as a string, regardless of whether the
# user enters a numerical value or a string value. This conversion is necessary for consistency and to
# avoid potential errors when comparing or manipulating the input value later in the code.
grade=str(grade)

if grade<"8" : print("You cannot participate in this event")

elif grade>"8":print("Your event is not in this place")

else:print("You can register and take part in the event")