
import csv

## Question Q6
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

## Q6: Create a dictionary in the below format
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
#print lnames(ifile)
#print '-' * 50
print make_dict(ifile)

print '-' * 50

## get first 3 entries in the dictionary
dict = make_dict(ifile)
count = 0
for key in dict:
    if count < 3:
        print "{'"+key+"':", dict[key],"}"
    count += 1




## Q7 Usekeys of 


import csv
## Q7. The previous dictionary does not have the best design for keys. Create a new dictionary with keys as:
def keys(data):
    flnames = []
    with open(data) as f:
        reader = csv.reader(f)
        header_line = next(reader)
        for row in reader:
            fullname = row[0]
            lastname = fullname.split()[-1]
            firstname = fullname.split()[0]
            flnames.append(tuple([firstname,lastname]))
    f.close()
    unique_flnames = list(set(flnames))
    return unique_flnames



def make_dict7(ifile):
    namekeys = keys(ifile)
    dnames = {}
    for name in namekeys:

        with open(ifile) as f:
            who_list = []
            f.seek(0)
            reader = csv.reader(f)
            header_line = next(reader)
            for row in reader:
                fullname = row[0]
                lastname = fullname.split()[-1]
                firstname = fullname.split()[0]
                
                if (name[0] == firstname) and (name[1] == lastname):
                    title = row[2].replace(" of Biostatistics", "")
                    who_list = [row[1],title,row[3]]
                    dnames[name] = who_list
    return dnames


import csv
from collections import OrderedDict

## Q8. The previous dictionary does not have the best design for keys. Create a new dictionary with keys as:
def sortedkeys(data):
    flnames = []
    with open(data) as f:
        reader = csv.reader(f)
        header_line = next(reader)
        for row in reader:
            fullname = row[0]
            lastname = fullname.split()[-1]
            firstname = fullname.split()[0]
            flnames.append(tuple([firstname,lastname]))
    f.close()
    #unique_flnames = list(set(flnames))
    flnames = sorted(flnames, key=lambda x: x[1])
    return flnames



def make_dict8(ifile):
    namekeys = sortedkeys(ifile)
    #dnames = {}
    dnames = OrderedDict({})
    for name in namekeys:

        with open(ifile) as f:
            who_list = []
            f.seek(0)
            reader = csv.reader(f)
            header_line = next(reader)
            for row in reader:
                fullname = row[0]
                lastname = fullname.split()[-1]
                firstname = fullname.split()[0]
                
                if (name[0] == firstname) and (name[1] == lastname):
                    title = row[2].replace(" of Biostatistics", "")
                    who_list = [row[1],title,row[3]]
                    dnames[name] = who_list
    return dnames

## Print out the dictionary key value pairs based on alphabetical orders of the last name of the profess

resp = make_dict8('faculty.csv')

print resp 


## Print out the first 3 entries in the sorted dictionary


print resp.popitem(last=False)
print resp.popitem(last=False)
print resp.popitem(last=False)



## Sorted dictionary collections:OrderedDict
## http://stackoverflow.com/questions/15711755/converting-dict-to-ordereddict
## 












