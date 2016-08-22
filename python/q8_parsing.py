## I chose to import the csv file, find the minimum difference between goals and goals allowed 
## and return the team name all in one function.  
## As the overall function is still less than 20 lines,
## I think it is OK


import csv

def find_min_diff(data):
    # COMPLETE THIS FUNCTIOn 
    min_diff = 1000
    min_diff_team = ""

    with open(data) as f:
    	reader = csv.reader(f)
    	header_line = next(reader)
 
    	for row in reader:
    		diff = abs(int(row[6]) - int(row[5])) 
 
    		if diff < min_diff:
    			min_diff = diff
    			min_diff_team = row[0]
#    		row.append(abs(int(row[6]) - int(row[5])))
#    		print row

	return min_diff_team, min_diff


