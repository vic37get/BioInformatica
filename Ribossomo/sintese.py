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
        'UUU': 'Phe', 'UUC': 'Phe',
        'UUA': 'Leu', 'UUG': 'Leu', 'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
        'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile',
        'AUG': 'Met',
        'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
        'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser', 'AGU': 'Ser', 'AGC': 'Ser',
        'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
        'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
        'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
        'UAU': 'Tyr', 'UAC': 'Tyr',
        'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop',
        'CAU': 'His', 'CAC': 'His',
        'CAA': 'Gln', 'CAG': 'Gln',
        'AAU': 'Asn', 'AAC': 'Asn',
        'AAA': 'Lys', 'AAG': 'Lys',
        'GAU': 'Asp', 'GAC': 'Asp',
        'GAA': 'Glu', 'GAG': 'Glu',
        'UGU': 'Cys', 'UGC': 'Cys',
        'UGG': 'Trp',
        'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg', 'AGA': 'Arg', 'AGG': 'Arg',
        'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly',
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
            elif codon == len(FITA)-1:
                print('Fita não contém codon de parada! (UGA, UUA, UAG)')
                return
    except ValueError:
        print('Fita não contém Metionina (AUG)!')

    cadeiaAminoacidos = ['.'.join(FITA)]
    print('Cadeia de aminoácidos: ', cadeiaAminoacidos[0])
    writeData('saida.txt', cadeiaAminoacidos[0])
        
sintese()