#coding:utf-8

decimal_number = int(input("Entrez un nombre entier positif décimal : "))

# Vérifier si le nombre est positif
if decimal_number < 0:
    print("Veuillez entrer un nombre entier positif.")
else:
    binary_result = ""

    # Algorithme de conversion en binaire
    while decimal_number > 0:
        binary_result = str(decimal_number % 2) + binary_result
        decimal_number = decimal_number // 2

    # Afficher le résultat à l'écran
    print(f"Le nombre binaire équivalent est : {binary_result}")
