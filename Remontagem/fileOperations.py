class Arquivo:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.dados = self.abreArquivo(arquivo)
    
    def abreArquivo(self, nomeArquivo):
        with open(nomeArquivo, 'r', encoding='utf-8') as f:
            dados = f.read()
            sequencias = self.quebraEmLista(dados)
        return sequencias

    def quebraEmLista(self, dados):
        sequencias = dados.split(',')
        return sequencias

arquivo = Arquivo('Atividade_9.COMPUTACAO.PROVA.Vale 10.composicao_1_Bioinformaticas_size_30000_k_50.txt')
print(arquivo.dados)