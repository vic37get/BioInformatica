from no import *
from fileOperations import *
from grafo import *
from copy import deepcopy

def quebraEmKmer(sequencia, k):
    k-=1
    kmers = []
    for indice in range(len(sequencia) - k+1):
        kmers.append(sequencia[indice:k+indice])
    return kmers[0], kmers[1]

def adicionaFita(fita, mer):
    fita+=mer[-1]
    return fita

def pecaDeFita(fita, indice, kmer):
    return fita[indice:kmer-1+indice]

def buscaNaFita(grafo, fita, kmer):
    for item in range(len(fita)):
        novoInicio = pecaDeFita(fita, item, kmer)
        if novoInicio in grafo.keys():
            return grafo[novoInicio]
    return None

def montaGrafo(grafo, k):
    for sequencia in sequencias.dados:
        prefixo, sufixo = quebraEmKmer(sequencia, k)
        prefixoNo, sufixoNo = No(prefixo), No(sufixo)
        #Adicionando o prefixo no grafo.
        if grafo.adicionaNoGrafo(prefixoNo.nome, prefixoNo) == True:
            prefixoNo.aumentaQtdPrefixos()
            prefixoNo.adicionaSufixo(sufixo)
        #Caso ele já exista no grafo.
        else:
            grafo.grafo[prefixoNo.nome].adicionaSufixo(sufixoNo.nome)
            grafo.grafo[prefixoNo.nome].aumentaQtdPrefixos()
        #Adiciona o sufixo no grafo.
        if grafo.adicionaNoGrafo(sufixoNo.nome, sufixoNo) == True:
            sufixoNo.aumentaQtdSufixos()
        #Caso o sufixo já esteja no grafo.
        else:
            #Aumenta a quantidade de vezes que ele foi sufixo.
            grafo.grafo[sufixoNo.nome].aumentaQtdSufixos()

def exibeGrafo(grafo):
    for item in grafo.grafo:
        print('Chave: {}\n Sufixos: {}\n Quantidade de Prefixos/Sufixos: [{},{}]'.format(grafo.grafo[item].nome, grafo.grafo[item].sufixos, grafo.grafo[item].qtdPrefixo, grafo.grafo[item].qtdSufixo))

def defineInicialEfinal(grafo):
    #Vértice inicial e vértice final.
    inicial, final = None, None
    for item in list(grafo.grafo.keys()):
        if grafo.grafo[item].diferenca > 0:
            inicial = grafo.grafo[item]
        elif grafo.grafo[item].diferenca < 0:
            final = grafo.grafo[item]            
    return inicial, final

def reconstrucao(grafoFinal):
    fitaAux = ''
    fitas = []
    inicial, final = defineInicialEfinal(grafoFinal)
    proximo = inicial
    fita = ''
    fita += proximo.nome
    #Percorrendo o grafo:

    while len(grafoFinal.grafo.keys()) > 0:
        exibeGrafo(grafoFinal)
        print('---------------------')
        if len(grafoFinal.grafo[proximo.nome].sufixos) > 0:
            atual = grafoFinal.grafo[proximo.nome].sufixos.pop(0)
            proximo = grafoFinal.grafo[atual]
            fita = adicionaFita(fita, proximo.nome)
        else:
            grafoFinal.removeDoGrafo(proximo.nome)
        if proximo == None:
            pass
        else:
            fitas.append(fita)
            proximo = buscaNaFita(grafoFinal.grafo, fita, kmer)

        #print('FITA: ', fita)
    saida.escreveArquivo(fita)


sequencias = Arquivo('input.txt')
sequencias.dados = sequencias.abreArquivo()
kmer = sequencias.kmer
saida = Arquivo('saida.txt')
grafo = Grafo()
montaGrafo(grafo, kmer)
exibeGrafo(grafo)
reconstrucao(grafo)