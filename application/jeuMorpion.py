#coding:utf-8
import random


def afficher_grille(grille):
    """
    Affiche la grille de morpion.
    """
    for i in range(3):
        print(" | ".join(grille[i * 3: i * 3 + 3]))
        if i < 2:
            print("-" * 9)


def tester_victoire(grille, symbole):
    """
    Teste si un joueur a gagné.
    """
    lignes = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for ligne in lignes:
        if grille[ligne[0]] == grille[ligne[1]] == grille[ligne[2]] == symbole:
            return True
    return False


def tester_grille_pleine(grille):
    """
    Teste si la grille est pleine.
    """
    return " " not in grille


def joueur_humain():
    """
    Fonction qui permet à un joueur humain de jouer.
    """
    while True:
        coup = input("Entrez votre coup (de 1 à 9) : ")
        if coup.isdigit() and 1 <= int(coup) <= 9:
            coup = int(coup) - 1
            if grille[coup] == " ":
                return coup
            else:
                print("Cette case est déjà occupée. Essayez à nouveau.")
        else:
            print("Veuillez entrer un nombre entre 1 et 9.")


def joueur_ordi():
    """
    Fonction qui permet à l'ordinateur de jouer.
    """
    coups_disponibles = [i for i, symbole in enumerate(grille) if symbole == " "]
    return random.choice(coups_disponibles)


def jouer_coup(joueur, symbole):
    """
    Fait jouer un joueur.
    """
    if joueur == "humain":
        coup = joueur_humain()
    else:
        coup = joueur_ordi()
    grille[coup] = symbole


# Initialisation de la grille
grille = [" " for _ in range(9)]

# Boucle principale
while True:
    afficher_grille(grille)

    # Tour du joueur 1 (X)
    jouer_coup("humain", "X")
    if tester_victoire(grille, "X"):
        afficher_grille(grille)
        print("Joueur 1 a gagné !")
        break
    if tester_grille_pleine(grille):
        afficher_grille(grille)
        print("Match nul !")
        break

    # Tour du joueur 2 (O)
    jouer_coup("ordi", "O")
    if tester_victoire(grille, "O"):
        afficher_grille(grille)
        print("Ordinateur a gagné !")
        break
    if tester_grille_pleine(grille):
        afficher_grille(grille)
        print("Match nul !")
        break
