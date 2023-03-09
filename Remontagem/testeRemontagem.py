
def abreArquivo(filename):
    with open(filename, 'r') as f:
        dados = f.read()
    return dados

def inicialFinalFita(fita, k):
    inicial = fita[:k-1]
    final = fita[(len(fita)-k+1):]
    return inicial, final

def testeSaida(inicial, final, fita, k):
    resposta = abreArquivo('Saidas/resposta.txt')
    saida = abreArquivo('Saidas/saida.txt')
    inicialfita, finalfita = inicialFinalFita(fita, k)
    if (sorted(resposta) == sorted(saida)):
        print('MESMAS BASES!')
        if (inicial.nome == inicialfita and final.nome == finalfita):
            print('\nCORRETO!\n')
            print('Comparação:\n{}\n{}'.format(resposta, saida))
            print('Resposta: {}'.format(sorted(resposta)))
            print('Saida: {}'.format(sorted(saida)))
        else:
            print('\nERRADO!\n')
            print('Comparação:\n{}\n{}'.format(resposta, saida))
            print('Resposta: {}'.format(sorted(resposta)))
            print('Saida: {}'.format(sorted(saida)))
    else:
        print('As bases não são iguais!')
        print('Comparação:\n{}\n{}'.format(resposta, saida))
        print('Resposta: {}'.format(sorted(resposta)))
        print('Saida: {}'.format(sorted(saida)))