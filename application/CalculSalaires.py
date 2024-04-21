
# Entrées
heures_travaillees = float(input("Entrez le nombre d'heures travaillées par semaine : "))
enfants = int(input("Entrez le nombre d'enfants : "))

# Constantes

salaire_horaire = 50
salaire_max_IR = 7000
cotisation_syndicale = 15

# Calcul du salaire brut
salaire_brut = salaire_horaire * heures_travaillees*4

# Calcul de la mutuelle en fonction du nombre d'enfants
if enfants > 0:
    mutuelle = 0.05 * salaire_brut
else:
    mutuelle = 0.03 * salaire_brut

# Calcul de la retraite
retraite = 0.06 * salaire_brut

# Calcul de l'Impôt sur le Revenu (IR)
if salaire_brut <= salaire_max_IR:
    IR = 0.3 * salaire_brut
else:
    IR = 0.38 * salaire_brut

# Calcul du salaire net
salaire_net = salaire_brut - mutuelle - retraite - IR - cotisation_syndicale

# Affichage des résultats
print("Salaire brut :", salaire_brut, "DH")
print("Mutuelle :", mutuelle, "DH")
print("Retraite :", retraite, "DH")
print("Impôt sur le Revenu (IR) :", IR, "DH")
print("Salaire net :", salaire_net, "DH")
