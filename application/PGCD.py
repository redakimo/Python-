nombre1 = int(input("Entrez le premier entier naturel : "))
nombre2 = int(input("Entrez le deuxième entier naturel : "))

# Vérifier si les nombres sont positifs
if nombre1 < 0 or nombre2 < 0:
    print("Veuillez entrer des entiers naturels positifs.")
else:
    while nombre2 != 0:
        temp = nombre2
        nombre2 = nombre1 % nombre2
        nombre1 = temp

    pgcd = nombre1

    print(f"Le PGCD des deux nombres est : {pgcd}")
