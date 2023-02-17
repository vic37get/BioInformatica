from no import *
from fileOperations import *
from no import *

sequencias = Arquivo('exemploAula.txt')
kmer = 3
grafo = {}

for sequencia in sequencias.dados:
    no = No(sequencia, kmer)
    grafo[no.prefixo] = []
    for 

print(grafo)
    