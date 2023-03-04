class Grafo:
    def __init__(self):
        self.grafo = {}

    def pesquisaChave(self, chave):
        if self.grafo.get(chave):
            return True
        else:
            return False

    def adicionaNoGrafo(self, chave, valor):
        if self.pesquisaChave(chave) != True:
            self.grafo[chave] = valor
            return True
        else:
            return False

    def removeDoGrafo(self,  chave):
        del self.grafo[chave]