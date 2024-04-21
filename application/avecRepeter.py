#coding:utf-8
# Définition de la fonction factorielle
"""
def factorielle(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

# Calcul de S1
n = int(input("Entrez la valeur de n pour S1 : "))
s1 = 0
i = 1
répéter:
    s1 += 3 * i
    i += 1
jusqu'à ce que i > n

print("S1 =", s1)

# Calcul de S2
n = int(input("Entrez la valeur de n pour S2 : "))
s2 = 0
i = 1
répéter:
    s2 += 2 * i
    i += 1
jusqu'à ce que i > n

print("S2 =", s2)

# Calcul de S3
n = int(input("Entrez la valeur de n pour S3 : "))
s3 = 0
i = 1
répéter:
    s3 += factorielle(i)
    i += 1
jusqu'à ce que i > n

print("S3 =", s3)

# Calcul de S4
n = int(input("Entrez la valeur de n pour S4 : "))
s4 = 0
i = 1
répéter:
    s4 += 1 / factorielle(i)
    i += 1
jusqu'à ce que i > n

print("S4 =", s4)
"""