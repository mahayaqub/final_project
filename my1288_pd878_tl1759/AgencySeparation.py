##############################################################
#
#
#	Author : Maha Yaqub (my1288)
#	DS GA 1007
#	Final Project
#
#	This module cleans up the dataset with regard to agencies
#	The function takes in the dataset and the agency name and then it selects the dataset based on the selected agency
#
#
##############################################################


def AgencyData(dataset, agency):

	# Specify the agency that is being analyzed
	dataset = dataset[dataset['Agency']==agency]

	# Group the dataset by created date and borough 
	grouped = dataset.groupby(['Created Date', 'Agency'])

	# Unstack the dataset to get all the borough plots separately
	dataset = grouped.size().unstack()

	return dataset