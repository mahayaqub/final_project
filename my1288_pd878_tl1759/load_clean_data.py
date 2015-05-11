# Name: 	load_clean_data.py
# Author: 	Pan Ding
# Date: 	May 08, 2015
# Summary:	1) Defines a class to load the csv file to a dataframe and eliminates the irrelavant columns
# 		2) Defines a function that cleans the dataframe 
########################################################################################## 


import pandas as pd
import sys

class dataframe():
	'''load csv file and select relavant colomns'''

	def __init__(self):
		'''Instantiates a class object'''
		pass

	def load_csv(self):
		'''
		Loads a csv file
		Throws an exception when IOError occurs
		'''
		try:
			print "\nLoading data..."
			df = pd.read_csv(sys.argv[1], dtype = 'unicode', low_memory = False)
		except IOError:
			print 'The file does not exit. Please check your file directory.'
			sys.exit()

		# Select relavent columns
		print "\nJust a few more seconds..."
		return df

def clean_df(df):
	"""
	Removes the rows with NAN values for Boroughs and Agencies
	and removes records unspecified in agency name
	"""
	df_clean = df.dropna(subset = ['Borough', 'Agency'])

	# Drop rows with Agency = 3-1-1
	df_clean = df_clean[df_clean['Agency']!='3-1-1']


	return df_clean

			