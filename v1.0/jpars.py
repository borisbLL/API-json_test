#! /usr/bin/python
# -*- coding: UTF-8 -*-

import json
import csv
import urllib2
from pprint import pprint

# Make it work for Python 2+3 and with Unicode
import io
try:
    to_unicode = unicode
except NameError:
	to_unicode = str 

## import JSON string from hard-coded URL  

url = 'https://api.punkapi.com/v2/beers'

with open('in.json', 'w') as html_data:
	html_data.write(urllib2.urlopen(url).read())

with open('in.json', 'r') as data_file:    
	data = json.load(data_file)

## TASK 01 : print-out all imported data as JSON formatted
pprint(data)

## --------------------------------------------------------------------------------
## https://docs.python.org/3/howto/unicode.html
## --------------------------------------------------------------------------------
# new_f = codecs.StreamRecoder(f,
#     # en/decoder: used by read() to encode its results and by write() to decode its input.
#     codecs.getencoder('utf-8'), codecs.getdecoder('utf-8'),
# 
#     # reader/writer: used to read and write to the stream.
#     codecs.getreader('ascii'), codecs.getwriter('ascii') )
# # --------------------------------------------------------------------------------
# with open(fname, 'r', encoding="ascii", errors="surrogateescape") as f:
#     data = f.read()
# 
# # make changes to the string 'data'
# 
# with open(fname + '.new', 'w',
#           encoding="ascii", errors="surrogateescape") as f:
#     f.write(data)
# # --------------------------------------------------------------------------------

# create object .load from json object-like string file

# with open('in.json', 'r') as data_file:    
# 	data = json.load(data_file)
# 
# ## TASK 01 print all imported data
# pprint(data)

'''
# json loads -> returns an object from a string representing a json object.
# json dumps -> returns a string representing a json object from an object.
# load and dump -> read/write from/to file instead of string


with io.open('out.json', 'w', encoding='utf8') as outfile:
	jstring = json.dumps(data, indent=4, sort_keys=False, separators=(',', ': '), ensure_ascii=False)
	outfile.write(to_unicode(jstring))


for item in data:
	print item['name'], item['abv']

with open("out.csv", "wb") as file:
    csv_file = csv.writer(file)
    for item in data:
        csv_file.writerow([item['name'], item['abv']])



'''
# for item in data:
# 	if data.item['abv'] > '5'
# 	print item['name'], item['abv']
# '''	
# ttstring = json.load(data, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
# pprint(to_unicode(ttstring))
# 
