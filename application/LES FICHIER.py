file = open("stagiaires.txt","w+")
file.write("reda\n")
file.write("hicham\n")
file.write("kamal\n")
file.write("joudia\n")

for i in range(5):
    file.write(str(i) + '\n')
file.close()
file = open("stagiaires.txt","r")

stag=file.read()
print(stag)
file.close()