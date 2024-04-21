import os


file = open("myfile.txt", 'w')

T = "Python      est     un langage       de       programmation      de         haut      niveau    "
# ajouter le texte T au fichier
file.write(T)

# fermer le fichier
file.close()
# ouvrir le fichier en mode read
file = open("myfile.txt" , 'r')

content = file.read()
file.close()

# transformer le contenu en une liste
list_words = content.split()


content2=""

for word in list_words:
    content2 = content2 + word + " "


file = open("myfile2.txt" , 'w')
file.write(content2)

