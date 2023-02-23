from no import *
from fileOperations import *
from grafo import *
from copy import deepcopy

def quebraEmKmer(sequencia, kmer):
    kmer-=1
    kmers = []
    for indice in range(len(sequencia) - kmer+1):
        kmers.append(sequencia[indice:kmer+indice])
    print(kmers[0], kmers[1])
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

def montaGrafo(grafo, kmer):
    for sequencia in sequencias.dados:
        prefixo, sufixo = quebraEmKmer(sequencia, kmer)
        prefixoNo = No(prefixo)
        sufixoNo = No(sufixo)
        #PREFIXO
        if grafo.adicionaNoGrafo(prefixoNo.nome, prefixoNo) == True:
            prefixoNo.aumentaQtdPrefixos()
            prefixoNo.adicionaSufixo(sufixo)
        else:
            grafo.grafo[prefixoNo.nome].adicionaSufixo(sufixoNo.nome)
            grafo.grafo[prefixoNo.nome].aumentaQtdPrefixos()
        #SUFIXO
        if grafo.adicionaNoGrafo(sufixoNo.nome, sufixoNo) == True:
            sufixoNo.aumentaQtdSufixos()
        else:
            grafo.grafo[sufixoNo.nome].aumentaQtdSufixos()
    
def defineInicial():
    #Removendo mesma paridade
    for item in list(grafo.grafo.keys()):
        if grafo.grafo[item].qtdPrefixo == grafo.grafo[item].qtdSufixo:
            grafo.removeDoGrafo(item)
    #Possivel inicial
    inicial = None
    for item in grafo.grafo.keys():
        if grafo.grafo[item].diferenca == 1:
            inicial = grafo.grafo[item]
    return inicial

def reconstrucao(grafoFinal):
    proximo = defineInicial()
    #Percorrendo o grafo:
    fita = ''
    fita += proximo.nome
    while len(grafoFinal.grafo) > 0:
        print(proximo.nome)
        print(grafoFinal.grafo.keys())
        if len(grafoFinal.grafo[proximo.nome].sufixos) > 0:
            atual = grafoFinal.grafo[proximo.nome].sufixos.pop(0)
            proximo = grafoFinal.grafo[atual]
        else:
            print('removi')
            grafoFinal.removeDoGrafo(proximo.nome)
            proximo = None
            print(grafoFinal.grafo.keys())
        if proximo != None:
            fita = adicionaFita(fita, proximo.nome)
        else:
            proximo = buscaNaFita(grafoFinal.grafo, fita, kmer)
            print('to buscando na fita')
            print(len(grafoFinal.grafo))
        print('FITA: ', fita)
    saida.escreveArquivo(fita)


sequencias = Arquivo('exemploAula.txt')
sequencias.dados = sequencias.abreArquivo()
kmer = sequencias.kmer
saida = Arquivo('saida.txt')
grafo = Grafo()
montaGrafo(grafo, kmer)
grafoFinal = deepcopy(grafo)
reconstrucao(grafoFinal)