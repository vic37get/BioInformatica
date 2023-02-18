from no import *
from fileOperations import *
from grafo import *
from copy import deepcopy

sequencias = Arquivo('input.txt')
sequencias.dados = sequencias.abreArquivo()
saida = Arquivo('saida.txt')
kmer = 3
grafo = Grafo()

def quebraEmKmer(sequencia, kmer):
    kmer-=1
    kmers = []
    for indice in range(len(sequencia) - kmer+1):
        kmers.append(sequencia[indice:kmer+indice])
    return kmers[0], kmers[1]

def adicionaFita(fita, mer):
    fita+=mer[1:]
    return fita

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
    

grafoFinal = deepcopy(grafo)
#Removendo mesma paridade
for item in list(grafo.grafo.keys()):
    #grafo.grafo[item].exibeNo()
    if grafo.grafo[item].qtdPrefixo == grafo.grafo[item].qtdSufixo:
        grafo.removeDoGrafo(item)

#Possivel inicial
inicial = None
for item in grafo.grafo.keys():
    grafo.grafo[item].exibeNo()
    if grafo.grafo[item].diferenca == 1:
        atual = grafo.grafo[item]

#Percorrendo o grafo:
fita = ''
fita += atual.nome
while atual != None:
    if len(grafoFinal.grafo[atual.nome].sufixos) > 0:
        proximo = grafoFinal.grafo[atual.nome].sufixos.pop(0)
        atual = grafoFinal.grafo[proximo]
    else:
        grafoFinal.removeDoGrafo(proximo)
        break
    fita = adicionaFita(fita, atual.nome)
    print(fita)
saida.escreveArquivo(fita)
