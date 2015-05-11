####################################################################################################
#
#
#	Author : Liwen Tian (tl1759)
#	DS GA 1007
#	Final Project
#
#	This is the module that contains different methods of cleaning data.
#	It matched the longitudes and latitudes in the complaint data to the shapefiles in order to plot the number of complaints for a selected agency
#	It also matches the zipcodes to boroughs
#	Source: CUSP Urban Informatics Fall 2014
#
####################################################################################################


# This function reads in the file zips_borough.csv
# Stores all the zipcodes in a dictionary with the borough names as the keys
def getzipBorough(zipdata):
	""""this is the method to get zipdata"""
	zipBorough = {}
	for i in range(len(zipdata)):
			zipBorough[zipdata['Incident Zip'][i]]= zipdata['Borough'][i]
	return zipBorough


def getmapPoints(complaintsdata):
	"""get mapPoints for top agency for each zipCode"""
	agencyDict = {};complaintsPerZip = {};mapPoints = {};lat = [];lng = []
	for i in range(len(complaintsdata)):
			try:
				lat.append(float(complaintsdata['Latitude'][i]))
				lng.append(float(complaintsdata['Longitude'][i]))
				# List of agnecies
				agency = complaintsdata['Agency'][i] 
				# List of zipcodes
				zipCode = complaintsdata['Incident Zip'][i]

				if not agency in agencyDict:
					# agency as key and values is the leghth of the dictionary
					agencyDict[agency] = len(agencyDict)
				# zipcode as a key 
				if zipCode in complaintsPerZip:
					# value is also a dictionary{agency:number}
					if agency in complaintsPerZip[zipCode]: 
						complaintsPerZip[zipCode][agency] += 1
					else:
						complaintsPerZip[zipCode][agency] = 1

				else:
					complaintsPerZip[zipCode] = {}
					complaintsPerZip[zipCode][agency] = 1

			except:
				pass
	mapPoints = {'zip_complaints':complaintsPerZip}
	return mapPoints


# Counts the number of complaints for each selected agency 
# Prepares these as points on a map to plot 
def getagencymapPoints(data,agency1,agency2):
	"""get two agenies mapPoints"""
	complaintsPerZip = {};lat = [];lng = [];
	for i in range(len(data)):
		try:
			lat.append(float(data['Latitude'][i]))
			lng.append(float(data['Longitude'][i]))
			# List of agnecies
			agency = data['Agency'][i] 
			zipCode = data['Incident Zip'][i]

			# This counts the number of complaints in the selected agencies and stores them in a dictionary to be plotted
			if zipCode in complaintsPerZip:
				# Checks for the first agency
				if agency == agency1:
					if agency in complaintsPerZip[zipCode]:
						complaintsPerZip[zipCode][agency]+=1
					else:
						complaintsPerZip[zipCode][agency] = 1
				# Checks for the second agency
				elif agency == agency2:
					if agency in complaintsPerZip[zipCode]:
						complaintsPerZip[zipCode][agency]+=1
					else:
						complaintsPerZip[zipCode][agency] = 1
				else:
					pass
			else:
				complaintsPerZip[zipCode]={agency1:0,agency2:0}
		except:
			pass
	agencymapPoints = {'zip_complaints':complaintsPerZip}
	return agencymapPoints


# This is the method that get number of complaints  for each zipcodes
def getzipmapPoints(complaintsdata):
	
	complaintsPerZip = {}
	lat = []
	lng = []
	for i in range(len(complaintsdata)):
		try:
			# Append the Lat Lng as tuples in a list
			lat.append(float(complaintsdata['Latitude'][i]))
			lng.append(float(complaintsdata['Longitude'][i]))
			# List of agencies
			agency = complaintsdata['Agency'][i] 
			# List of zipcodes
			zipCode = complaintsdata['Incident Zip'][i]
			if zipCode in complaintsPerZip:
				complaintsPerZip[zipCode]+=1
			else:
				complaintsPerZip[zipCode]=1

		except:
			pass
	zipmapPoints = {'zip_complaints':complaintsPerZip}
	return zipmapPoints