# WARNING: Do not use this as a password validation or password checker!

# This is a basic password checker that promps the user for thier password 
# if it is ture it will print a greeting. If not, the user will have 3 attempts
# to enter thier password correctly or the system will print an err msg then exit(). 

# Where did I learn how to do this? Check out: https://teamtreehouse.com/about

import sys #import system routines

MASTER_PASSWORD = "lab0"
password = raw_input("Please enter your password: ")
attempt_count = 1
while password != MASTER_PASSWORD:
	if attempt_count > 3:
		sys.exit("Too many invalid password attemts! Good Buy!")
	password = raw_input("Invalid password, try again: ")
	attempt_count += 1
print("Welcome to BlueRaptor.co!")