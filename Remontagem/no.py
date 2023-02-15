class No:
    def __init__(self, nome, kmer):
        self.sequencia = nome
        self.prefixo = None
        self.sufixo = None
        self.kmer = kmer
        
    def quebraEmKmer(self):
        kmers = []
        for indice in range(len(self.sequencia) - self.kmer+1):
            print(indice)
            kmers.append(self.sequencia[indice:self.kmer+indice])
        self.prefixo = kmers[0]
        self.sufixo = kmers[1]
        return 
no = No('ATG', 2)
print(no.quebraEmKmer())
print(no.prefixo)
print(no.sufixo)
            
        