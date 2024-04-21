import csv

# 1. Créer une fonction pour importer le fichier dans une table
def importer_utilisateurs(nom_fichier):
    table_utilisateurs = []
    with open(nom_fichier, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            table_utilisateurs.append(dict(row))
    return table_utilisateurs

# 2. Utiliser la fonction pour créer la table utilisateurs
table_utilisateurs = importer_utilisateurs('utilisateurs.csv')

# 3. Créer la table des joueurs ayant moins de 300 points au premier jeu
def joueurs_moins_de_300_points(table):
    return [joueur for joueur in table if int(joueur['score_1']) < 300]

# 4. Créer la table des enregistrements des filles
def enregistrements_des_filles(table):
    return [joueur for joueur in table if joueur['genre'].lower() == 'f']

# 5. Créer la table des enregistrements des utilisateurs du domaine @example.fr
def utilisateurs_domaine_example(table):
    return [joueur for joueur in table if joueur['email'].endswith('@example.fr')]

# 6. Fonction pour les meilleurs scores pour chaque jeu
def meilleurs_scores_par_jeu(table, jeu):
    return sorted(table, key=lambda x: int(x[f'score_{jeu}']))

# 7. Fonction pour la liste des meilleurs scores pour chaque jeu triés par score croissant
def liste_meilleurs_scores(table):
    result = {}
    for jeu in range(1, 3):
        scores = meilleurs_scores_par_jeu(table, jeu)
        result[f'score_{jeu}'] = scores
    return result

# 8. Fonction pour le score moyen de chaque jeu
def score_moyen_par_jeu(table, jeu):
    scores = [int(joueur[f'score_{jeu}']) for joueur in table]
    return sum(scores) / len(scores)

# 9. Fonction pour la projection des adresses mail
def projection_adresses_mail(table):
    return [joueur['email'] for joueur in table]

# 10. Fonction pour les 10 joueurs ayant le plus mauvais score pour chaque jeu, sans doublons
def pires_scores_par_jeu_sans_doublons(table):
    result = {}
    for jeu in range(1, 3):
        scores = sorted(table, key=lambda x: int(x[f'score_{jeu}']), reverse=True)[:10]
        result[f'score_{jeu}'] = list(set([joueur['email'] for joueur in scores]))
    return result

# Utilisation des fonctions
joueurs_moins_de_300 = joueurs_moins_de_300_points(table_utilisateurs)
filles = enregistrements_des_filles(table_utilisateurs)
example_fr = utilisateurs_domaine_example(table_utilisateurs)
meilleurs_scores = liste_meilleurs_scores(table_utilisateurs)
score_moyen_jeu1 = score_moyen_par_jeu(table_utilisateurs, 1)
adresses_mail = projection_adresses_mail(table_utilisateurs)
pires_scores_sans_doublons = pires_scores_par_jeu_sans_doublons(table_utilisateurs)

# Exemples d'utilisation des résultats
print("Joueurs ayant moins de 300 points au premier jeu:", joueurs_moins_de_300)
print("Enregistrements des filles:", filles)
print("Enregistrements des utilisateurs du domaine @example.fr:", example_fr)
print("Liste des meilleurs scores pour chaque jeu:", meilleurs_scores)
print("Score moyen pour le premier jeu:", score_moyen_jeu1)
print("Projection des adresses mail:", adresses_mail)
print("Les 10 joueurs ayant le plus mauvais score pour chaque jeu, sans doublons:", pires_scores_sans_doublons)
