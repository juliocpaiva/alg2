from random import randint
import sys


def merge(listaA, listaB):
    lista = []
    i = 0
    j = 0
    while i < len(listaA) and j < len(listaB):
        if listaA[i] < listaB[j]:
            lista.append(listaA[i])
            i += 1
        else:
            lista.append(listaB[j])
            j += 1
    
    while i < len(listaA):
        lista.append(listaA[i])
        i += 1
    
    while j < len(listaB):
        lista.append(listaB[j])
        j += 1
    return lista
    


def mergesort(lista):
    if len(lista) <= 1:
        return lista
    
    meio = len(lista) // 2    
    listaA = mergesort(lista[:meio])
    listaB = mergesort(lista[meio:])
    return merge(listaA, listaB)


def partition(lista, esq, dir):
    r = randint(esq,dir)
    aux = lista[r]
    lista[r] = lista[esq]
    lista[esq] = aux
    j = esq
    pivot = lista[dir]  # Mudando para pegar o último elemento como pivô
    for k in range(esq, dir):
        if lista[k] < pivot:
            lista[j], lista[k] = lista[k], lista[j]
            j += 1
    lista[j], lista[dir] = lista[dir], lista[j]  # Coloca o pivô no lugar correto
    return j


def quicksort(lista, esq, dir):
    if esq < dir:
        p = partition(lista, esq, dir)
        quicksort(lista, esq, p - 1)
        quicksort(lista, p + 1, dir)


# Teste de merge
listaA = [1, 18, 33, 42]
listaB = [2, 13, 16, 46]
lista = merge(listaA, listaB)
print("Merged List:", lista)

# Teste de quicksort
sys.setrecursionlimit(10000)
lista = list(range(0, 10000))
quicksort(lista, 0, len(lista) - 1)

print(lista)
#teorema... para qualquer entrada o tempo esperado de execução do quick sort
# é o(n log n)...
