
# encoding: utf-8
# Copyright (c) 2017 Mahdi bahri
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import csv
import re
import json
contacts = "contacts.csv" # google contacts csv here exemple : contacts.csv

csvfile = open(contacts, 'r')
#get emails by columns : "E-mail Address" , "E-mail 2 Address" and "E-mail 3 Address"
columns = ("E-mail Address","E-mail 2 Address","E-mail 3 Address")
#read csv
csv = csv.DictReader( csvfile, columns)
id = 0
lists = []
for i in csv:
	id= id+1
	for d in i:
		try:
			lists.append(i[d][11])
		except :
			pass
ds=[]
for a in lists:
	#check email format
	EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
	if  EMAIL_REGEX.match(a):
		ds.append(a)
#write to output file as json
with open('contact.json','a')as fs:
		json.dump(ds, fs)
