class Arquivo:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.dados = self.abreArquivo()
    
    def abreArquivo(self):
        with open(self.arquivo, 'r', encoding='utf-8') as f:
            dados = f.read()
            sequencias = self.quebraEmLista(dados)
        return sequencias

    def quebraEmLista(self, dados):
        sequencias = dados.replace(' ', '').replace('\n', '').split(',')
        return sequencias