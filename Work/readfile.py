with open('Data/portfolio.csv','rt') as f:
  data = f.read()
data
print(data)

#line by line
with open('Data/portfolio.csv','rt') as f:
  for line in f:
    print(line, end='')

#skip a line
f = open('Data/portfolio.csv','rt')
headers = next(f)
headers

for line in f:
  print(line, end='')

f.close()

#split a line
f = open('data/portfolio.csv','rt')
headers = next(f).split(',')
headers

for line in f:
  row = line.split(',')
  print(row)

f.close()
