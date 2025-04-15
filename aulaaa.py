#max heap

#2o pai é maior que os filhos.
#2o arvore binária quase completa.

def SelectionSort(lista):
	for i in range(len(lista) -1, 0, -1):
		maior = 0
	for j in range(1, i+1):
		if lista[j] > lista[maior]:
			maior = j
	aux = lista[i]
	lista[i] = lista[maior]
	lista[maior] = aux
	
class MaxHeap:
	def __init__(self):
		self.dados = []
		self.tamanho = 0
		
	def sobe_heap(self, i):
		if i == 0:
			return
		pai = (i-1)  // 2
		if self.dados[i] > self.dados[pai]:
			self.dados[i], self.dados[pai] = self.dados[pai], self.dados[i]
			self.sobe_heap(pai)
		
	def inserir(self, valor):		
		self.dados.append(valor)
		self.tamanho += 1
		self.sobe_heap(self.tamanho - 1)
		
	def desce_heap(self, i):
		esq = 2*i+1
		dir	= 2*i+2
		maior = -1
		if esq <= self.tamanho - 1:
			maior = esq
		if dir <= self.tamanho - 1 and self.dados[dir] > self.dados[esq]:
			maior = dir
		if maior != -1 and self.dados[maior] > self.dados[i]:
			self.dados[i], self.dados[maior] = self.dados[maior], self.dados[i]
			self.desce_heap(maior)		
		
	def remover(self):
		if self.tamanho ==0:
			return None
		maximo = self.dados[0]
		self.dados[0] = self.dados[self.tamanho - 1]
		self.dados.pop()
		self.tamanho -= 1
		if self.tamanho > 0:
			self.desce_heap(0)
		return maximo
		
		
	def peek(self):
		return self.dados[0]		
		
	
H = MaxHeap()
H.inserir(33)
H.inserir(42)
print(H.dados)
H.inserir(18)
H.inserir(1)
print(H.dados)
H.inserir(6)
H.inserir(31)
print(H.dados)
print(H.remover())
print(H.dados)
print(H.remover())
print(H.dados)
print(H.remover())
print(H.dados)




















