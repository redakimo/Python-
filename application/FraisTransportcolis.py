#coding:utf-8
# Entrées
largeur = float(input("Entrez la largeur du colis en mètres : "))
hauteur = float(input("Entrez la hauteur du colis en mètres : "))
longueur = float(input("Entrez la longueur du colis en mètres : "))
poids = float(input("Entrez le poids du colis en kilogrammes : "))
distance = float(input("Entrez la distance à parcourir en kilomètres : "))

taxe_base = 100
if poids > 50:
    surtaxe_poids = (poids - 50) * 20
else:
    surtaxe_poids = 0

if largeur>1 or hauteur>1 or longueur > 1:
    surtaxe_dimensions = 30
else:
    surtaxe_dimensions = 0

total_avant_surtaxe = taxe_base + surtaxe_poids + surtaxe_dimensions

if distance > 100:
    surtaxe_distance = 0.15 * total_avant_surtaxe
else:
    surtaxe_distance = 0

total_final = total_avant_surtaxe + surtaxe_distance

print("Le coût total du transport est de", total_final, "DH")
