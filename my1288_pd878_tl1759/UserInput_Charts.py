# Name: 	dataframe.py
# Author: 	Pan Ding
# Date: 	May 08, 2015
# Summary:	Defines two functions to get input from the user.
########################################################################################## 

import sys


def get_borough(boroughs):
	''' 
	Lets user input a borough name of NYC
	The function takes a list of Boroughs and check if the input is in the list to make sure it's a valid input.
	'''

	while True:

		try:
			print '\nNow you can specify a Borough and the program will draw a bar plot to visualize the volumn of complaints for each agency in this Borough.\nBoroughs are ' + ', '.join(boroughs[:-1]) + '.'
			print 'You can also enter NYC to visualize the city data.'
			borough = raw_input("Enter a borough name (not case-sensitive), or enter 'finish' to exit: ").upper()
			
			if borough in boroughs:		# checks if the input is a valid Borough name
				return borough			
			elif borough == 'FINISH':	# to be used later in the main program to exit the program
				print "\nYou entered 'finish'. Exiting the bar plotting module for Boroughs..."
				return borough
			else:
				print "\nPlease enter the correct format given in the instructions!"
			
        #catches invalid input    
		except ValueError:
			print "\nOops!  Invalid input."
		except KeyboardInterrupt:
			print '\nYou pressed Ctrl+C! Exiting...'
			sys.exit()   


def get_agency(agencies):
	''' 
	Lets user input an agency code. 
	The function takes an agency list and check if the input is in the list to make sure it's a valid input.
	'''
	while True:

		try:
			print '\nSelect an Agency code from the following:\nAgency codes are ' + ', '.join(agencies) + '.'
			agency = raw_input("Enter an Agency code (not case-sensitive), \nEnter 'finish' to exit: ").upper()

			if agency in agencies:		# checks if the input is a valid agency code
				return agency
			elif agency == 'FINISH':	# to be used later in the main program to exit the program
				print "\nYou entered 'finish'. Exiting the pie plotting module for agencies..."
				return agency
			else:
				print "\nPlease enter the correct format given in the instructions!"

		#catches invalid input    
		except ValueError:
			print "\nOops!  Invalid input."
		except KeyboardInterrupt:
			print '\nYou pressed Ctrl+C! Exiting...'
			sys.exit()   



