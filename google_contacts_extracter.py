import csv
import re
import json
#contacts = "contacts.csv here"
contacts = "contacts.csv"
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