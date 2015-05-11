# Name: 	draw_plots.py
# Author: 	Pan Ding
# Date: 	May 08, 2015
# Summary:	Contains two functions. 
# 			1) draws a bar plot for a given Borough
# 			2) draws a pie plot for a given agency
########################################################################################## 

import matplotlib.pyplot as plt


def draw_boro_bar(df,boro):
	'''
	Takes a dataframe and a Borough name, Draws bar chart of the complaints of each agencies in the given Borough.
	'''

	print "\nPlotting %s bar chart..." %boro
	# if the user input 'NYC', the program plots the entire dataframe
	if boro == 'NYC':
		df_boro = df
	else:
		df_boro = df[df.Borough == boro]  # selects data for the given Borough

	# groups the entries by agencies
	df_groupby = df_boro[['Unique Key', 'Agency']].groupby('Agency').count() 
	
	# draws a bar plot
	df_groupby.plot(kind = 'bar', legend = False, title = 'Total number of complaints in %s' %boro)
	plt.show()
	plt.close()


def draw_agency_pie(df, agency):
	'''
	Draws pie chart of the complaints of a selected agency in each borough.
	'''
	print "\nPlotting %s bar chart..." %agency
	# selects data for the given agency
	df_agency = df[df.Agency == agency] 
	
	# groups the entries by Borough
	df_groupby = df_agency[['Unique Key', 'Borough']].groupby('Borough').count()
	
	# draws a pie plot
	df_groupby['Unique Key'].plot(kind = 'pie', autopct='%1.1f%%', figsize=(8, 8), title = 'Total number of complaints for %s in each Borough' %agency)
	plt.ylabel('')
	plt.show()
	plt.close()

