from utils import read_data
import numpy as np
import matplotlib.pyplot as plt

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
	num_years = maximum - minimum + 1
	years_days_rain = np.zeros((num_years, days_in_month)) # data structure of shape num_years x days_in_oct

	years_locs_rain_amount = np.zeros((num_years, num_locations)) # data structure of shape num_years x num_locations

	years_locs_rainy_days = np.zeros((num_years, num_locations)) # data structure of shape num_years x num_locations

	visibilities = list()
	precipitations = list()
	temperatures = list()
	dewpoint_offsets = list()

	for i in range(all_weather.shape[0]):
		datapoint = all_weather[i]
		yr = int(datapoint[year] - minimum) # adjust to use as index
		loc = int(datapoint[location])
		if datapoint[precip] > 0:
			years_days_rain[yr][loc] = 1 # at each index is either 0 (no precip) or 1 (if that day had rain in any location)
			years_locs_rainy_days[yr][loc] += 1 # increment each location when a day has rain
		years_locs_rain_amount[yr][loc] += datapoint[precip] # increment each location with precip amount
		if datapoint[visibility] > 0:
			visibilities.append(datapoint[visibility])
		precipitations.append(datapoint[precip])
		temperatures.append(datapoint[temp])
		dewpoint_offsets.append(datapoint[temp] - datapoint[dewp])

	print 'number of days it rained somewhere in the Outback, on average by year'
	"""years = list()
	rainy_days = list()"""
	for i in range(0, years_days_rain.shape[0]):
		entry = years_days_rain[i]
		print minimum + i, len(np.nonzero(entry)[0]), '\n'
		"""years.append(minimum + i)
		rainy_days.append(len(np.nonzero(entry)[0]))
	plt.bar(np.arange(len(years)), rainy_days)
	plt.xticks(np.arange(len(years)), years)
	plt.title('number of days it rained somewhere in the Outback')
	plt.show()"""

	print 'days in which it rained somewhere in the Outback'
	for i in range(0, years_days_rain.shape[0]):
		print minimum + i, years_days_rain[i], '\n'
		"""plt.bar(np.arange(len(years_days_rain[i])), years_days_rain[i])
		plt.title('days it rained somewhere in the Outback in ' + str(minimum + i))
		plt.show()"""

	print 'inches of rain in October, by year and location'
	for i in range(0, years_locs_rain_amount.shape[0]):
		print minimum + i, years_locs_rain_amount[i], '\n'
		"""plt.bar(np.arange(len(years_locs_rain_amount[i])), years_locs_rain_amount[i])
		plt.title('inches of rain by location in ' + str(minimum + i))
		plt.show()"""


	print 'number of rainy days, by location'
	for i in range(0, years_locs_rainy_days.shape[0]):
		entry = years_locs_rainy_days[i]
		print minimum + i, entry, '\n'
		plt.bar(np.arange(len(years_locs_rainy_days[i])), years_locs_rainy_days[i])
		plt.title('number of rainy days by location in ' + str(minimum + i))
		plt.show()


	print 'average visibility'
	print sum(visibilities)/len(visibilities)

	print 'average amount of rain'
	print sum(precipitations)/len(precipitations)

	print 'average temperature'
	print sum(temperatures)/len(temperatures)

	print 'average difference between dewpoint and temperature'
	print sum(dewpoint_offsets)/len(dewpoint_offsets)


all_weather = read_data()
minimum = 2020.0
maximum = 0.0
for elem in all_weather:
	if elem[year] < minimum:
		minimum = elem[year]
	if elem[year] > maximum:
		maximum = elem[year]
report_basic_stats(all_weather, int(minimum), int(maximum))