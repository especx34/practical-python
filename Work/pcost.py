# pcost.py
#
# Exercise 1.27

pcost = 0
with open('Data/portfolio.csv','rt') as f:
	for line in f:
		row = line.split(',')
		pcost += int(row[1]) * float(row[2])

print(pcost)
