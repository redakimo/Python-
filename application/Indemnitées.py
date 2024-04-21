# coding:utf-8
def calculer_indemnite(salaire, etat_matrimonial, nombre_enfants):
    if etat_matrimonial == "célibataire":
        indemnite = salaire / 2 * 0.45
    else:
        if nombre_enfants > 3:
            indemnite = salaire * 0.75
        else:
            indemnite = salaire * 0.6
    return indemnite


salaire = float(input("Entrez le salaire de l'employé : "))
etat_matrimonial = input("Entrez l'état matrimonial de l'employé (célibataire/marié) : ").lower()
if etat_matrimonial == "marié":
    nombre_enfants = int(input("Entrez le nombre d'enfants de l'employé : "))
else:
    nombre_enfants = 0

indemnite = calculer_indemnite(salaire, etat_matrimonial, nombre_enfants)
print("L'indemnité de l'employé est de :", indemnite)
