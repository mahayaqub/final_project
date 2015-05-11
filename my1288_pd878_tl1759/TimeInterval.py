##############################################################
#
#
#	Author : Maha Yaqub (my1288)
#	DS GA 1007
#	Final Project
#
#	This module cleans up the dataset with regard the given time interval
#
#
##############################################################

# Import any modules that are required
from datetime import datetime

def get_TimeInterval(dataset, start, end):

	try:
		# Convert the date to a datetime object and sort it in ascending order
		dataset['Created Date'] = dataset['Created Date'].apply(lambda x: datetime.strptime(x, '%m/%d/%Y %I:%M:%S %p'))

	except:
		print "The datetime format is incorrect"

	# Create a mask which will take in the dates for the time interval selected by the user
	# Put an if condition to check if it is month 12
	if int(end) == 12:
		mask = (dataset['Created Date']>=datetime(2014, int(start),1)) & (dataset['Created Date']<datetime.datetime(2014, int(end),31,23,59,59))
	else:
		mask = (dataset['Created Date']>=datetime(2014, int(start),1)) & (dataset['Created Date']<datetime(2014, int(end)+1,1,0,0,0))

	# Select the part of the dataset which satisfies the time interval
	dataset = dataset[mask]

	# Convert the dates back into presentable format
	dataset['Created Date'] = dataset['Created Date'].apply(lambda x: x.strftime('%m/%d/%Y'))

	return dataset





