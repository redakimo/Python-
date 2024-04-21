import csv
with open('data.csv', 'r') as f:
    stag = csv.reader(f , delimiter=',')
    print("Liste des noms : ")
    for row in stag:
        print (row[2])
# Cela affiche la liste des noms de la table.