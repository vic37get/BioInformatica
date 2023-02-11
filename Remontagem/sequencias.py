def abreArquivo(nomeArquivo):
    with open(nomeArquivo, 'r', encoding='utf-8') as f:
        dados = f.read()
        sequencias = trataLeitura(dados)
    return sequencias

def trataLeitura(dados):
    sequencias = dados.split(',')
    return sequencias