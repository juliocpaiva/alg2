#divisão e conquista...

#divisão
#conquista
#combinação


def merge(lista1, lista2):
	lista = []
	i = 0
	j = 0
	
	while i < len(lista1) and j < len(lista2):
		if lista1[i] < lista2[j]:
			lista.append(lista1[i])
			i += 1
		else:
			lista.append(lista2[j])
			j +=1
			
	while i < len(lista1):
		lista.append(lista1[i])
		i +=1
		
	while j < len(lista2):
		lista.append(lista2[j])			
		j += 1
	return lista	
		
		
def mergesort(lista):

	if len(lista) <= 1:
		return lista
		
	meio = len(lista) // 2
	lista1 = mergesort(lista[:meio])
	lista2 = mergesort(lista[meio:])
	return merge (lista1, lista2)	
	
	
def quicksort(lista, esq, dir):	
	if esq < dir:
		p = partition(lista, esq, dir)
		quicksort(lista, esq, p-1)
		quicksort(lista, p+1, dir)
	
			
lista1 = [1, 18, 33, 42]		
lista2 = [2, 13, 45, 46]		

lista = merge(lista1, lista2)
print(lista)


lista = [18, 1, 33, 42, 16, 46, 2, 13]
lista = mergesort(lista)
print(lista)


# ---------- digão sort -------------- 03/04/2025 - 22h10
