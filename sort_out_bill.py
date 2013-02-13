import re
import csv
text_file = ("export_messages_usage_period_50140.csv")
data_file = ("export_megabytes_usage_period_50140.csv")
minutes_file = ("export_minutes_usage_period_50140.csv")
min_dict = {}
text_dict = {}
data_dict = {}
num_dict= {'7165254605': "Megan", '7169572733': "Katie", '7169574439': "Erin", '7169306752': "Bridget"}
with open(minutes_file) as minutes:
	minutes_reader = csv.reader(minutes)
	minutes_reader.next()
	for line in minutes_reader:
		if len(line) >= 11:
			num = line[4]
			if line[4] in min_dict:
				min_dict[num] += int(line[11])
			else :
				min_dict[num] = int(line[11])
for key in min_dict:
	print num_dict[key], min_dict[key]
	
with open(text_file) as texts:
	text_reader = csv.reader(texts)
	text_reader.next()
	for line in text_reader:
		if len(line) >= 3:
			num = line[2]
			if num in text_dict:
				text_dict[num] += 1
			else :
				text_dict[num] = 1
for key in text_dict:
	print num_dict[key], text_dict[key]
	
with open(data_file, 'rb') as data:
	data_reader = csv.reader(data)
	data_reader.next()
	for line in data_reader:
		if len(line) >= 4:
			num = line[1]
			if num in data_dict:
				data_dict[num] += int(line[3])
			else :
				data_dict[num] = int(line[3])
for key in data_dict:
	print num_dict[key], data_dict[key]


def sum(d):
	s = 0
	for key in d:
		s += d[key]
	return s
	
tot_data = sum(data_dict)
tot_min = sum(min_dict)
tot_texts = sum(text_dict)

dcost = 24.
mcost = 9.
tcost = 14.

extra_per_line = (11.61+24.0+14.69)/4.0
print extra_per_line
print 6.+14.69/4.0

for key in num_dict:
	print num_dict[key]
	print "text", (text_dict[key]/float(sum(text_dict)))*tcost
	print "min", (min_dict[key]/float(sum(min_dict)))*mcost
	print "data", (data_dict[key]/float(sum(data_dict)))*dcost
	print "total", (text_dict[key]/float(sum(text_dict)))*tcost+ (min_dict[key]/float(sum(min_dict)))*mcost+(data_dict[key]/float(sum(data_dict)))*dcost+extra_per_line
	




		

			