import csv

import pandas

data = [['ID', 'Nom', 'Age', 'Taille'] ,
['1', 'Walid', '19', '180'],
['2', 'Najib', '30', '185'],
['3', 'Majda', '27', '175']]
with open('data1.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',')
# write data
    for ligne in data:
        writer.writerow(ligne)
result = pandas.read_csv('data.csv')
print(result)