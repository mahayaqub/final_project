####################################################################################################
#
#
#	Author : Maha Yaqub (my1288)
#	DS GA 1007
#	Final Project
#
#	This is the start page file. It contains the function which will direct the user to the different options of data analysis.
#
####################################################################################################


import ChartsPlot_main as pm
import mapModule as mm
import TimeSeries_Main as ts
import sys

def start_input():

	dataset = pm.load_dataset()

	valid_inputs = ['1', '2', '3']

	while True:

		try:

			print "Hi! Welcome to the NYC 311 Complaint Data Analyzer. \nSelect '1' to analyze the complaints using Bar Charts and Pie Charts. \nSelect '2' for time series of complaints. \nSelect '3' to view a spatial analysis via Maps.\n"

			user_selection = raw_input("Type 'Finish' to exit the program.")

			if user_selection in valid_inputs:
				if user_selection == '1':
					# Runs the Bar Chart and Pie Chart modules
					pm.RunChartModule(dataset)

				elif user_selection == '2':
					# Runs the time series modules
					ts.RunTimeModule(dataset)

				elif user_selection == '3':
					# Runs the map modules
					mm.RunMapModule(dataset)

			# If the user enter finish the program will exit 
			elif user_selection.capitalize() == 'Finish':
				print "\nYou entered Finish. Program is exiting"
				sys.exit()

			# Inform the user to input the correct data
			else:
				print "\nPlease select a valid input."

		except ValueError:
			print "\nWrong input. Try again."

		except KeyboardInterrupt:
			print "\nYou entered Ctrl+C! Exiting..."
			sys.exit()
