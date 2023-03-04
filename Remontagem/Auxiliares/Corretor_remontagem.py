
#Funcionamento do algoritmo:
# 1. Lê - se a composição k - mer original.
# 2. Lê - se a fita de dna que foi gerada por seu algoritmo de remontagem.
# 3. Faz - se a composição k - mer, ordenada, da sua fita de dna.
# 4. Compara - se a sua composição k - mer da original, apontando alguns comentários.
# 5. Os comentários são salvos em um arquivo de nome: resposta_"nome do seu arquivo".


gabarito = ""
resposta = ""

#Informe o arquivo que contenha a composição original:
file = open("input_teste.txt","r")

gabarito = file.read()
file.close()

#Informe o arquivo que contenha a sua resposta:
file_name = "joaopaz.txt"

#Não precisa alterar o código a partir da linha
#---------------------------------------------------------------------------------------------------#

file = open(file_name,"r")
resposta = file.read()
file.close()

k = gabarito.index(",")
new_resposta = []

for x in range(len(resposta) - k + 1):
    new_resposta.append( resposta[0:k] + ",")
    resposta = resposta.replace(resposta[0],"",1)
    
new_resposta.sort()
new_resposta = "".join(new_resposta).replace(" ","").replace("'","").replace("[","").replace("]","")

acertos = 0
erros = 0
posicao = []
total = len(gabarito)

for x in range( len(gabarito) ):
    try:
        if( gabarito[x] == new_resposta[x] ):
            acertos = acertos + 1
        else:
            erros = erros + 1
            posicao.append(x)
            
    except:
        break
if( acertos == total ):
    print("Acertou")
else:
    print("errou")
comentarios = ""
comentarios = comentarios + f"Tamanho do gabarito: {len(gabarito)} | Tamanho da sua resposta: {len(new_resposta)}\n"
comentarios = comentarios + f"Acertos: {acertos}\n"
comentarios = comentarios + f"Erros: {erros}\n"
comentarios = comentarios + f"Posicao dos erros: {posicao}\n"
comentarios = comentarios + f"Provavel nota: {(acertos*10.0)/(total)}\n"
comentarios = comentarios + f"\nSua resposta:\n{new_resposta}\n\n"
comentarios = comentarios + f"Gabarito:\n{gabarito}\n"
file_name = file_name.split(".")[0]
file = open(f"resposta_{file_name}.txt","w")
file.write(comentarios)
file.close()
print("Feito!")
