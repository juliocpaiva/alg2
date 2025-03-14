lista1 = [1,2,3,4]

print(1 in lista1)
print(10 not in lista1)
print(2 in lista1)
print(20 in lista1)

lista2 = lista1 + [5,6,-7,-8]

print(lista2)
lista2[0] = 100
print(lista1)

lista2= lista1
lista3 = [1,2,3,4]

if lista2 == lista3:
	print('listas iguais')
else:	
	print('listas diferentes')
	
if lista2 is lista3:
	print('são o mesmo objeto')
else:
	print('são objetos distintos')	
	
if lista2 is lista1:
	print('é o mesmo')
else:
	print("não é o mesmo objeto...")	
	

x = 3
y = 3

if x is y:
	print('são o mesmo objeto')
else:
	print('são objetos distintos')	
	
str1 = 'hokama'
print(str1[0])
str1= str1[0].upper() + str1[1:]
print(str1)

lista2 = lista1 
print(lista1)
lista1.append(5)
#lista1.insert(0,-1)
print(lista1)

if lista2 is lista1:
	print('são o mesmo objeto')
else:
	print('são objetos distintos')	
	

lista2.extend([6,7,8])	
print(lista1)
	
	
#===== TUPLAS ======

tupla1 = (10,30,20)
tupla2 = ("hokama", 10)
tupla3 = ('hokama', 10)

print(id(tupla2))
print(id(tupla3))	
print(tupla2[1])	
#tupla2[1] = 20 NÃO PODE SER UTILIZADA...

print(tupla2[-1])
print(tupla1[1:])



valor = (10)
tupla4 = (10,)
tupla5 = ()
print(valor)
print(tupla4)
print(tupla5)

lista6 = [1,2]
lista6.extend((3,4,5))
print(lista6)


lista6.append((3,4,5))
print(lista6)
print(lista6[5])
lista6[5] = 87
print(lista6)


#len, min max
print(min([1,3,4,5,5.9,8.9]))
print(len(lista6))


tupla6 = (1,10) + (2,20)

print(tupla6)


tupla7= (1,2 ,[3,4])
print(id(tupla7))
tupla7[2].extend((5,6))
tupla7[2] = tupla7[2] + [7,8]
print(tupla7)





