import csv
with open('data.csv', 'r') as f:
    stag = csv.DictReader(f , delimiter=',')
    for row in stag:
        print (row)