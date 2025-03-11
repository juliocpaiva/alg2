#use j para representar parte imaginária de um numero...
c = 10 + 5j
print(type(c))

z = 0.000000000001
print(z)
print(bool(z))

z = z + 1
z = z - 1
print(z)
print(bool(z))


str1 = 'fagner acougueiro'
str2 = 'matheus perneta 10 '
str3 = """string com 
varias linhas"""

print(str2 * 10)

lista = [1,2,3,4]
lista2 = ["kj19", "bolasie"]
lista3 = [1, 'cabuloso', 2, 'campeao', lista2]

print(lista3)

def foo(x):
	x  = x + 1
	return
	
def foo2(l):
	l[0] = l[0]+1
	return	
x = 1
foo(x)
print(x)	

l=[1,2,3,4]
foo2(l)
print(l)
	
str1 = "FORA MARLON"
str2 = str1
print(str2)
print(id(str1))
print(id(str2))

str2 = str2.lower()
print(str1)
print(str2)

lista1 = ['b', 'a', 'n']
lista2 = lista1

lista2[0] = 'b'
print(lista1)
	
