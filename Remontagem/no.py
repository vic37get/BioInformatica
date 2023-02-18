class No:
    def __init__(self, nome):
        self.nome = nome
        self.qtdPrefixo = 0
        self.qtdSufixo = 0
        self.sufixos = []
        self.diferenca = self.qtdPrefixo - self.qtdSufixo
    
    def aumentaQtdPrefixos(self):
        self.qtdPrefixo += 1

    def aumentaQtdSufixos(self):
        self.qtdSufixo += 1

    def adicionaSufixo(self, sufixo):
        self.sufixos.append(sufixo)
    
    def exibeNo(self):
        print('Nome: {}\nQuantidade de prefixo: {}\nQuantidade de sufixo: {}\nLista de sufixos: {}'.format(self.nome, self.qtdPrefixo, self.qtdSufixo, self.sufixos))