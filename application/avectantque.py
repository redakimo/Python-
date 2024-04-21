#coding:utf-8
# Calcul de S1
n = int(input("Entrez la valeur de n pour S1 : "))
s1 = 0
i = 1
while i <= n:
    s1 += 3 * i
    i += 1

print("S1 =", s1)

# Calcul de S2
n = int(input("Entrez la valeur de n pour S2 : "))
s2 = 0
i = 1
while i <= n:
    s2 += 2 * i
    i += 1

print("S2 =", s2)

# Calcul de S3
n = int(input("Entrez la valeur de n pour S3 : "))
s3 = 0
fact = 1
i = 1
while i <= n:
    fact *= i
    s3 += fact
    i += 1

print("S3 =", s3)

# Calcul de S4
n = int(input("Entrez la valeur de n pour S4 : "))
s4 = 0
fact = 1
i = 1
while i <= n:
    fact *= i
    s4 += 1 / fact
    i += 1

print("S4 =", s4)
