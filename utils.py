import numpy as np
from os import listdir
from os.path import isfile, join

# structure: location number, temperature, dewpoint/temperature differential, visibility, precipitation, wind speed
# Indicators (1 = yes, 0 = no/not          
#                         reported) for the occurrence during the 
#                         day of:
#                         Fog ('F' - 1st digit).
#                         Rain or Drizzle ('R' - 2nd digit).
#                         Snow or Ice Pellets ('S' - 3rd digit).
#                         Hail ('H' - 4th digit).
#                         Thunder ('T' - 5th digit).
#                         Tornado or Funnel Cloud ('T' - 6th       
#                         digit).

def is_october(date):
	if date[1] == '10':
		return True 
	else:
		return False


def parse_date(date_string):
	date = [date_string[0:4], date_string[4:6], date_string[6:8]]
	return date


def save(date, split, all_data):
	location = int(split[0])
	temp = float(split[3])
	if temp == 9999.9:
		temp = 0.0
	dewp = float(split[4])
	if dewp == 9999.9:
		dewp = 0.0
	visibility = float(split[7])
	if visibility == 999.9 or visibility == 9999.9:
		visibility = 0.0
	wind = float(split[8])
	if wind == 999.9:
		wind = 0.0
	precip = float(split[13])
	if precip == 99.99:
		precip = 0.0
	all_data.append([location, int(date[0]), int(date[1]), int(date[2]), temp, dewp, visibility, wind, precip])
	return all_data


def cleanup(split):
	cleaned = []
	for entry in split:
		if len(entry) > 0:
			if entry != '\n':
				cleaned.append(entry)
	return np.asarray(cleaned)


def read_data():
	all_data = []
	all_files = [f for f in listdir('raw_data') if isfile(join('raw_data', f))]
	print 'reading ' + str(len(all_files)) + ' files'
	for file in all_files:
		print str(file) + '...'
		o = open('raw_data/' + file)
		curr_line = 0
		for line in o.readlines():
			if curr_line > 0: # skip the first line
				split = line.split(' ')
				if len(split) < 50:
					continue
				else:
					cleaned = cleanup(split)
					date = parse_date(cleaned[2])
					if is_october(date):
						save(date, cleaned, all_data)

			curr_line += 1
	return np.array(all_data)