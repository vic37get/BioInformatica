class No:
    def __init__(self, nome, kmer):
        self.sequencia = nome
        self.kmer = kmer - 1
        self.sufixo = None
        self.prefixo = None
        self.numConexoes = 0
        self.quebraEmKmer()
        
    def quebraEmKmer(self):
        kmers = []
        for indice in range(len(self.sequencia) - self.kmer+1):
            kmers.append(self.sequencia[indice:self.kmer+indice])
        self.prefixo = kmers[0]
        self.sufixo = kmers[1]
        return    