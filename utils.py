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
	if date[1] == 10:
		return True 
	else:
		return False


def parse_date(date_string):
	# TODO: this is probably totally wrong
	date = [date_string[0:5], date_string[6:7], date_string[8:9]]
	return date


def save(date, split, all_data):
	# TODO: this parsing won't work -- need way more edge case handling
	location = split[0]
	temp = split[3]
	dewp = split[4]
	visibility = split[7]
	wind = split[8]
	precip = split[13]
	codes = split[15]
	all_data[location][date] = [temp, dewp, visibility, wind, precip, codes]
	return all_data


def read_data():
	all_data = # STRUCTURE
	all_files = [f for f in listdir('raw_data') if isfile(join('raw_data', f))]
	for file in all_files:
		o = open(file)
		curr_line = 0
		for line in o.readlines():
			if curr_line > 0: # skip the first line
				split = line.split(' ')
				date = parse_date(split[2])
				if is_october(date):
					save(date, split, all_data)

			curr_line += 1
	return all_data