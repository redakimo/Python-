#coding:utf-8

# Lecture des données d'entrée
NbreKm = float(input("Entrez le nombre total de kilomètres : "))
Nbre_jrs = int(input("Entrez le nombre de jours de location : "))
t1 = float(input("Entrez le tarif pour les 100 premiers kilomètres : "))
t2 = float(input("Entrez le tarif pour les kilomètres de 101 à 1000 : "))
t3 = float(input("Entrez le tarif au-delà de 1000 kilomètres : "))
t4 = float(input("Entrez le tarif journalier pour le forfait illimité : "))
assur_jr = float(input("Entrez le montant de l'assurance comptabilisée par jour : "))

    # Calcul du coût de la location pour un forfait au kilomètre
if NbreKm <= 100:
    cout_km = NbreKm * t1
elif NbreKm <= 1000:
    cout_km = 100 * t1 + (NbreKm - 100) * t2
else:
    cout_km = 100 * t1 + 900 * t2 + (NbreKm - 1000) * t3

    # Calcul du coût de la location pour un forfait journalier
total_journalier = Nbre_jrs * t4 + assur_jr * Nbre_jrs

    # Affichage des coûts
print("Coût de la location pour un forfait au kilomètre : ", cout_km)
print("Coût de la location pour un forfait journalier : ", total_journalier)

# Comparaison des forfaits et affichage du plus avantageux
if cout_km < total_journalier:
    print("Le forfait au kilomètre est plus avantageux.")
elif cout_km > total_journalier:
    print("Le forfait journalier est plus avantageux.")
else:
    print("Les deux forfaits ont le même coût.")



