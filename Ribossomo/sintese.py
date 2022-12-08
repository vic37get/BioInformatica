def readInput(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        fita = arquivo.read()
    return fita

def writeData(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(dados)

def tratamentoEntrada(entrada):
    entrada = entrada.strip().replace('\n', '')
    return entrada

def sintese():
    dados = readInput('entrada.txt')
    condicoes_parada = ['UAA', 'UAG', 'UGA']
    
    ...


sintese()