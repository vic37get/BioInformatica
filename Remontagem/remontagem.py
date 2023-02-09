ls
# Importar as bibliotecas necessárias
from collections import defaultdict

# Definir a função de remontagem de genomas com k-mers
def genome_reassembly(reads, k):
    # Criar um dicionário vazio para armazenar os k-mers
    kmer_dict = defaultdict(list)
    
    # Loop para percorrer todos os reads
    for read in reads:
        # Loop para percorrer cada k-mer em um read
        for i in range(len(read) - k + 1):
            kmer = read[i:i+k]
            # Adicionar o read à lista de reads para esse k-mer
            kmer_dict[kmer].append(read)
    
    # Criar uma lista vazia para armazenar os k-mers iniciais
    start_kmers = []
    # Loop para percorrer todos os k-mers e identificar aqueles que são iniciais
    for kmer, reads in kmer_dict.items():
        # Se o número de reads para um k-mer é igual a 1, então é um k-mer inicial
        if len(reads) == 1:
            start_kmers.append(kmer)
    
    # Criar uma lista vazia para armazenar as assembleias
    assemblies = []
    # Loop para percorrer todos os k-mers iniciais e realizar a remontagem
    for start_kmer in start_kmers:
        # Criar uma variável para armazenar a assembleia atual
        assembly = start_kmer
        # Criar uma variável para armazenar o último k-mer utilizado
        last_kmer = start_kmer
        # Loop enquanto o próximo k-mer existir
        while True:
            # Obter a lista de reads que contêm o último k-mer
            reads = kmer_dict[last_kmer]
            # Se a lista tiver mais de 1 read, então o processo termina
            if len(reads) != 1:
                break
            # Obter o próximo k-mer
            next_kmer = reads[0][len(last_kmer):len(last_kmer)+k]
            # Adicionar o próximo k-mer à assembleia atual
            assembly += next_kmer
            # Atualizar o último k-mer utilizado
            last_kmer = next_kmer
        # Adicionar a assembleia atual à lista de assembleias
        assemblies.append(assembly)
    
    # Retornar a lista de assembleias
    return assemblies

# Testar a função de remontagem de genomas com k-mers
reads = ['ACTGATCGACTG', 'CTGATCGACTAG', 'TCGACTAGACTA']
k = 4

# Chamar a função de remontagem de genomas com k-mers
assemblies = genome_reassembly(reads, k)

# Imprimir o resultado
print('Assembléias:')
for assembly in assemblies:
    print(assembly)