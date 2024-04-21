import os
user=os.getlogin()
print(user)
f=open("C:/Users/" + user + "/desktop/monfichier1.txt","w")
os.startfile("C:/Users/" + user + "/desktop/monfichier1.txt")

with open("myfile2.txt","r") as f:
    cont=f.read()
    print(cont)
    nouvcont=cont.replace("haut","bass")

with open("myfile2.txt","w") as f:
    f.write(nouvcont)