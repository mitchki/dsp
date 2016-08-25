
import csv

## input faculty file, return set of unique last names

ifile = 'faculty.csv'

def lnames(data):
    lastnames = []
    with open(data) as f:
    	reader = csv.reader(f)
    	header_line = next(reader)
    	for row in reader:
    		fullname = row[0]
    		lastname = fullname.split()[-1]
    		lastnames.append(lastname)
	f.close()
	unique_lastnames = list(set(lastnames))
	return unique_lastnames


def make_dict(ifile):
	lastnames = lnames(ifile)
	dnames = {}
	for name in lastnames:

	    with open(ifile) as f:
	    	who_list = []
	    	f.seek(0)
	    	reader = csv.reader(f)
	    	header_line = next(reader)
	    	who_list = []
	    	for row in reader:
	    		fullname = row[0]
	    		lastname = fullname.split()[-1]
	    		#title = ""
	    		if name == lastname:
	    			title = row[2].replace(" of Biostatistics", "")
	    			#who_list.append(row[1:3])
	    			who_list.append([row[1],title,row[3]])
	    			dnames[name] = who_list
#	    			print name, who_list
	return dnames

## below to test program
print lnames(ifile)
print '-' * 50
print make_dict(ifile)

print '-' * 50

## get first 3 entries in the dictionary
dict = make_dict(ifile)
count = 0
for key in dict:
    if count < 3:
        print "{'"+key+"':", dict[key],"}"
    count += 1











