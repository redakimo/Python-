#coding:utf-8
# Imports ---------------------------------------------------------------------
from random import *
from iutk import *

# PARTIE A NE PAS MODIFIER ====================================================

def matriceAleatoire():
    """Renvoie une matrice 9x9 d'entiers entre 1 et 9 choisis au hasard."""
    M = []
    for i in range(9):
        M.append([])
        for j in range(9):
            M[i].append(randint(1, 9))
    return M

def estPermutation(T):
    """Renvoie True si T est une permutation de 1, 2, ..., n, False sinon."""
    n = len(T)
    r = True
    elements = []
    for i in range(n):
        elements.append(False)
    i = 0
    while i < n and r:
        if T[i] >= 1 and T[i] <= n:
            r = not elements[T[i] - 1]
            elements[T[i] - 1] = True
        else:
            r = False
        i += 1
    return r

def verifierLigne(M, i):
    """Renvoie 1 si la ligne i de M est valide, 0 sinon."""
    return estPermutation(M[i])

def verifierColonne(M, j):
    """Renvoie 1 si la colonne j de M est valide, 0 sinon."""
    # extraire les Ã©lÃ©ments de la colonne j dans une liste
    L = []
    for i in range(len(M)):
        L.append(M[i][j])
    return estPermutation(L)

def verifierSousMatrice(M, i, j):
    """Renvoie 1 si la sous-matrice 3x3 de M commenÃ§ant en ligne i et en
    colonne j est valide, 0 sinon.
    """
    # extraire les Ã©lÃ©ments de la sous-matrice dans une liste
    L = []
    for k in range(i, i + 3):
        for p in range(j, j + 3):
            L.append(M[k][p])
    return estPermutation(L)

def verifierMatrice(M):
    """Renvoie 1 si la matrice M est valide, 0 sinon."""
    n = len(M)
    # 1 vÃ©rifier les lignes et les colonnes
    for i in range(n):
        if not verifierLigne(M, i) or not verifierColonne(M, i):
            return False

    # 2 vÃ©rifier les sous-matrices
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not verifierSousMatrice(M, i, j):
                return False

    # on a passÃ© tous les tests, la matrice est donc valide
    return True

def grilleValideAleatoire():
    """Renvoie une matrice 9x9 d'entiers choisis au hasard qui constitue une
    grille valide (d'aprÃ¨s les critÃ¨res Sudoku)."""
    M = [[1, 2, 3, 7, 8, 9, 4, 5, 6],
         [4, 5, 6, 1, 2, 3, 7, 8, 9],
         [7, 8, 9, 4, 5, 6, 1, 2, 3],
         [2, 3, 1, 8, 9, 7, 5, 6, 4],
         [5, 6, 4, 2, 3, 1, 8, 9, 7],
         [8, 9, 7, 5, 6, 4, 2, 3, 1],
         [3, 1, 2, 9, 7, 8, 6, 4, 5],
         [6, 4, 5, 3, 1, 2, 9, 7, 8],
         [9, 7, 8, 6, 4, 5, 3, 1, 2]]
    renommageAleatoire(M)
    return M

def renommageAleatoire(M):
    """Rajoute un entier alÃ©atoire modulo 9 puis incrÃ©mente chaque entrÃ©e de
    M."""
    p = randint(1, 8)
    for i in range(9):
        for j in range(9):
            M[i][j] = (M[i][j] + p) % 9 + 1

def genererPuzzle(casesRestantesMin=17,casesRestantesMax=26):
    """GÃ©nÃ¨re un puzzle Ã  rÃ©soudre pour l'utilisateur, en partant d'une grille
    valide.
    Le nombre de cases restantes sera choisi alÃ©atoirement dans l'intervalle fourni.
    """
    M = grilleValideAleatoire()
    nb_restants = randint(casesRestantesMin,casesRestantesMax)  # le nombre de cases qu'on va laisser
    n = len(M)
    nb_elem = n * n  # 81 dans le cas du Sudoku classique
    # gÃ©nÃ©rer des paires d'indices valides alÃ©atoires tant qu'on doit supprimer
    # des Ã©lÃ©ments
    while nb_elem > nb_restants:
        i, j = randint(0, n - 1), randint(0, n - 1)
        if M[i][j] != 0:  # si l'Ã©lÃ©ment n'a pas encore Ã©tÃ© effacÃ©
            M[i][j] = 0  # l'effacer
            nb_elem -= 1  # mettre Ã  jour le nombre d'Ã©lÃ©ments

    return M

# FIN DE LA PARTIE A NE PAS MODIFIER ==========================================
