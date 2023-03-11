from no import *
from fileOperations import *
from grafo import *

#Quebra as sequencias em K mers.
def quebraEmKmer(sequencia, k):
    k-=1
    sequenciaQuebrada = []
    for indice in range(len(sequencia) - k+1):
        sequenciaQuebrada.append(sequencia[indice:k+indice])
    #Prefixo, Sufixo
    return sequenciaQuebrada[0], sequenciaQuebrada[1]

#Concatena o mer atual à fita.
def adicionaFita(fita, mer):
    fita+=mer[-1]
    return fita

#Adiciona os vértices e as arestas do grafo.
def montaGrafo(grafo, sequencias, k):
    for sequencia in sequencias.dados:
        prefixo, sufixo = quebraEmKmer(sequencia, k)
        noPrefixo, noSufixo = No(prefixo), No(sufixo)
        #Adicionando o prefixo como vértice no grafo.
        if grafo.adicionaNoGrafo(noPrefixo.nome, noPrefixo):
            #O nó foi prefixo mais uma vez.
            noPrefixo.aumentaQtdPrefixos()
            #O sufixo é adicionado à lista de sufixos do nó.
            noPrefixo.adicionaSufixo(noSufixo.nome)
        #Caso ele já exista no grafo.
        else:
            #Adiciona o sufixo na lista de sufixos do nó.
            grafo.grafo[noPrefixo.nome].adicionaSufixo(noSufixo.nome)
            #O nó foi prefixo mais uma vez.
            grafo.grafo[noPrefixo.nome].aumentaQtdPrefixos()
        #Adiciona o sufixo como vértice no grafo.
        if grafo.adicionaNoGrafo(noSufixo.nome, noSufixo):
            #O nó foi sufixo mais uma vez.
            noSufixo.aumentaQtdSufixos()
        #Caso o sufixo já esteja no grafo.
        else:
            #Aumenta a quantidade de vezes que ele foi sufixo.
            grafo.grafo[noSufixo.nome].aumentaQtdSufixos()

#Exibe a estrutura do grafo.
def exibeGrafo(grafo):
    for item in grafo.grafo:
        print('Chave: {}\n Sufixos: {}\n Quantidade de Prefixos/Sufixos: [{},{}]'.format(grafo.grafo[item].nome, grafo.grafo[item].sufixos, grafo.grafo[item].qtdPrefixo, grafo.grafo[item].qtdSufixo))

#Busca o vértice inicial e o vértice final do caminho Euleriano.
def defineInicialEfinal(grafo):
    #Vértice inicial e vértice final.
    inicial, final = None, None
    for item in list(grafo.grafo.keys()):
        if grafo.grafo[item].diferenca > 0:
            inicial = grafo.grafo[item]
        elif grafo.grafo[item].diferenca < 0:
            final = grafo.grafo[item]            
    return inicial, final

def reconstrucao(grafoFinal,k):
    fitaAuxiliar, fitaUm, fitaDois = '', '', ''
    proximo = None
    inicial, final = defineInicialEfinal(grafoFinal)
    #Não existe vértice inicial ou final.
    if inicial is None or final is None:
        #print('Não é possível percorrer um caminho Euleriano!')
        return False
    proximo = inicial
    fita = ''
    fita += proximo.nome
    #Percorrendo o grafo até não existirem mais vértices.
    while len(grafoFinal.grafo.keys()) != 0:
        try:
            #Se a lista de sufixos do vértice não for vazia.
            if len(grafoFinal.grafo[proximo.nome].sufixos) != 0:
                #Retira o primeiro sufixo da lista de sufixos
                sufixoAtual = grafoFinal.grafo[proximo.nome].sufixos.pop(0)
                #O proximo a passar por esse processo será o sufixo retirado.
                proximo = grafoFinal.grafo[sufixoAtual]
                #Escreve na fita esse sufixo.
                fita = adicionaFita(fita, sufixoAtual)
                #Se após a remoção a lista de sufixos ficar vazia.
                if len(grafoFinal.grafo[proximo.nome].sufixos) == 0:
                    #Remove o vértice do grafo.
                    grafoFinal.removeDoGrafo(proximo.nome)
                #Se o não existir chave no grafo que coincida com o sufixo atual.
                if grafoFinal.pesquisaChave(proximo.nome) == False:
                    fitaAuxiliar = fita
                    fita = fitaUm+fitaAuxiliar+fitaDois
                    #Percorre a fita que já foi criada
                    for base in range(0,len(fita)-1):
                        #Percorre cada mer
                        merAtual = fita[base:base+k]
                        #Se esse mer da fita for vértice do grafo.
                        if grafoFinal.pesquisaChave(merAtual) == True:
                            #Se a lista de sufixos desse vértice não for vazia.
                            if len(grafoFinal.grafo[merAtual].sufixos) != 0:
                                #O próximo que antes era nulo, será esse vértice.
                                proximo = grafoFinal.grafo[merAtual]
                                #A primeira parte da fita será do inicio da fita até o mer encontrado.
                                fitaUm = fita[0:base+k]
                                #A segunda parte da fita será do mer encontrado até o fim da fita.
                                fitaDois = fita[base+k:len(fita)]
                                #A fita é reiniciada.
                                fita = ""
                                break
            else:
                #Remove o vértice do grafo.
                grafoFinal.removeDoGrafo(proximo.nome)
        except KeyError:
            #Programa finalizado.
            break
    return fita

def mainReconstrucao(arquivoEntrada):
    sequencias = Arquivo(arquivoEntrada)
    sequencias.dados = sequencias.abreArquivoSequencias()
    k = sequencias.kmer
    saida = Arquivo('Saidas/output.txt')
    grafo = Grafo()
    montaGrafo(grafo, sequencias, k)
    inicial, final = defineInicialEfinal(grafo)
    fita = reconstrucao(grafo,k-1)
    if fita != False:
        saida.escreveArquivo(fita)
        return inicial, final, fita, k
    #Não é possivel percorrer o caminho Euleriano.
    else:
        return None