####################################################################################################
#
#
#	Author : Liwen Tian(tl1759)
#	DS GA 1007
#	Final Project
#
#	
#
####################################################################################################


# Import the in built libraries

import sys
import shapefile
import pandas as pd


# Import all the modules needed for this module to run
from cleanup_MapData import *
from Plot_Maps import *
from UserInput_Maps import *
from prompt import *


def RunMapModule(complaintsdata):

	try:
		# Load zipcode data with pandas
		zipcodedata = pd.read_csv(sys.argv[2]) 

		# Load shapefiles
		dat = shapefile.Reader(sys.argv[3])

		zipBorough = getzipBorough(zipcodedata)
		k  = plotMaps(zipBorough)

	# Check for all the files 
	except IOError:
		raise Exception("Please make sure all the files in the same folder.")
		sys.exit()

	# Check for a keyboard interrupt 
	except KeyboardInterrupt:
		print ('You have interrupted the program!')
		quitproject()

	# Set a boolean variable to check for the while loop
	i = True
	while (i == True):
		# Start to take the input
		try:
			method = raw_input('Which method among the three u want to try?\n(You can type in "Finish" to quit the program.)\n'+"1.Top Agency Complaints for each Zipcode\n"+
				"2.Compare two agencies' complaints\n"+"3.Use circles to represent complaints number for each Zipcode\n"+'Type number 1, 2, or 3:\n')
			if method.capitalize() == 'Finish':
				break

			elif method in ['1', '2', '3']:

				if int(method) == 1:
					print "The map is generating. This will take a few moments..."
					mapPoints = getmapPoints(complaintsdata)
					k.TopAgencyforEachzipCode(mapPoints,dat)
					i = prompt()
				elif int(method) == 2:
					print "\nPlease select the first agency."
					a1 = get_agency()
					print "\nPlease select the second agency."
					a2 = get_agency()
					print "The map is generating. This will take a few moments..."
					agencymapPoints = getagencymapPoints(complaintsdata,a1,a2)
					k.comparetowagencies(agencymapPoints,dat)
					i = prompt()
				elif int(method) ==3:
					print "The map is generating. This will take a few moments..."
					zipmapPoints = getzipmapPoints(complaintsdata)
					k.plotzipcomplaints(zipmapPoints,dat)
					i = prompt()

			else:
				print ('\nPlease select one of the numbers.(1, 2, or 3)\n')
			
		except ValueError:
			raise Exception ('There is a problem with the input you gave, please check it and run the program again.')
		except KeyboardInterrupt:
			print '\nYou pressed Ctrl+C! Exiting...'
			sys.exit() 