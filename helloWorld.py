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