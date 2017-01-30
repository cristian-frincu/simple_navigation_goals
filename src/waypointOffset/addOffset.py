import csv

f= open('offset.csv','w')
with open('file.csv','rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:
		for index in row:
			if index != row[-1]:
				f.write(str( float(index)+100)+",")
			else:
				f.write(str("1.0"))
		f.write("\n")
