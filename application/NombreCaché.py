#coding:utf-8
"""
variable nomre_caché,proposotion,tentative :entier
debut
    nombre_cache=aleatoir(0,100)
    tentative=0
    tant que tentatives < 7
        ecrire"Proposez un nombre entre 0 et 100 : "
        Lire proposition
        tentatives <-- tentatives + 1
        si proposition = nombre_cache:
           Ecrire("Félicitations, vous avez trouvé le nombre en",tentatives, "tentatives !")
           break
       sinon:
            si proposition < nombre_cache alors
                Ecrire("Le nombre recherché est plus grand.")
            sinon
                ecrire("Le nombre recherché est plus petit.")
            finSi
        FinSi
    FinTantQue

si proposition != nombre_cache and tentatives >= 7 alors
    ecrire("Désolé, vous avez perdu. Le nombre caché était", nombre_cache)
finsi
Fin   
"""



import random
nombre_cache = random.randint(0, 100)
tentatives = 0
while tentatives < 7:
       proposition = int(input("Proposez un nombre entre 0 et 100 : "))
       tentatives += 1
       if proposition == nombre_cache:
           print(f"Félicitations, vous avez trouvé le nombre en {tentatives} tentatives !")
           break
       else:
            if proposition < nombre_cache:
                print("Le nombre recherché est plus grand.")
            else:
                print("Le nombre recherché est plus petit.")
if proposition != nombre_cache and tentatives >= 7:
    print(f"Désolé, vous avez perdu. Le nombre caché était {nombre_cache}.")



