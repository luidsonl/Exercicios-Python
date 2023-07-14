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
        c = self.nodes

        while True:
            # se a árvore ter apenas 1 nó
            if c == 1:
                break

            p = c // 2

            if self.heap[p - 1] >= self.heap[c-1]:
                break
            else:
                self.heap[p - 1], self.heap[c-1] = self.heap[c-1], self.heap[p - 1]
                c = p

    def remove_node(self):
        #Armazena o valor do primeiro nó(maior valor)
        root = self.heap[0]
        #Atribui o valor do último nó ao primeiro
        self.heap[0] = self.heap[self.nodes - 1]
        # Remove o último elemento
        self.heap.pop()
        # Decrementa 1 da quantidade de nós
        self.nodes -=1

        p = 1

        while True:
            c = p * 2 #child = parent * 2
            if c > self.nodes: #filho a esquerda não existe
                break
            if c + 1 <= self.nodes: #se o filho a direita existir
                if self.heap[c] > self.heap[c - 1]: 
                    # se o filho da direita for maior que o da esquerda
                    c += 1
                    # o filho passa a ser o da direita
            if self.heap[p - 1]>= self.heap[c - 1]:
                break
            else:
                self.heap[p - 1], self.heap[c - 1] = self.heap[c - 1], self.heap[p - 1]
                p = c
        return root
        
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
        print(' ')

    def length(self):
        return self.nodes
    
    def root(self):
        if self.nodes == 0:
            return None
        
        return self.heap[0]
    
    def get_node(self, i):
        return self.heap[i-1]
        
    def chid_on_left(self, i):
        if self.nodes < 2 * i - 1:
            return None
        
        return self.heap[2 * i - 1]
    
    def child_on_right(self, i):
        if self.nodes < 2 * i - 1:
            return None
        
        return self.heap[2 * i]

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
h.remove_node()

h.show()
print('Tamanho do heap:', h.length())
print('Valor do nó raiz:', h.root())
print('Valor do terceiro nó:', h.get_node(3))
print('Filho a esquerda do 25:', h.chid_on_left(3))
print('Filho a direita do 25:', h.child_on_right(3))
