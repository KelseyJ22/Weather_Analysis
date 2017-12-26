from utils import read_data
import numpy as np

location = 0
year = 1
month = 2
day = 3
temp = 4
dewp = 5
visibility = 6
wind = 7
precip = 8
days_in_month = 31
num_locations = 11


def report_basic_stats(all_weather, minimum, maximum):
	# number of days it rains, on average
	num_years = maximum - minimum + 1
	years_days_rain = np.zeros((num_years, days_in_month)) # data structure of shape num_years x days_in_oct

	# inches of rain in October, on average
	years_locs_rain_amount = np.zeros((num_years, num_locations)) # data structure of shape num_years x num_locations

	# rainiest year by number of days
	# data structure of shape num_years x num_locations
	years_locs_rainy_days = np.zeros((num_years, num_locations)) # data structure of shape num_years x num_locations

	# number of days with low visibility
	# data structure of shape num_years x num_locations
	#years_locs_visibility = np.zeros((maximum - minimum, num_locations)) # data structure of shape num_years x num_locations

	for i in range(all_weather.shape[0]):
		datapoint = all_weather[i]
		yr = int(datapoint[year] - minimum) # adjust to use as index
		loc = int(datapoint[location])
		if datapoint[precip] != 0:
			years_days_rain[yr][loc] = 1 # at each index is either 0 (no precip) or 1 (if that day had rain in any location)
			years_locs_rain_amount[yr][loc] += 1 # increment each location when a day has rain
		years_locs_rainy_days[yr][loc] += datapoint[precip] # increment each location with precip amount
	#	years_locs_visibility[yr][loc] += datapoint[visibility] # increment each location when a day has low visibility

	# average visibility
	print np.mean(all_weather, axis=visibility)

	# average amount of rain
	print np.mean(all_weather, axis=precip)

	# average temperature
	print np.mean(all_weather, axis=temp)
	# rainiest weather station, on average


all_weather = read_data()
minimum = 2020.0
maximum = 0.0
for elem in all_weather:
	if elem[year] < minimum:
		minimum = elem[year]
	if elem[year] > maximum:
		maximum = elem[year]
report_basic_stats(all_weather, int(minimum), int(maximum))