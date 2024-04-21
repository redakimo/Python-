import csv
import os
contenu=[]
with open("Exo1.csv", "r", newline="") as fichier:
    reader = csv.reader(fichier,delimiter=';')
    for ligne in reader:
        contenu.append(ligne)
print(contenu)
print("******************************************************")
for ligne in contenu:
    ligne.append(float(ligne[1])+float(ligne[2]))

print(contenu)

with open("exo1-sortie.csv", "w") as fichier:
    writer = csv.writer(fichier,delimiter=';')
    for ligne in contenu:
        writer.writerow(ligne)
    os.startfile("exo1-sortie.csv")


