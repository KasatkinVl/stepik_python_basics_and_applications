import csv
from collections import Counter as c

with open('Crimes.csv') as f:
    data = csv.reader(f)
    print(c(row[5] for row in data if '2015' in row[2]))

with open('Crimes.csv') as f:
  result = c(row[5] for row in csv.reader(f) if '2015' in row[2])
  print(result.most_common(1))