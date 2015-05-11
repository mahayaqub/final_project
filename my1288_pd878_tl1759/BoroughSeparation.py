##############################################################
#
#
#	Author : Maha Yaqub (my1288)
#	DS GA 1007
#	Final Project
#
#	This module cleans up the dataset with regard to boroughs
#
#
##############################################################


def boroughData(dataset):

	# Group the dataset by created date and borough 
	grouped = dataset.groupby(['Created Date', 'Borough'])
	# Unstack the dataset to get all the borough plots separately
	dataset = grouped.size().unstack()

	# Remove unwanted field is applicable
	try:
		dataset = dataset.drop(['Unspecified'], axis=1)
	except:
		pass

	return dataset

