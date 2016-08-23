##PLACE YOUR CODE HERE



import csv


# Q1 Question one..  find the list and frequency of degrees
def reg_deg(data):
    # COMPLETE THIS FUNCTIOn 
    degrees = []
    with open(data) as f:
    	reader = csv.reader(f)
    	header_line = next(reader)
    	for row in reader:
    		raw = row[1].replace('.','').split()
#    		degrees.append = row[1].gsub('\.','')
    		degrees.append(raw)
	deg = [j for i in degrees for j in i]
	degset = set(deg)
	for d in degset:
		print d, deg.count(d)
	return deg


#Q2 Question 2.. find the list and frequency of titles

def reg_ttl(data):
    # COMPLETE THIS FUNCTIOn 
    titles = []
    with open(data) as f:
    	reader = csv.reader(f)
    	header_line = next(reader)
    	for row in reader:
    		raw = row[2].replace(' of Biostatistics','')
    		raw = raw.replace(' is Biostatistics', '')
    		titles.append(raw)
	ttlset = set(titles)
	for d in ttlset:
		print d, titles.count(d)
	return titles


##Q3. Search for email addresses and put them in a list.  Print the list of email addresses.


def reg_email(data):
    emails = []
    with open(data) as f:
    	reader = csv.reader(f)
    	header_line = next(reader)
    	for row in reader:
    		emails.append(row[3])
	return emails


## Q4.  Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

import re

def reg_domain(data):
	emails = reg_email(data)
	domains = []
	find = re.compile("^(.*)@.*")
	for e in emails:
		domain = e.replace(re.match(find,e).group(1)+'@','')
		domains.append(domain)
	print len(set(domains))
	return (set(domains))



