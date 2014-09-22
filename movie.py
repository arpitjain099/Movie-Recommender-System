import csv

with open('u.item','rb') as f:
    reader=csv.reader(f,delimiter='|')
    for row in reader:
        print row
