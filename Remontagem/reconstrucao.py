from no import *
from fileOperations import *
from grafo import *

sequencias = Arquivo('exemploAula.txt')
kmer = 3
grafo = Grafo()

def quebraEmKmer(sequencia, kmer):
    kmer-=1
    kmers = []
    for indice in range(len(sequencia) - kmer+1):
        kmers.append(sequencia[indice:kmer+indice])
    return kmers[0], kmers[1]

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

#Removendo mesma partidade
for item in list(grafo.grafo.keys()):
    #grafo.grafo[item].exibeNo()
    if grafo.grafo[item].qtdPrefixo == grafo.grafo[item].qtdSufixo:
        grafo.removeDoGrafo(item)
#Possivel inicial
inicial = []
for item in grafo.grafo.keys():
    if grafo.grafo[item].diferenca == 1:
        inicial.append(item)

    
    #grafo.adicionaNoGrafo(sufixoNo.nome, sufixoNo)

    
    