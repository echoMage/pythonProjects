# Hello, World! This is my first program using the python language and loving it
# This simple little program intakes the imput the user gives as a user name
# runs it in a function called greeting, displays the greeting to the user, and then
# depending on "if" its the User John or Mark, will output a msg to the user. 
#
# I'm super excited to be learning python and look forward to seeing what else I can do!
# See you soon!

def greeting(user):
	print("Hello," + user)

user = raw_input("What is your user name? \n")

greeting(user)

if user == "John":
	print("Today, " + user + " is learning how to code in python so he can speak to robotics!")
	
elif user == "Mark":
	print("Welcome, " + user)

else:
	print("Meah! Have a nice day {}!".format(user))
	print("Good Bye!")
