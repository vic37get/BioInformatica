def readInput(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        fita = arquivo.read()
    return fita

def writeData(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(dados)

def tratamentoEntrada(entrada):
    entrada = entrada.strip().replace('\n', '')
    return entrada

def separaCodons(fita):
    nova_fita = []
    string_fita = ''
    for item in fita:
        string_fita = string_fita + item
        if len(string_fita) % 3 == 0:
            nova_fita.append(string_fita)
            string_fita = ''
    return nova_fita

def carregaDicionario():
    dicionario = {
        'UUU': 'F', 'UUC': 'F',
        'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
        'AUG': 'M',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'AGU': 'S', 'AGC': 'S',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'UAU': 'Y', 'UAC': 'Y',
        'UAA': 'ST', 'UAG': 'ST', 'UGA': 'ST',
        'CAU': 'H', 'CAC': 'H',
        'CAA': 'Q', 'CAG': 'Q',
        'AAU': 'N', 'AAC': 'N',
        'AAA': 'K', 'AAG': 'K',
        'GAU': 'D', 'GAC': 'D',
        'GAA': 'E', 'GAG': 'E',
        'UGU': 'C', 'UGC': 'C',
        'UGG': 'W',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    }
    return dicionario

def sintese():
    DICIONARIO = carregaDicionario()
    FITA = separaCodons(readInput('entrada.txt'))
    try:
        inicio = FITA.index('AUG')
        FITA = FITA[inicio:]
        print('Fita a ser processada: ', FITA)
        for codon in range(len(FITA)):
            FITA[codon] = FITA[codon].replace(FITA[codon], DICIONARIO[FITA[codon]])
            if FITA[codon].find('Stop') != -1:
                break
            
    except ValueError:
        print('Fita não contém Metionina (AUG)!')

    cadeiaAminoacidos = ['.'.join(FITA)]
    print('Cadeia de aminoácidos: ', cadeiaAminoacidos[0])
    writeData('saida.txt', cadeiaAminoacidos[0])
        
sintese()