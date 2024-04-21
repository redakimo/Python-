from tkinter import *
from tkinter import font
from tkinter import *
from time import *
import subprocess
import os
import sys


# classe qui encapsule tous les objets TKinter nécessaires �  la création d'un canevas

class CustomCanvas:
    def __init__(self, width, height):
        # width and height of the canvas
        self.width = width
        self.height = height

        # root Tk object
        self.root = Tk()

        # canvas attached to the root object
        self.canvas = Canvas(self.root, width=width,
                             height=height, highlightthickness=0)

        # binding of the different event
        # self.root.protocol("WM_DELETE_WINDOW", self.eventQuit)
        self.canvas.bind("<Button-1>", self.eventHandlerButton1)
        rightButton = "<Button-3>"  # d'après la doc le bouton droit le 3
        if sys.platform.startswith("darwin"):  # sous mac c'est le bouton 2
            rightButton = "<Button-2>"
        self.canvas.bind(rightButton, self.eventHandlerButton2)
        self.canvas.bind_all("<Key>", self.eventHandlerKey)
        self.canvas.pack()

        # eventQueue stores the list of events received
        self.eventQueue = []

        # font for the texte functions
        self.police = ("Purisa", 24)
        self.tkfont = font.Font(self.canvas, font=self.police)
        self.tkfont.height = self.tkfont.metrics("linespace")

        # marque
        self.tailleMarque = 5
        self.marqueh = None
        self.marquev = None

        # update
        self.root.update()

    def update(self):
        sleep(_tkinter.getbusywaitinterval() / 1000)
        self.root.update()

    def eventHandlerKey(self, event):
        self.eventQueue.append(("Touche", event))

    def eventHandlerButton2(self, event):
        self.eventQueue.append(("ClicDroit", event))

    def eventHandlerButton1(self, event):
        self.eventQueue.append(("ClicGauche", event))

    def eventQuit(self):
        self.eventQueue.append(("Quitte", ""))


__canevas = None


#############################################################################
# Exceptions
#############################################################################

class typeEvenementNonValide(Exception): pass


class fenetreNonCree(Exception): pass


class fenetreDejaCree(Exception): pass


#############################################################################
# Initialisation, mise �  jour et fermeture
#############################################################################

def creeFenetre(largeur, hauteur):
    """
    Crée une fenêtre largeur x hauteur.
    """
    global __canevas
    if __canevas != None:
        raise fenetreDejaCree('La fenetre a déj�  été crée avec la fonction "creeFenetre".')
    __canevas = CustomCanvas(largeur, hauteur)


def fermeFenetre():
    """"
    Détruit la fenêtre.
    """
    global __canevas
    if __canevas == None:
        raise fenetreNonCree("La fenetre n'a pas été crée avec la fonction \"creeFenetre\".")
    __canevas.root.destroy()
    __canevas = None


def miseAJour():
    """
    Met �  jour la fenêtre. Les dessins ne sont affichés qu'après
    l'appel �   cette fonction.
    """
    global __canevas
    if __canevas == None:
        raise fenetreNonCree("La fenetre n'a pas été crée avec la fonction \"creeFenetre\".")
    __canevas.update()


#############################################################################
# Fonctions de dessin
#############################################################################

####### Ligne

def ligne(ax, ay, bx, by):
    """
    Trace une ligne en noir du point (ax,ay) au point (bx,by).
    """
    global __canevas
    return __canevas.canvas.create_line(ax, ay, bx, by)


def ligneCouleur(ax, ay, bx, by, c):
    """
    Trace une ligne du point (ax,ay) au point (bx,by) de la couleur c.
    """
    global __canevas
    return __canevas.canvas.create_line(ax, ay, bx, by, fill=c)


####### Rectangle

def rectangle(ax, ay, bx, by):
    """
    Trace un rectangle en noir ayant le point (ax,ay) et le point (bx,by)
    comme coins.
    """
    global __canevas
    return __canevas.canvas.create_rectangle(ax, ay, bx, by)


def rectangleCouleur(ax, ay, bx, by, c):
    """
    Trace un rectangle en noir ayant le point (ax,ay) et le point (bx,by)
    comme coins avec la couleur c.
    """
    global __canevas
    return __canevas.canvas.create_rectangle(ax, ay, bx, by, outline=c)


def rectanglePlein(ax, ay, bx, by, c):
    """
    Trace un rectangle plein ayant le point (ax,ay) et le point (bx,by)
    comme coins avec la couleur c.
    """
    global __canevas
    return __canevas.canvas.create_rectangle(ax, ay, bx, by, fill=c, outline=c)


def polygonePlein(lst, c, b):
    """
    Trace un polygone qui passe par les points (lst[0],lst[1]) (lst[2],lst[3])
    etc la couleur de fond est c et celle du bord est b
    """
    global __canevas
    return __canevas.canvas.create_polygon(lst, fill=c, outline=b)


####### Cercle

def cercle(x, y, r):
    """
    Trace un cercle de centre (x,y) et de rayon r en noir.
    """
    global __canevas
    return __canevas.canvas.create_oval(x - r, y - r, x + r, y + r)


def cercleCouleur(x, y, r, c):
    """
    Trace un cercle de centre (x,y) et de rayon r de la couleur c.
    """
    global __canevas
    return __canevas.canvas.create_oval(x - r, y - r, x + r, y + r, outline=c)


def cerclePlein(x, y, r, c):
    """
    Trace un cercle plein de centre (x,y) et de rayon r de la couleur c.
    """
    global __canevas
    return __canevas.canvas.create_oval(x - r, y - r, x + r, y + r, fill=c, outline=c)


###### Marque

def marque(x, y):
    """
    Place la marque sur la position (x,y) qui peut être effacé en appelant
    `effaceMarque()`.
    """
    global __canevas
    effaceMarque()
    __canevas.marqueh = ligneCouleur(x - __canevas.tailleMarque, y, x + __canevas.tailleMarque, y, "red")
    __canevas.marquev = ligneCouleur(x, y - __canevas.tailleMarque, x, y + __canevas.tailleMarque, "red")


def effaceMarque():
    """
    Efface la marque affiché par la fonction `marque`
    """
    global __canevas
    if __canevas.marqueh != None and __canevas.marquev != None:
        efface(__canevas.marqueh)
        efface(__canevas.marquev)
        __canevas.marqueh = None
        __canevas.marquev = None


####### Texte

def texte(x, y, texte, c):
    """
    Affiche la chaîne `texte` avec (x,y) comme coin en haut �  gauche dans la couleur `c`.
    """
    global __canevas
    return __canevas.canvas.create_text(x, y, text=texte, font=__canevas.police, fill=c, anchor="nw")


def texteCentre(x, y, texte, c):
    """
    Affiche la chaîne `texte` centré sur le point (x,y) dans la couleur `c`.
    """
    global __canevas
    return __canevas.canvas.create_text(x, y, text=texte, font=__canevas.police, fill=c, anchor="center")


def longueurTexte(texte):
    """
    Donne la longueur en pixel nécessaire pour afficher `texte`.
    """
    global __canevas
    return __canevas.tkfont.measure(texte)


def hauteurTexte(texte):
    """
    Donne la hauteur en pixel nécessaire pour afficher `texte`.
    """
    global __canevas
    return __canevas.tkfont.height


#############################################################################
# Efface
#############################################################################

def effaceTout():
    """
    Efface la fenêtre
    """
    global __canevas
    __canevas.canvas.delete("all")


def efface(objet):
    """
    Efface `objet` de la fenêtre
    """
    global __canevas
    __canevas.canvas.delete(objet)


#############################################################################
# Utilitaires
#############################################################################


def attenteClic():
    """
    Attend que l'utilisateur clique sur la fenêtre
    """
    while True:
        ev = donneEvenement()
        typeEv = typeEvenement(ev)
        if typeEv == "ClicDroit" or typeEv == "ClicGauche":
            return (clicX(ev), clicY(ev))
        miseAJour()


def attenteTouche():
    """
    Attend que l'utilisateur clique sur la fenêtre
    """
    while True:
        ev = donneEvenement()
        typeEv = typeEvenement(ev)
        if typeEv == "Touche":
            return touche(ev)
        miseAJour()


def clic():
    """
    Attend que l'utilisateur clique sur la fenêtre
    """
    return attenteClic()


def captureEcran(file):
    """
    Fait une capture d'écran sauvegardé dans `file`.png
    """
    global __canevas
    __canevas.canvas.postscript(file=file + ".ps", height=__canevas.height, width=__canevas.width, colormode="color")
    subprocess.call("convert -density 150 -geometry 100% -background white -flatten " + file + ".ps " + file + ".png",
                    shell=True)
    subprocess.call("rm " + file + ".ps", shell=True)


#############################################################################
# Gestions des évènements
#############################################################################

def donneEvenement():
    """
    Renvoie l'évènement associe �  la fenêtre.
    """
    global __canevas
    if __canevas == None:
        raise fenetreNonCree("La fenetre n'a pas été crée avec la fonction \"creeFenetre\".")
    if len(__canevas.eventQueue) == 0:
        return ("RAS", "")
    else:
        return __canevas.eventQueue.pop()


def typeEvenement(evenement):
    """
    Renvoie une string donnant le type de evenement.

    Les types possibles sont:
    * 'ClicDroit'
    * 'ClicGauche'
    * 'Touche'
    * 'RAS'
    """
    nom, ev = evenement
    return nom


def clicX(evenement):
    """
    Renvoie la coordonnée X associé �  evenement qui doit être de type 'ClicDroit' ou 'ClicGauche'
    """
    nom, ev = evenement
    if not (nom == "ClicDroit" or nom == "ClicGauche"):
        raise typeEvenementNonValide('On peut pas utiliser "clicX" sur un évènement de type ' + nom)
    return ev.x


def clicY(evenement):
    """
    Renvoie la coordonnée Y associé �  evenement
    qui doit être de type 'ClicDroit' ou 'ClicGauche'
    """
    nom, ev = evenement
    if not (nom == "ClicDroit" or nom == "ClicGauche"):
        raise typeEvenementNonValide('On peut pas utiliser "clicY" sur un évènement de type ' + nom)
    return ev.y


def touche(evenement):
    """
    Renvoie une string correspondant �  la touche associé �  evenement
    qui doit être de type 'Touche'.
    """
    nom, ev = evenement
    if not (nom == "Touche"):
        raise typeEvenementNonValide('On peut pas utiliser "touche" sur un évènement de type ' + nom)
    return ev.keysym


dic = {}


def afficheImage(nom):
    global __canevas
    global dic
    image = PhotoImage(file=nom)
    dic['toto'] = image
    __canevas.canvas.create_image(200, 200, anchor=NW, image=image)
    __canevas.update()