#coding:utf-8
nbrecolis=int(input("Entrer le nombre de colis :"))
# Entrées
total_final=0
for i in range(nbrecolis):
    taxe_base = 100
    surtaxe_poids = 0
    surtaxe_dimensions = 0
    total_avant_surtaxe = 0
    total_coli = 0
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(f"Introduit les données du coli numero {i+1}:")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    largeur = float(input("Entrez la largeur du colis en mètres : "))
    hauteur = float(input("Entrez la hauteur du colis en mètres : "))
    longueur = float(input("Entrez la longueur du colis en mètres : "))
    poids = float(input("Entrez le poids du colis en kilogrammes : "))
    distance = float(input("Entrez la distance à parcourir en kilomètres : "))

    if poids > 50:
        surtaxe_poids = (poids - 50) * 20
    else:
        surtaxe_poids = 0

    if max(largeur, hauteur, longueur) > 1:
        surtaxe_dimensions = 30
    else:
        surtaxe_dimensions = 0

    total_avant_surtaxe = taxe_base + surtaxe_poids + surtaxe_dimensions

    if distance > 100:
        surtaxe_distance = 0.15 * total_avant_surtaxe
    else:
        surtaxe_distance = 0

    total_coli = total_avant_surtaxe + surtaxe_distance


    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(f"La totale de la coli num {i+1} est de {total_coli}")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


    total_final = total_final+total_coli

print("Le coût total du transport est de", total_final, "DH")
