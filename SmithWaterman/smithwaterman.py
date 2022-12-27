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

    #Olhar como ele percorre
    
    '''for i in range(matriz.shape[0]-1, -1, -1):
        for j in range(1, matriz.shape[1]):
            score_match, sequenciaUm_gap, sequenciaDois_gap = float('-inf'), float('-inf'), float('-inf')
            print(sequenciaUm[i - 1], sequenciaDois[j - 1])
            if sequenciaUm[i - 1] == sequenciaDois[j - 1]:
                score_match = matriz[i - 1][j - 1] + int(match)
                print('ScoreMatch: ', score_match)
                print(matriz)
            else:
                print('SequenciaUm_gap: ', matriz[i - 1][j])
                sequenciaUm_gap = matriz[i - 1][j] + int(gap)
                print('SequenciaDois_gap: ', matriz[i][j - 1])
                sequenciaDois_gap = matriz[i][j - 1] + int(gap)
                score_mismatch = matriz[i - 1][j - 1] + int(mismatch)
                print(matriz)
            matriz[i, j] = max(score_match, sequenciaUm_gap, sequenciaDois_gap, score_mismatch)
            print('Matriz alterada:')
            print(matriz)'''


info = abreInput('input.txt')
smithWaterman(info['sequenciaUm'], info['sequenciaDois'], info['match'], info['mismatch'], info['gap'])
