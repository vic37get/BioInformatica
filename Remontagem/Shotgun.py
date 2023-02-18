import random

#Coloque quantas bases você deseja
bases = 20

#Coloque o tamanho do k que você deseja
k = 3

#----------------------------------------#
dna = ""
resposta = ""
mers = []
letras = "ACGT"

if( k <= bases ):
    for x in range( bases ):
        dna = dna + letras[random.randint(0,3)]
    resposta = dna
    bases = bases - k + 1
    for x in range( bases ):
        mers.append( "," + dna[0:k] )
        dna = dna.replace(dna[0],"",1)

    mers.sort()
    mers = "".join(mers).replace(" ","").replace("[","").replace("]","").replace("'","")
    mers = mers.replace(mers[0],"",1)
    
file = open("input.txt","w")
file.write(mers)
file.close()
file = open("resposta.txt","w")
file.write(resposta)
file.close()
print("Feito")
