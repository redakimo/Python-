#coding:utf-8
import csv

from pandas import DataFrame

def importer_utilisateurs(nom_fichier):
    table_utilisateurs = []
    with open(nom_fichier, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            table_utilisateurs.append(dict(row))
    return table_utilisateurs

table_utilisateurs = importer_utilisateurs('utilisateurs.csv')
print(table_utilisateurs)


def Score_moins_300(table):
    return [joueur for joueur in table if int(joueur['score_1']) < 300]

def genre_fille(table):
    return [joueur for joueur in table if joueur['genre'].lower() == 'f']

#
def user_domain(table):
    return [joueur for joueur in table if joueur['email'].endswith('@example.com')]

#fonction dretournant le meilleur score par jeu:
def meilleurs_sc_par_jeu(table):
    return sorted(table, key=lambda x: int(x[f'score_1']))



#creation de liste de dictionnaires retourné par chaque fonction :
Score_moins_300 = Score_moins_300(table_utilisateurs)
filles = genre_fille(table_utilisateurs)
example_com = user_domain(table_utilisateurs)
meilleurs_scores = meilleurs_sc_par_jeu(table_utilisateurs)


#affichage des resultats :
print("resultat de chaque fonction :")
print("##############################################################################################################")
print("Joueurs ayant moins de 300 points au premier jeu:", Score_moins_300)
print("##############################################################################################################")
dataFrmscrore_300 = DataFrame(Score_moins_300, columns= ['nom', 'genre', 'score_1','score_1', 'email'])
# chemin vers un fichier pour stocker les resultats
export_csv = dataFrmscrore_300 .to_csv (r'Pandascrore_300.csv', index = None, header=False)
print (dataFrmscrore_300 )
print("##############################################################################################################")

print("Enregistrements des utilisateurs du domaine @example.fr:", example_com)
print("##############################################################################################################")
print("Enregistrements des filles:", filles)
print("##############################################################################################################")

dataFrmfilles = DataFrame(filles, columns= ['nom', 'genre', 'score_1','score_1', 'email'])
# chemin vers un fichier pour stocker les resultats
export_csv = dataFrmfilles .to_csv (r'PandaFilles.csv', index = None, header=False)
print (dataFrmfilles )

print("##############################################################################################################")
print()
print("Liste des meilleurs scores pour chaque jeu:", meilleurs_scores)