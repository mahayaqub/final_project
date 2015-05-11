##############################################################
#
#
#	Author : Maha Yaqub (my1288)
#	DS GA 1007
#	Final Project
#
#	This module contains the class for plotting the data by borough and time interval
#	It also has the function which plots a time series for the selected agency
#
#
##############################################################

import matplotlib.pyplot as plt

from TimeInterval import *
from BoroughSeparation import *
from AgencySeparation import *

# This class will take in the start and end of the time interval and then plot the time series of complaints for each borough
class Plot_TimeSeries:

	# The constructor function which defines the class variable
	def __init__(self, start, end):

		self.start = start
		self.end  = end

	# Function defined to save the plots
	def Plot_BoroGraphs(self, dataset):

		# Clean up the dataset according to the requirements
		dataset = get_TimeInterval(dataset, self.start, self.end)
		dataset = boroughData(dataset)

		# Give plot commands and save the plot to a pdf
		dataset.plot(title = 'Number of complaints between ' + str(self.start) +'/2014 and ' + str(self.end) + '/2014 for each Borough')
		plt.ylabel('Number of Complaints')
		plt.xlabel('Dates')

		plt.savefig('TimeSeries_NYC_Complaints.pdf')
		plt.show()
		plt.clf()


	def Plot_AgencyGraphs(self, dataset, agency):

		# Clean up the dataset according to the requirements
		dataset = get_TimeInterval(dataset, self.start, self.end)
		dataset = AgencyData(dataset, agency)

		# Give plot commands and save the plot to a pdf
		dataset.plot(title = 'Number of complaints between ' + str(self.start) +'/2014 and ' + str(self.end) + '/2014 for ' + agency)
		plt.ylabel('Number of Complaints')
		plt.xlabel('Dates')
		
		plot_filename = 'Complaints_for_' + agency + '.pdf'
		plt.savefig(plot_filename)
		plt.show()
		plt.clf()







