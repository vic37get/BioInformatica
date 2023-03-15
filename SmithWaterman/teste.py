file = open("input.txt", "r") #lê arquivo | read file 

save_data = [] #cria lista | create list

for i in file:  #salva os dados na lista | save the data in the list 
    save_data.append(i.split("\n")[0]) #[primeira sequencia, segunda sequencia, match, missmatch gap] | [first sequence, second sequence, match, missmatch gap] 
 
def criaMatriz(seq1, seq2): #funcao que cria a matriz | function that creates the array
    matriz = [] #cria uma lista vazia | create an empty list
    seq1 = seq1[::-1] #inverte a 1ª sequencia | reverse the 1st sequence
    for i in seq1: 
        templist = [i] #adiciona a primera letra da sequencia em uma lista (lembre que a sequecia foi invertida) | adds the first letter of the sequence to a list (remember the sequence is inverted)
        [templist.append(None) for j in range(0,len(seq2)+1)] #preenche o resto da lista com valores nulos | fills the rest of the list with null values
        matriz.append(templist) #adicione a linha na matriz | add the row in the matrix
    templist = ["-"] #adiciona casa vazia representada por - | add empty square represented by -
    [templist.append(None) for j in range(0,len(seq2)+1)] #preenche o resto da lista com valores nulos | fills the rest of the list with null values
    matriz.append(templist) #adicione a linha na matriz | add the row in the matrix
    templist = ["start", "-"] #adiciona a ultima linha da matriz que começa com start e casa vazia | adds the last line of the matrix that starts with start and empty box
    [templist.append(i) for i in seq2] #preenche o resto da lista com a segunda sequencia | fills the rest of the list with the second sequence
    matriz.append(templist) #adiciona a ultima linha na matriz | add the last row to the matrix
    return [matriz, len(seq1)+2, len(seq2)+2] #retorna o esqueleto da matriz, numero de linhas e numero de colunas | returns the skeleton of the matrix, number of rows and number of column

matriz = criaMatriz(save_data[0], save_data[1]) #salva a matriz | save the matrix

def inicializaMatriz(matriz, gapValue): #inicializa a matriz com os gaps horizontal e vertical | initializes the matrix with the horizontal and vertical gaps
    nLin = int(matriz[1]) #salva numero de linhas da matriz | save number of rows in matrix
    nCol = int(matriz[2]) #salva numero de colunas da matriz | save number of column in matrix
    matriz = matriz[0] #salva a matriz | save the matrix
    matriz[-2][1] = [0, '','', 'stop'] #salva a casa inicial 0 score e coordenadas nulas (stop serve para facilitar o traceback) | saves the initial square 0 score and null coordinates (stop serves to facilitate the traceback)
    for i in range(nLin-3, -1,-1):
        matriz[i][1] = [int(matriz[i+1][1][0]) + int(gapValue), i+1, 1, "baixo"] #inicializa os gaps verticais com score, casa anterior (linha, coluna) e posição da casa anterior | initialize vertical gaps with score, previous square (row, column) and previous square position
    for i in range(2, nCol, 1):
        matriz[-2][i] = [int(matriz[-2][i-1][0]) + int(gapValue), nLin-2, i-1, "esq"] #inicializa os gaps horizontais | initialize the horizontal gaps
    return (matriz, nLin, nCol) #retorna a matriz, numero de linhas e numero de colunas | returns the matrix, number of rows and number of columns

#baixo = under | esq = left | diag = diagonal

inicializaMatriz(matriz, save_data[-1]) #usa a funcao anterior | use the previous function

def calculaCasa(matriz, match, missmatch, gap, posLin, posCol):
    diag = None
    if(matriz[posLin][0][0] == matriz[-1][posCol][0]):
        diag = matriz[posLin+1][posCol-1][0] + match
    else:
        diag = matriz[posLin+1][posCol-1][0] + missmatch
    maior = [diag, posLin+1, posCol-1, "diag"] 

    esq = matriz[posLin][posCol-1][0] + gap

    if(esq > maior[0]):
        maior = [esq, posLin, posCol-1, "esq"] 
    baixo = matriz[posLin+1][posCol][0] + gap
    if(baixo>maior[0]):
        maior = [baixo, posLin+1, posCol, "baixo"] 
    return maior


for i in range(matriz[1]-3, -1, -1):
    for j in range(2, matriz[2], 1):
        matriz[0][i][j] = calculaCasa(matriz[0], int(save_data[2]), int(save_data[3]), int(save_data[4]), i, j)

def findScore(matriz, nLin, nCol):
    score = matriz[0][1][0]
    for i in range(2, nCol):
        if(matriz[0][i][0]>score):
            score = matriz[0][i][0]
    for i in range(1, nLin-1):
        if(matriz[i][-1][0]>score):
            score = matriz[i][-1][0]
    return score

scoreFinal = findScore(matriz[0], matriz[1], matriz[2])

def backTrace(matriz, nLin, nCol):
    #with open('matriz2.txt', 'w') as f:
        #f.write()
    print(matriz)
    colIni = nCol-1
    linIni = 0
    primSeq = []
    segSeq = []
    while(True):
        if(matriz[linIni][colIni][-1] == "diag"):
            primSeq.append(matriz[linIni][0])
            segSeq.append(matriz[nLin-1][colIni])
        elif(matriz[linIni][colIni][-1] == "baixo"):
            primSeq.append(matriz[linIni][0])
            segSeq.append("-")
        else:
            primSeq.append("-")
            segSeq.append(matriz[nLin-1][colIni])
       
        newCol = matriz[linIni][colIni][-2]
        newLin = matriz[linIni][colIni][-3]
        colIni = newCol
        linIni = newLin
        if(matriz[linIni][colIni][-1] == 'stop'):
            break

    seq1 = ''.join(primSeq[::-1])
    seq2 = ''.join(segSeq[::-1])

    return [seq1, seq2]

seq1Final, seq2Final = backTrace(matriz[0], matriz[1], matriz[2])


with open("output.txt", 'w') as file:
    file.writelines([str(seq1Final)+'\n', str(seq2Final)+'\n', str(scoreFinal)+'\n', str(save_data[2])+'\n', str(save_data[3])+'\n', str(save_data[4])])