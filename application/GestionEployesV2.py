import struct

# Définition de la classe Employe
class Employe:
    format_string = "i 50s i f"

    def __init__(self, numero_matricule, nom, annee_embauche, salaire):
        self.numero_matricule = numero_matricule
        self.nom = nom
        self.annee_embauche = annee_embauche
        self.salaire = salaire

    def pack(self):
        return struct.pack(self.format_string,
                           self.numero_matricule,
                           self.nom.encode('utf-8'),
                           self.annee_embauche,
                           self.salaire)

    @classmethod
    def unpack(cls, data):
        unpacked_data = struct.unpack(cls.format_string, data)
        return cls(*unpacked_data)

# Fonction pour saisir et écrire un employé dans un fichier binaire
def saisie_ecrire_employe(f):
    numero_matricule = int(input("Numéro de matricule : "))
    nom = input("Nom : ")
    annee_embauche = int(input("Année d'embauche : "))
    salaire = float(input("Salaire : "))

    employe = Employe(numero_matricule, nom, annee_embauche, salaire)
    f.write(employe.pack())
    print("Employé enregistré avec succès.")

# Fonction pour afficher les employés contenus dans un fichier binaire
def affiche_employe(f):
    f.seek(0)
    while True:
        data = f.read(struct.calcsize(Employe.format_string))
        if not data:
            break
        employe = Employe.unpack(data)
        print(f"Numéro de matricule: {employe.numero_matricule}")
        print(f"Nom: {employe.nom.decode('utf-8').rstrip('\x00')}")
        print(f"Année d'embauche: {employe.annee_embauche}")
        print(f"Salaire: {employe.salaire:.2f}")
        print("---------------------------")

# Exemple d'utilisation
with open("employes.bin", "ab+") as fichier:
    saisie_ecrire_employe(fichier)
    affiche_employe(fichier)
