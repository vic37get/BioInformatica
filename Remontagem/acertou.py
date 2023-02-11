gabarito = ""
resposta = ""
file = open("resposta.txt","r")
gabarito = file.read()
file.close()
file = open("JoaoPaz.txt","r")
resposta = file.read()
file.close()
if( gabarito == resposta ):
    print("Acertou!")
else:
    print("Errou!")
