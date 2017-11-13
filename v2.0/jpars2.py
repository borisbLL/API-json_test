#! /usr/bin/python
# -*- coding: UTF-8 -*-

# Author:	Boris Battistin
# Date:		11/08/2017
# 
# Objectives:
# 
# 1) retrieve json file from url/api, save data file -> in.json
# 2) print imported data
# 3) save a parsed/formatted file -> out.json
# 4) retrieve ['name'],['abv'] list and save it to file -> selection.csv
# 5) print csv selection of data
# 6) request input abv value print out matching results 

import sys
import operator
import json
import csv
import urllib2
import io
from pprint import pprint

## import JSON string from hard-coded URL  

url = 'https://api.punkapi.com/v2/beers'

print("Fetching RAW data")

with open('in.json', 'w') as html_data:
	html_data.write(urllib2.urlopen(url).read())

with open('in.json', 'r') as infile:    
	data = json.load(infile)

raw_input("\n\nPress Enter to continue...\n\n")


## TASK 01 : print-out all imported data as JSON formatted
pprint(data)
raw_input("\n\nPress Enter to continue...\n\n")


# saves a formatted JSON output file taking care of unicode
# Make it work for Python 2+3 and with Unicode
try:
    to_unicode = unicode
except NameError:
    to_unicode = str 

with io.open('out.json', 'w', encoding='utf8') as outfile:
	jstring = json.dumps(data, indent=4, sort_keys=False, separators=(',', ': '), ensure_ascii=False)
	outfile.write(to_unicode(jstring))


## TASK 02 : print-out all name, vbs fields values using UTF-8 encoding in names
with open('selection.csv', 'wb') as file:
    csv_file = csv.writer(file)
    for item in data:
        csv_file.writerow([item['name'].encode('utf8'), item['abv']])

with open('selection.csv', 'rb') as csvfile:
	print csvfile.read()

raw_input("\n\nPress Enter to continue...\n\n")

## TASK 03 : print-out user-selected avalues of names & vbs fields
# need to fix
# input validation
# number acceptance/validation logic
# error handling 
while True:
    try:
        n = float(input("\nInsert a valid value (e.g. 10, 5.5 ...):  "))
    except ValueError:
        print("NaN! please retry")
    else:
        print("You entered: ", n)
        print("\n")
        break

#conditional check on input
for item in data:
       if (item['abv'] > n ):
        print item['name'].encode('utf8'), item['abv']
       else:
       	pass


raw_input("\n\nPress Enter to continue...\n\n")

## TASK 04 : print-out ordered list user-selected avalues of names & vbs fields
