import random

def GeraEntrada(bases, k):
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
        file = open("Entradas/input.txt","w")
        file.write(mers)
        file.close()
        file = open("Saidas/resposta.txt","w")
        file.write(resposta)
        file.close()
        return True
    else:
        return False