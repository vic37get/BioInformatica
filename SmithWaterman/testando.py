from copy import deepcopy

lista = [1, -1, 0, 1]
lista2 = ['a', 'b', 'c', 'd']

def valoresIguais(lista, lista2):
    listaIguais = []
    listaIguais2 = []
    for indice, item in enumerate(lista):
        listaTeste = deepcopy(lista)
        valor = listaTeste[indice]
        del listaTeste[indice]
        if valor in listaTeste:
            listaIguais2.append(lista2[indice])
    return listaIguais2

iguais = valoresIguais(lista, lista2)
print(iguais)
