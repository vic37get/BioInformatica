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
            'match': dados[2],
            'mismatch': dados[3],
            'gap': dados[4],
    }
    return info

def smithWaterman(sequenciaUm, sequenciaDois, match, mismatch, gap):
    matriz = np.zeros((len(sequenciaUm) + 1, len(sequenciaDois) + 1))
    for i in range(1, matriz.shape[0]):
        for j in range(1, matriz.shape[1]):
            score_match, score_gap, score_gap_insert = float('-inf'), float('-inf'), float('-inf')
            if sequenciaUm[i - 1] == sequenciaDois[j - 1]:
                score_match = matriz[i - 1][j - 1] + int(match)
            else:
                score_gap = matriz[i - 1][j] + int(gap)
                print('foi gap!')
                score_gap_insert = matriz[i][j - 1] + int(gap)
            print(sequenciaUm[i - 1], sequenciaDois[j - 1])
            matriz[i, j] = max(score_match, score_gap, score_gap_insert)
            print(matriz)


info = abreInput('input.txt')
smithWaterman(info['sequenciaUm'], info['sequenciaDois'], info['match'], info['mismatch'], info['gap'])
