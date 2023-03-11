from testeRemontagem import mainTesteRemontagem
from reconstrucao import mainReconstrucao
from geradorEntrada import GeraEntrada

#Programa principal que executa todo o processo de reconstrução.
def main(teste=False, entrada=True):
    if teste == True:
        #Arquivo de entrada, iterações, quantidade mínima de bases, quantidade máxima de bases, valor mínimo K, valor máximo K.
        mainTesteRemontagem('Entradas/input.txt', 10000, 3, 10000, 3, 100)
    elif entrada == True:
        #mainReconstrucao('Entradas/input.txt')
        mainReconstrucao('Entradas/Atividade_9.COMPUTACAO.PROVA.Vale 10.composicao_1_Bioinformaticas_size_30000_k_50.txt')
    else:
        #Quantidade de bases / Valor do K.
        GeraEntrada(10,3)
        mainReconstrucao('Entradas/input.txt')
    return

#Se teste = True: Roda a rotina de testes, com a quantidade determinada.
#Se teste = False e entrada = True: Usa a entrada atual (input.txt) para realizar a reconstrução.
#Se teste = False e entrada = False: Gera uma determinada entrada e reliza a reconstrução.
main(teste=False, entrada=True)