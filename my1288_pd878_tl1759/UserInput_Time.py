##############################################################
#
#
#	Author : Maha Yaqub (my1288)
#	DS GA 1007
#	Final Project
#
#	This file contains the function that takes the correct input from the user
#	First it will take the input for the time interval
#	Then it will ask the user whether they want to analyze the data by borough or by agency
#	The function will keep taking input from the user until the user types in 'finish'
#
##############################################################

import sys

# This function takes the input from the user
def TakeUserInput_month():

	# Set a boolean variable to keep track of the while loop
	check = True

	# Run a while loop to keep on taking inputs from the user until finish is entered
	while (check == True):

		# use the try/except statements to check whether the user gives the correct input
		try:
			month = raw_input()

			# Check whether the input is actually a year. This sets x to True so that further tests can be applied
			try:
				int(month)
				x = True
			# exit the function if finish is typed in or raise an error for a wrong format
			except:
				if (month.capitalize() == 'Finish'):
					check = False
					return 'Finish'
				else:
					print "You have typed the month in wrong format. Please enter numbers 1 to 12"
					x = False

		# Exits the program if there is a keyboard interrupt
		except (KeyboardInterrupt, SystemExit):
			sys.exit()

		# Check for the other errors possible
		if (x==True):
			if (int(month)<1) or (int(month)>12):
				print "These are not valid months. Try again."
			else:
				check = False

	return int(month)

# Define a function which takes in the start month and compares it with the end month
# Start month should not be greater than the end
def TakeUserInput():

	print "Please enter the month between 1 (January) and 12 (December) for the time interval. Type 'Finish' to exit."

	while True:
		try:
			# Take the start month from the user
			print "Please enter the start month."
			start_month = TakeUserInput_month()
			# Check if the user entered finish
			try:
				if start_month.capitalize()=='Finish':
					return "Finish"
			except:
				pass

			# Take the end month from user
			print "Please enter the end month."
			end_month = TakeUserInput_month()
			# Check if the user entered finish
			try:
				if end_month.capitalize()=='Finish':
					return "Finish"
			except:
				pass

		except (KeyboardInterrupt, SystemExit):
			sys.exit()

		if int(start_month)>int(end_month):
			print "Please enter the correct format. The end month should be greater or equal than the start month."
		else:
			return start_month,end_month

