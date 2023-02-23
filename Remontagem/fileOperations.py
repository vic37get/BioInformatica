class Arquivo:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.dados = None
        self.kmer = None
    
    def abreArquivo(self):
        with open(self.arquivo, 'r', encoding='utf-8') as f:
            dados = f.read()
            sequencias = self.quebraEmLista(dados)
        return sequencias

    def quebraEmLista(self, dados):
        sequencias = dados.replace(' ', '').replace('\n', '').split(',')
        self.kmer = len(sequencias[0])
        if sequencias[-1]:
            return sequencias
        else:
            return sequencias[:-1]
    
    def escreveArquivo(self, dados):
        with open(self.arquivo, 'w', encoding='utf-8') as f:
            f.write(dados)