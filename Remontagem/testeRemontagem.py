from geradorEntrada import GeraEntrada
import random
from reconstrucao import mainReconstrucao
from fileOperations import Arquivo

#Extrai o Mer inicial e o Mer final da fita.
def inicialFinalFita(fita, k):
    inicial = fita[:k-1]
    final = fita[(len(fita)-k+1):]
    return inicial, final

#Constrói a saída para ser escrita no Log de teste (Errado/Correto).
def saidaLog(resposta, saida, avaliacao):
    dadosLog = '\n'+avaliacao+'\n'+'Comparação:\n{}\n{}\n'.format(resposta, saida)+'Resposta: {}\n'.format(sorted(resposta))+'Saida: {}\n'.format(sorted(saida))+'Tamanho da resposta: {}\nTamanho obtido: {}'.format(len(resposta), len(saida))
    return dadosLog

#Testa se a saída produzida pelo programa de remontaegm é igual a saída original.
def testeSaida(inicial, final, fita, k):
    resposta = Arquivo('Saidas/resposta.txt').abreArquivo()
    saida = Arquivo('Saidas/output.txt').abreArquivo()
    #Obtem o mer inicial e o mer final da fita.
    inicialfita, finalfita = inicialFinalFita(fita, k)
    #Caso se ordene os dois, os mesmos forem iguais.
    if (sorted(resposta) == sorted(saida)):
        #Caso o mer inicial e o final da fita produzida sejam iguais aos mers iniciais e finais do grafo.
        if (inicial.nome == inicialfita and final.nome == finalfita):
            #dadosCorretos = saidaLog(resposta, saida, 'CORRETO!')
            #Arquivo('Saidas/logSaidaCorreto.txt').gravaArquivo(dadosCorretos)
            return True
        #Caso contrario, grava no arquivo logSaidaErrada.txt e retorna False.
        else:
            dadosErrados = saidaLog(resposta, saida, 'ERRADO!')
            Arquivo('Saidas/logSaidaErrada.txt').gravaArquivo(dadosErrados)
            return False
    #Caso as sequencias não sejam iguais, grava no arquivo logSaidaErrada.txt e retorna False.
    else:
        dadosErrados = saidaLog(resposta, saida, 'ERRADO!')
        Arquivo('Saidas/logSaidaErrada.txt').gravaArquivo(dadosErrados)
        return False

#Chamada do programa principal para executar os testes (iteracoes: quantidade de testes a serem executados).
def mainTesteRemontagem(arquivoEntrada, iteracoes, min_qtd_bases, max_qtd_bases, min_k, max_k):
    iter = 0
    while(iter < iteracoes):
        #Obtem um número de K aleatório.
        k = random.randint(min_k, max_k)
        #Obtem uma quantidade aleatoria de bases.
        qtdBases = random.randint(min_qtd_bases, max_qtd_bases)
        if GeraEntrada(qtdBases, k):
            #Executa o algoritmo de reconstrução e obtem os valores de mer inicial e final, a fita gerada e o k fornecido.
            if mainReconstrucao(arquivoEntrada):
                inicial, final, fita, k = mainReconstrucao(arquivoEntrada)
                #Obtem a resposta do teste (Correto = True, Incorreto = False).
                resposta = testeSaida(inicial, final, fita, k)
                #Se a resposta for errada:
                if resposta != True:
                    print('RESPOSTA ERRADA!!')
                iter+=1
                print('Iteração: {}, Resposta: {}'.format(iter, resposta))
            else:
                #Não é possivel percorrer um caminho Euleriano!
                pass
        else:
            #O valor do K é maior que a quantidade de bases.
            pass