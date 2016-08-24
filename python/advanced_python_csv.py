#PLACE YOUR CODE HERE


import csv

def reg_email(data):
    emails = []
    with open(data) as f:
    	reader = csv.reader(f)
    	header_line = next(reader)
    	for row in reader:
    		emails.append(row[3])
	f.close()
	return emails

def email_csv(ifil,ofil):
	#emails.csv
	e = reg_email(ifil)
	#	print type(e)
	ofile  = open(ofil, "w")

	writer = csv.writer(ofile, delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	for row in e:
	#	print row
		writer.writerow([row])

	ofile.close()
	#	print 'done'

