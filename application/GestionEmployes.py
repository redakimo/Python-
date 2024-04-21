import struct
import os

# Définition de la structure Employe
employe_format = "i 49s i f"
employe_size = struct.calcsize(employe_format)


def SaisiEcrireEmploye(f):
    numeroMatricule = int(input("Numéro de matricule : "))
    nom = input("Nom : ")
    anneeEmbauche = int(input("Année d'embauche : "))
    salaire = float(input("Salaire : "))

    employe = struct.pack(employe_format, numeroMatricule, nom.encode("utf-8"), anneeEmbauche, salaire)
    f.write(employe)
    print("Employé enregistré avec succès.")


def afficheEmploye(f):
    f.seek(0)
    while True:
        employe_data = f.read(employe_size)
        if not employe_data:
            break
        numeroMatricule, nom, anneeEmbauche, salaire = struct.unpack(employe_format, employe_data)
        print(f"Numéro de matricule: {numeroMatricule}")
        print(f"Nom: {nom.decode('utf-8').rstrip('\x00')}")
        print(f"Année d'embauche: {anneeEmbauche}")
        print(f"Salaire: {salaire:.2f}")
        print("---------------------------")


def RechercheEmploye(f, num):
    f.seek(0)
    while True:
        employe_data = f.read(employe_size)
        if not employe_data:
            break
        numeroMatricule, _, _, _ = struct.unpack(employe_format, employe_data)
        if numeroMatricule == num:
            print("Employé trouvé!")
            return True
    print("Employé non trouvé.")
    return False


def NbreEmployes2019(f):
    f.seek(0)
    count = 0
    while True:
        employe_data = f.read(employe_size)
        if not employe_data:
            break
        _, _, anneeEmbauche, _ = struct.unpack(employe_format, employe_data)
        if anneeEmbauche == 2019:
            count += 1
    return count


def ModifierEmploye(f, num):
    f.seek(0)
    employe_list = []
    while True:
        employe_data = f.read(employe_size)
        if not employe_data:
            break
        numeroMatricule, nom, anneeEmbauche, salaire = struct.unpack(employe_format, employe_data)
        if numeroMatricule == num:
            print(f"Salaire actuel: {salaire:.2f}")
            nouveau_salaire = float(input("Nouveau salaire : "))
            employe_data = struct.pack(employe_format, numeroMatricule, nom, anneeEmbauche, nouveau_salaire)
            print("Salaire modifié avec succès.")
        employe_list.append(employe_data)

    f.seek(0)
    f.truncate(0)
    for employe_data in employe_list:
        f.write(employe_data)


def SupprimerEmploye(f, num):
    f_temp = open("temp.dat", "wb")

    f.seek(0)
    while True:
        employe_data = f.read(employe_size)
        if not employe_data:
            break
        numeroMatricule, _, _, _ = struct.unpack(employe_format, employe_data)
        if numeroMatricule != num:
            f_temp.write(employe_data)

    f.close()
    f_temp.close()

    os.remove("employes.dat")
    os.rename("temp.dat", "employes.dat")

    f = open("employes.dat", "ab+")


def TriEmploye(f):
    f.seek(0)
    employe_list = []
    while True:
        employe_data = f.read(employe_size)
        if not employe_data:
            break
        employe_list.append(employe_data)

    employe_list.sort(key=lambda x: struct.unpack(employe_format, x)[-1], reverse=True)

    f.seek(0)
    f.truncate(0)
    for employe_data in employe_list:
        f.write(employe_data)

    print("Les employés ont été triés par salaire avec succès.")


if __name__ == "__main__":
    fichier = open("employes.dat", "ab+")

    if fichier is None:
        print("Erreur lors de l'ouverture du fichier")
        exit(1)

    choix = 0
    numeroMatricule = 0

    while choix != 8:
        print("\nMenu :")
        print("1. Saisir et écrire un employé")
        print("2. Afficher les employés")
        print("3. Rechercher un employé")
        print("4. Nombre d'employés recrutés en 2019")
        print("5. Modifier le salaire d'un employé")
        print("6. Supprimer un employé")
        print("7. Trier les employés par salaire")
        print("8. Quitter")

        choix = int(input("Choix : "))

        if choix == 1:
            SaisiEcrireEmploye(fichier)
        elif choix == 2:
            afficheEmploye(fichier)
        elif choix == 3:
            numeroMatricule = int(input("Entrez le numéro de matricule à rechercher : "))
            RechercheEmploye(fichier, numeroMatricule)
        elif choix == 4:
            print(f"Nombre d'employés recrutés en 2019 : {NbreEmployes2019(fichier)}")
        elif choix == 5:
            numeroMatricule = int(input("Entrez le numéro de matricule de l'employé à modifier : "))
            ModifierEmploye(fichier, numeroMatricule)
        elif choix == 6:
            numeroMatricule = int(input("Entrez le numéro de matricule de l'employé à supprimer : "))
            SupprimerEmploye(fichier, numeroMatricule)
        elif choix == 7:
            TriEmploye(fichier)
        elif choix == 8:
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

    fichier.close()
