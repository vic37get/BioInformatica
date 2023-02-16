from no import *
from fileOperations import *
from no import *

sequencias = Arquivo('exemploAula.txt')
kmer = 3
nos = []

for sequencia in sequencias.dados:
    no = No(sequencia, kmer)
    nos.append(no)

for i in nos:
    print(i.prefixo, i.sequencia, i.sufixo)    
    