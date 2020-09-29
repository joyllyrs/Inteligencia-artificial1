from queue import PriorityQueue

num = PriorityQueue()
num.empty()

num.put((5, 'prioridade maxima'))
num.put((1, 'prioridade baixa'))
num.put((3, 'prioridade media'))
num.put((4, 'prioridade qse maxima'))
num.put((2, 'prioridade qse media'))
num.put((5, 'prioridade maxima'))
num.put((1, 'prioridade baixa'))
num.put((3, 'prioridade media'))
num.put((4, 'prioridade qse maxima'))
num.put((2, 'prioridade qse media'))

num.empty()

for i in range(0,10):
    print(num.get())