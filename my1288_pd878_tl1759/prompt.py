####################################################################################################
#
#
#	Author : Liwen Tian (tl1759)
#	DS GA 1007
#	Final Project
#
#	This is the users input module.
#
####################################################################################################


import sys

def prompt():

	responses = ['Y', 'N', 'y', 'n']

	while True:
		try:
			print 'Do you want to try another method? (y or n)'
			commitmessage = raw_input().upper()

			if commitmessage in responses:
				if commitmessage.upper() == 'Y':
					return True
				elif commitmessage.upper() == 'N':
					return False
			else:
				print "Please type the correct input..."

		#catches invalid input
		except ValueError:
			print "\nOops!  Invalid input."
		except KeyboardInterrupt:
			print '\nYou pressed Ctrl+C! Exiting...'
			sys.exit() 

