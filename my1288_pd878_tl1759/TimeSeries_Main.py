##############################################################
#
#
#	Author : Maha Yaqub (my1288)
#	DS GA 1007
#	Final Project
#
#	This file contains the code that will take the input from the user and run the time series segment
#
##############################################################

# Import all the required modules
from prompt import *
from UserInput_Time import *
from Plot_TimeSeries import *
from BoroughSeparation import *
from AgencySeparation import *
from TimeInterval import *
import UserInput_Charts as ui


def RunTimeModule(dataset):

	# Define a boolean variable
	x = True

	while (x==True):

		try:
			print "\nType '1' to view a time series of complaints by borough.\nType '2' to view a time series of complaints by agency.\nType 'Finish' to exit."

			method = raw_input()

			if method.capitalize() == 'Finish':
				break

			elif method in ['1', '2']:

				# Put the borough analysis method
				if method == '1':
					time_interval = TakeUserInput()
					try:
						if time_interval.capitalize() == "Finish":
							break
					except:
						print "\nThis will take a few moments...\n"
						time_analysis = Plot_TimeSeries(time_interval[0], time_interval[1])
						time_analysis.Plot_BoroGraphs(dataset)
					x = prompt()

				# Put the agency analysis method
				elif method == '2':
					time_interval = TakeUserInput()
					agencies = list(dataset.Agency.unique())
					agency = ui.get_agency(agencies)
					try:
						if time_interval.capitalize() == "Finish" or agency.capitalize=="Finish":
							break
					except:
						print "\nThis will take a few moments...\n"
						time_analysis = Plot_TimeSeries(time_interval[0], time_interval[1])
						time_analysis.Plot_AgencyGraphs(dataset, agency)
					x = prompt()
			else:
				print "Please type the inputs '1', '2' or 'Finish'."

		except ValueError:
			print "\nOops!  Invalid input."
		except KeyboardInterrupt:
			print '\nYou pressed Ctrl+C! Exiting...'
			sys.exit() 
