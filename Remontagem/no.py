class No:
    def __init__(self, nome):
        self.nome = nome
        self.qtdPrefixo = 0
        self.qtdSufixo = 0
        self.diferenca = 0
        self.sufixos = []
    
    def aumentaQtdPrefixos(self):
        self.qtdPrefixo += 1
        self.diferenca = self.qtdPrefixo - self.qtdSufixo

    def aumentaQtdSufixos(self):
        self.qtdSufixo += 1
        self.diferenca = self.qtdPrefixo - self.qtdSufixo

    def adicionaSufixo(self, sufixo):
        self.sufixos.append(sufixo)
    
    def exibeNo(self):
        print('Nome: {}\nQuantidade de prefixo: {}\nQuantidade de sufixo: {}\nLista de sufixos: {}\nDiferença: {}'.format(self.nome, self.qtdPrefixo, self.qtdSufixo, self.sufixos, self.diferenca))