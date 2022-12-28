import numpy as np

def abreInput(filename):
    with open(filename, 'r') as f:
        dados = f.readlines()
    dados = trataInput(dados)
    return dados

def gravaOutput(info, filename):
    with open(filename, 'w') as f:
        for linha in info.values():
            f.writelines(str(linha)+'\n')

def trataInput(dados):
    for item in range(len(dados)):
        dados[item] = dados[item].replace('+', '').replace('\n', '')

    info = {'sequenciaUm': dados[0],
            'sequenciaDois': dados[1],
            'score': None,
            'match': int(dados[2]),
            'mismatch': int(dados[3]),
            'gap': int(dados[4]),
    }
    return info

def montaMatriz(sequenciaUm, sequenciaDois):
    matriz = np.zeros((len(sequenciaUm) + 1, len(sequenciaDois) + 1))
    gap = 0
    for linha in range(1, matriz.shape[1]):
        gap-=2
        matriz[-1][linha] = gap
    gap = 0
    for coluna in range(matriz.shape[0]-2, -1, -1):
        gap-=2
        matriz[coluna][0] = gap
    return matriz

def smithWaterman(sequenciaUm, sequenciaDois, match, mismatch, gap):
    sequenciaUm = sequenciaUm[::-1]
    matriz = montaMatriz(sequenciaUm, sequenciaDois)
    
    for i in range(matriz.shape[0]-2, -1, -1):
        for j in range(1, matriz.shape[1]):
            score_match, gap_esquerda, gap_direita, score_mismatch = float('-inf'), float('-inf'), float('-inf'), float('-inf')
            print('DIAGONAL: ', matriz[i + 1][j - 1] + mismatch)
            print('GAP DA ESQUERDA: ', matriz[i][j - 1] + gap)
            print('GAP DA DIREITA: ', matriz[i + 1][j] + gap)
            if sequenciaUm[i] == sequenciaDois[j - 1]:
                score_match = matriz[i + 1][j - 1] + match
            else:
                gap_esquerda = matriz[i][j - 1] + gap
                gap_direita = matriz[i + 1][j] + gap
                score_mismatch = matriz[i + 1][j - 1] + mismatch
            matriz[i][j] = max(score_match, gap_esquerda, gap_direita, score_mismatch)
            print(matriz)
    #Até aqui tudo ok, precisa ver como faz o backtracking e como fica caso tenha um gap na sequencia.
    
info = abreInput('input.txt')
smithWaterman(info['sequenciaUm'], info['sequenciaDois'], info['match'], info['mismatch'], info['gap'])
