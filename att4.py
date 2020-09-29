from collections import deque
numerosPilha = deque([])
for i in range(0,10):
    numerosPilha.append(int(input('Digite um numero= ')))
for i in range(0,10):
    print(numerosPilha.pop())
