import numpy as np
from copy import deepcopy

#Abre o arquivo de input e retorna os dados dele.
def abreInput(filename):
    with open(filename, 'r') as f:
        dados = f.readlines()
    dados = trataInput(dados)
    return dados

#Grava a saída gerada pelo programa.
def gravaOutput(info, filename):
    with open(filename, 'w') as f:
        for linha in info.values():
            f.writelines(str(linha)+'\n')

#Recebe os dados do arquivo input e os formata em um dicionario.
def trataInput(dados):
    for item in range(len(dados)):
        dados[item] = dados[item].replace('\n', '')

    info = {'sequenciaUm': dados[0],
            'sequenciaDois': dados[1],
            'score': None,
            'match': dados[2],
            'mismatch': int(dados[3]),
            'gap': int(dados[4]),
    }   
    return info

#Monta a matriz de scores, já adicionando os valores de gap.
def montaMatriz(sequenciaUm, sequenciaDois, gap):
    matriz = np.zeros((len(sequenciaUm) + 1, len(sequenciaDois) + 1))
    matrizCaminho = [['' for j in range(len(sequenciaDois) + 1)] for i in range(len(sequenciaUm) + 1)]
    gap_score = 0
    for linha in range(1, matriz.shape[1]):
        gap_score+=gap
        matriz[-1][linha] = gap_score
        matrizCaminho[-1][linha] = 'es'
    gap_score = 0
    for coluna in range(matriz.shape[0]-2, -1, -1):
        gap_score+=gap
        matriz[coluna][0] = gap_score
        matrizCaminho[coluna][0] = 'ba'
    return matriz, matrizCaminho

def valoresIguais(listaValores):
    listaIguais = []
    for indice, item in enumerate(listaValores):
        listaTeste = deepcopy(listaValores)
        valor = listaTeste[indice]
        del listaTeste[indice]
        for val in listaTeste:
            if val[2] == valor[2] and valor != float('-inf'):
                listaIguais.append(listaValores[indice])
    return listaIguais

#Código de alinhamento de sequencias Smith-Waterman.
def smithWaterman(sequenciaUm, sequenciaDois, match, mismatch, gap):
    #Montagem da matriz de scores.
    sequenciaUm = sequenciaUm[::-1]
    matriz, matrizCaminho = montaMatriz(sequenciaUm, sequenciaDois, gap)
    #Percorre a matriz de scores e atribui os respectivos valores, gaps, mismatch e match.
    for i in range(matriz.shape[0]-2, -1, -1):
        for j in range(1, matriz.shape[1]):
            score_match, gap_esquerda, gap_baixo, score_mismatch = float('-inf'), float('-inf'), float('-inf'), float('-inf')
            if sequenciaUm[i] == sequenciaDois[j - 1]:
                score_match = matriz[i + 1][j - 1] + match
            
            score_mismatch = matriz[i + 1][j - 1] + mismatch
            gap_esquerda = matriz[i][j - 1] + gap
            gap_baixo = matriz[i + 1][j] + gap

            anterior_match = matriz[i + 1][j - 1]
            anterior_mismatch = matriz[i + 1][j - 1]
            anterior_esquerda = matriz[i][j - 1]
            anterior_baixo = matriz[i + 1][j]

            #print(score_match, score_mismatch, gap_esquerda, gap_baixo)
            dados = [['di',anterior_match, score_match],['di',anterior_mismatch, score_mismatch],['es',anterior_esquerda, gap_esquerda],['ba', anterior_baixo, gap_baixo]]
            nIguais = valoresIguais(dados)
            if len(nIguais) > 0:
                maior = min(nIguais, key=lambda x: x[1])
                dados.remove(maior)
            valores = [valor[2] for valor in dados]
            direcoes = [direcao[0] for direcao in dados]
            indice = valores.index(max(valores))
            matriz[i][j] = valores[indice]
            matrizCaminho[i][j] = direcoes[indice]

    #MATRIZ CAMINHO MONTADA, SO FALTA PERCORRER COM BASE NAS DIREÇÕES


    #BackTracing da matriz de scores.
    maior_score = np.max(matriz[:,-1])
    i, j = 0, matriz.shape[1]-1
    with open('matriz.txt', 'w') as f:
        f.write(str(matriz))

    #Alinhamento das sequências.
    palavra1, palavra2 = [], []
    while i != len(sequenciaUm) or j != 0:

        if j == 0:
            palavra1.append(sequenciaUm[i])
            palavra2.append('-')
            i+=1
        
        elif i == len(sequenciaUm):
            palavra1.append('-')
            palavra2.append(sequenciaDois[j - 1])
            j-=1

        elif matriz[i][j] == matriz[i + 1][j - 1] + match:
            palavra1.append(sequenciaUm[i])
            palavra2.append(sequenciaDois[j-1])
            i+=1
            j-=1
        
        elif matriz[i][j] == matriz[i + 1][j - 1] + mismatch:
            palavra1.append(sequenciaUm[i])
            palavra2.append(sequenciaDois[j-1])
            i+=1
            j-=1
            
        elif matriz[i][j] == matriz[i + 1][j] + gap:
            palavra1.append(sequenciaUm[i])
            palavra2.append('-')
            i+=1
            
        elif matriz[i][j] == matriz[i][j-1] + gap:
            palavra2.append(sequenciaDois[j-1])
            palavra1.append('-')
            j-=1

    #Inversão da ordem ou sentido das sequências.
    seq1 = ''.join(palavra1)[::-1]
    seq2 = ''.join(palavra2)[::-1]

    return seq1, seq2, maior_score

#Chamada do programa.
info = abreInput('input.txt')
seq1, seq2, maior_score = smithWaterman(info['sequenciaUm'], info['sequenciaDois'], int(info['match']), info['mismatch'], info['gap'])
info['sequenciaUm'] = seq1
info['sequenciaDois'] = seq2
info['score'] = int(maior_score)
gravaOutput(info, 'output.txt')