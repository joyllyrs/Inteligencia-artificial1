from collections import deque
numerosFila = deque([])
for i in range(0,10):
    numerosFila.append(int(input('Digite um numero')))
for i in range(0,10):
    print(numerosFila.popleft())