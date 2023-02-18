
#Funcionamento do algoritmo:
# 1. Conforme especificações, gera uma fita de dna aleatória.
# 2. Gera - se uma composição k - mer, ordenada, a partir da fita.
# 3. A composição k - mer é salva em um arquivo.

import random

#Informe o tamanho total da fita de dna:
bases = 30000

#Informe o tamanho do k:
k = 50

#Não precisa alterar o código a partir da linha
#---------------------------------------------------------------------------------------------------#

dna = []
mers = []
letras = "ACGT"
resposta = ""
if( k <= bases ):
    for x in range( bases ):
        dna.append( letras[random.randint(0,3)] )
    resposta = "".join( dna )
    bases = bases - k + 1
    control = 0
    for x in range( bases ):
        mers.append( resposta[control:control+k] + ",")
        control = control + 1
    
    mers.sort()
    mers = "".join(mers).replace(" ","").replace("[","").replace("]","").replace("'","")
    
file = open("input_teste.txt","w")
file.write(mers)
file.close()
file = open("resp.txt","w")
file.write(resposta)
file.close()
print("Feito!")
