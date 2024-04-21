#coding:utf-8
# Calcul de S1
n = int(input("Entrez la valeur de n pour S1 : "))
s1 = 0
for i in range(1, n + 1):
    s1 += 3 * i

print("S1 =", s1)

# Calcul de S2
n = int(input("Entrez la valeur de n pour S2 : "))
s2 = 0
for i in range(1, n + 1):
    s2 += 2 * i

print("S2 =", s2)

# Calcul de S3
n = int(input("Entrez la valeur de n pour S3 : "))
s3 = 0
fact = 1
for i in range(1, n + 1):
    fact *= i
    s3 += fact

print("S3 =", s3)

# Calcul de S4
n = int(input("Entrez la valeur de n pour S4 : "))
s4 = 0
fact = 1
for i in range(1, n + 1):
    fact *= i
    s4 += 1 / fact

print("S4 =", s4)
