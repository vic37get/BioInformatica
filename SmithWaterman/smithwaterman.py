import numpy as np

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
    gap_score = 0
    for linha in range(1, matriz.shape[1]):
        gap_score+=gap
        matriz[-1][linha] = gap_score
    gap_score = 0
    for coluna in range(matriz.shape[0]-2, -1, -1):
        gap_score+=gap
        matriz[coluna][0] = gap_score
    return matriz

#Código de alinhamento de sequencias Smith-Waterman.
def smithWaterman(sequenciaUm, sequenciaDois, match, mismatch, gap):
    #Montagem da matriz de scores.
    sequenciaUm = sequenciaUm[::-1]
    matriz = montaMatriz(sequenciaUm, sequenciaDois, gap)
    #Percorre a matriz de scores e atribui os respectivos valores, gaps, mismatch e match.
    for i in range(matriz.shape[0]-2, -1, -1):
        for j in range(1, matriz.shape[1]):
            score_match, gap_esquerda, gap_baixo, score_mismatch = float('-inf'), float('-inf'), float('-inf'), float('-inf')
            if sequenciaUm[i] == sequenciaDois[j - 1]:
                score_match = matriz[i + 1][j - 1] + match
            else:
                gap_esquerda = matriz[i][j - 1] + gap
                gap_baixo = matriz[i + 1][j] + gap
                score_mismatch = matriz[i + 1][j - 1] + mismatch
            matriz[i][j] = max(score_match, gap_esquerda, gap_baixo, score_mismatch)

    #BackTracing da matriz de scores.
    coluna = matriz.shape[1]-1
    maior_score, maior_posicao = 0, 0
    for linha in range(matriz.shape[0]-2, -1, -1):
        if matriz[linha][coluna] >= maior_score:
            maior_score = matriz[linha][coluna]
            maior_posicao = linha, coluna
    i, j = maior_posicao
    palavra1, palavra2 = [], []

    #Se o maior valor da matriz não estiver no fim da diagonal da matriz, ou seja, no índice 0.
    if i > 0:
        for item in range(i):
            palavra2.append('-')
            palavra1.append(sequenciaUm[item])
    
    #Alinhamento das sequências.
    while i != len(sequenciaUm) or j != 0:
        if matriz[i][j] == matriz[i + 1][j - 1] + match:
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