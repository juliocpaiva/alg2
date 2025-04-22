k = 8
A = [3,4,2,1,8,0]


C = [0 for _ in range(0,k+1)]

for a in A:
	C[a] +=1

for i in range(1, k+1):
	C[i] = C[i] + C[i-1]
print(C)

	
B = [None for _ in range(0, len(A))]


for a in A:
	#onde colcoa a?
	B[C[a] - 1] = a	


def CoutingSort(lista,k):
	B = [None for _ in range(0, len(A))]
	C = [0 for _ in range(0,k+1)]
	for a in A:
		C[a] +=1

	for i in range(1, k+1):
		C[i] = C[i] + C[i-1]
	print(C)
	for i in range(len(A)-1, -1):
		a = A[i]
		B[C[a] - 1] = a	
		C[a] -= 1
	return B	
	
A = [3,3,4,2,1,8,0,1]
print(A)
B = CoutingSort(A,8)
print(B)	

