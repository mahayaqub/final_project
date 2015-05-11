##############################################################
#
#
#	Author : Maha Yaqub (my1288)
#	DS GA 1007
#	Final Project
#
#	This file will check if all the modules are present in the package for the program to run properly
#
#
##############################################################

import unittest
import os
import pandas as pd

class testForModules(unittest.TestCase):

	def testCompletePackage(self):

		# Check for all the files needed in the Python Package
		self.assertTrue(os.path.exists('AgencySeparation.py'))
		self.assertTrue(os.path.exists('BoroughSeparation.py'))
		self.assertTrue(os.path.exists('ChartsPlot_main.py'))
		self.assertTrue(os.path.exists('cleanup_MapData.py'))
		self.assertTrue(os.path.exists('load_clean_data.py'))
		self.assertTrue(os.path.exists('__init__.py'))
		self.assertTrue(os.path.exists('Main.py'))
		self.assertTrue(os.path.exists('mapModule.py'))
		self.assertTrue(os.path.exists('Plot_Charts.py'))
		self.assertTrue(os.path.exists('Plot_TimeSeries.py'))
		self.assertTrue(os.path.exists('Plot_Maps.py'))
		self.assertTrue(os.path.exists('prompt.py'))
		self.assertTrue(os.path.exists('start_function.py'))
		self.assertTrue(os.path.exists('TimeInterval.py'))
		self.assertTrue(os.path.exists('UserInput_Charts.py'))
		self.assertTrue(os.path.exists('UserInput_Maps.py'))
		self.assertTrue(os.path.exists('UserInput_Time.py'))
		self.assertTrue(os.path.exists('TimeSeries_Main.py'))

if __name__ == '__main__':
	unittest.main()

