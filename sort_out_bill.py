import re
import csv
data_dict = [{}, {}, {}]
files = ["export_messages_usage_period_50140.csv", "export_megabytes_usage_period_50140.csv","export_minutes_usage_period_50140.csv"]

num_index = [2, 1, 4]
length_index = [3,3,11]

num_dict= {'7165254605': "Megan", '7169572733': "Katie", '7169574439': "Erin", '7169306752': "Bridget"}
	
for (index, filename) in enumerate(files):		
	with open(filename, 'rb') as f:
		file_reader = csv.reader(f)
		file_reader.next()
		for line in file_reader:
			if len(line) >= length_index[index]:
				num = line[num_index[index]]
				amt_index = [lambda:1, lambda:float(line[3]), lambda:int(line[11])]
				if num in data_dict[index]:
						data_dict[index][num] += amt_index[index]()
				else :
						data_dict[index][num] = amt_index[index]()
	for key in data_dict[index]:
		print index, num_dict[key], data_dict[index][key]
		
#Sums dictionary entries
def sum(d):
	s = 0
	for key in d:
		s += d[key]
	return s
	
tot_data = sum(data_dict[1])
tot_min = sum(data_dict[2])
tot_texts = sum(data_dict[0])

#TODO Replace having to manually input the charges with a table of the plans so we can calculate them
dcost = 24.
mcost = 9.
tcost = 14.

extra_per_line = (14.69+24.0)/4.0
print extra_per_line

for key in num_dict:
	print num_dict[key]
	print "text", (data_dict[0][key]/float(tot_texts))*tcost
	print "min", (data_dict[2][key]/float(tot_min))*mcost
	print "data", (data_dict[1][key]/float(tot_data))*dcost
	print "total", (data_dict[0][key]/float(tot_texts))*tcost + (data_dict[2][key]/float(tot_min))*mcost + (data_dict[1][key]/float(tot_data))*dcost + extra_per_line
	




		

			