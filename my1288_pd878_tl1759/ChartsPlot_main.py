# Name: 	plots_main.py
# Author: 	Pan Ding
# Date: 	May 08, 2015
# Summary:	The main program, which does three things
#			1) It loads the csv file into a dataframe and cleans the data.
#			2) Then it asks the user to input a Borough name, and plots the volume of complaints for each agency in this Borough. It stops until the user enters 'finish'.
#			3) Then it asks the user to input an agency name, and plots the volume of complaints for this agency in each Borough. It stops until the user enters 'finish'.
########################################################################################## 

import pandas as pd
import matplotlib.pyplot as plt

import UserInput_Charts as ui
import Plot_Charts as dp
import load_clean_data as lcd


def load_dataset():
	#### Loads and cleans data####
	df = lcd.dataframe().load_csv() 
	return df


def RunChartModule(df):

	# #### Loads and cleans data####
	df_clean = lcd.clean_df(df)

	#### Draws bar plots for given Boroughs ####
	boroughs = list(df.Borough.unique())
	boroughs.remove('Unspecified')
	boroughs.append('NYC')
	while True:
		# gets input from user
		boro = ui.get_borough(boroughs) 
		if boro == 'FINISH':
			# exit the interactiove mode
			break
		else:
			dp.draw_boro_bar(df, boro)

	#### Draws pie plots for given agencies ####
	agencies = list(df.Agency.unique())
	while True:
		# gets the input from user
		print "Select an agency for which you would like to view a complaint distribution on a Pie Chart."
		agency = ui.get_agency(agencies) 
		if agency =="FINISH":
			# exit the interactiove mode
			break
		else:
			dp.draw_agency_pie(df, agency)




