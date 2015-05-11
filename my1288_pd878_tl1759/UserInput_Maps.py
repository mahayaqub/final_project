####################################################################################################
#
#
#	Author : Liwen Tian(tl1759)
#	DS GA 1007
#	Final Project
#
#	This is the users input module.
#
####################################################################################################

# Import all the built in libraries
import sys

# Import all the required modules
from cleanup_MapData import *
from Plot_Maps import *

# Define the list of agencies 
agencyList = ['HPD','DOT','NYPD','FDNY','DEP','DOHMH','DPR','TLC']

def get_agency():

	print "Choose from the following list of agencies:"
	print agencyList


	# Define a while loop which takes input untill the correct input is given
	while True:
		try:
			agency = raw_input().upper()

			# Check if the agency id in the list
			if agency in agencyList:
				return agency
			else:
				print "Please select the correct agency."
		# Check for invalid inputs
		except ValueError:
			print "\nOops!  Invalid input."
		except KeyboardInterrupt:
			print '\nYou pressed Ctrl+C! Exiting...'
			sys.exit()



