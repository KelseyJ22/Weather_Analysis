from utils import read_data
import numpy as np

year = 0
month = 1
day = 2
location = 3
temp = 4
dewp = 5
visibility = 6
wind = 7
precip = 8
codes = 9

def report_basic_stats(all_weather):
	print all_weather.shape
	# number of days it rains, on average
	# inches of rain in October, on average
	# rainiest year by days and by amount
	# number of days with low visibility
	# average visibility
	print np.mean(all_weather, axis=visibility)
	# average amount of rain
	print np.mean(all_weather, axis=precip)
	# average temperature
	print np.mean(all_weather, axis=temp)
	# rainiest weather station, on average


all_weather = read_data()
report_basic_stats(all_weather)