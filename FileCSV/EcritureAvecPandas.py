from pandas import DataFrame
# data sous forme d'un dictionnaire
dictData = {'ID': [1 , 2 , 3],
            'Nom': ['Robert', 'Albert', 'Natalie'],
            'Age': [23, 37, 21],
            'Taille': [180 , 175 , 170],
            }
dataFrm = DataFrame(dictData, columns= ['ID', 'Nom', 'Age', 'Taille'])
# chemin vers un fichier pour stocker les resultats
export_csv = dataFrm .to_csv (r'Pandaresult.csv', index = None, header=False)
print (dataFrm )