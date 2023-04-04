import math
# declara classe
class HeapMax:
    #cria construtor
    def __init__(self):
        self.nodes = 0
        self.heap =[]
    
    #Cria método de adição
    def add_node(self, u):
        self.nodes += 1
        self.heap.append(u)
        child = self.nodes

        while True:
            # se a árvore ter apenas 1 nó
            if child == 1:
                break

            parent = child // 2

            if self.heap[parent - 1] >= self.heap[child-1]:
                break
            else:
                self.heap[parent - 1], self.heap[child-1] = self.heap[child-1], self.heap[parent - 1]
                child = parent
        
    #método de exibicão
    def show(self):
        #pega o nível da árvore calculando o logaritmo do numero de nodes na base 2
        level = int(math.log(self.nodes,2))
        # position representa a posição no array heap
        position = 0
        #Cada i representa um nível
        for i in range(level):
            #cada j representa uma posição do nível
            for j in range(2**i):
                print(f'{self.heap[position]}', end = ' ')
                position += 1
            print('')

        # percorre os elementos da última linha
        for i in range(self.nodes - position):
            print(f'{self.heap[position]}', end = ' ')
            position += 1

h = HeapMax()
h.add_node(17)
h.add_node(36)
h.add_node(25)
h.add_node(7)
h.add_node(3)
h.add_node(100)
h.add_node(1)
h.add_node(2)
h.add_node(19)
h.show()