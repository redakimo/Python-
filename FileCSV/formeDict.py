import csv
with open('data.csv', 'r') as f:
    reader = csv.DictReader(f , delimiter=',')
    for row in reader:
        print (row)