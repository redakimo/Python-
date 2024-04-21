import csv
#importer la bibliothèque csv
bonCommande =[
    {"produit":"cahier ", "reference":"F452CP", "quantite":41, "prixUnitaire":1.4},
    {"produit":"stylo bleu", "reference":"D857BL", "quantite":18, "prixUnitaire":0.95},
    {"produit":"stylo noir", "reference":"D857NO", "quantite":18, "prixUnitaire":0.95},
    {"produit":"équerre ", "reference":"GF955K", "quantite":4, "prixUnitaire":2},
    {"produit":"compas ", "reference":"RT42AX", "quantite":13, "prixUnitaire":5.25}
    ] #déclarer des dictionnaires

fichier = open("boncommande.csv", "w") #ouvrir un fichier en écrire
ecrivainCSV = csv.DictWriter(fichier,delimiter=";",fieldnames=bonCommande[0].keys()) #produire des lignes de sortie depuis les dictionnaires,
#fieldnames contient les clés des dictionnaires
ecrivainCSV.writeheader()# écrire la ligne d'en tête avec le titre des colonnes
for ligne in bonCommande : # parcourir les dictionnaires
    ecrivainCSV.writerow(ligne) #Ecrire une ligne dans le fichier
fichier.close