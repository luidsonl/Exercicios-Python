# Realize uma sequência de print com for e whlie:
# A - inteiros de 3 até 12 com 12 incluso
# B - inteiros de 0 até 9, excluindo 9, com passo de 2

print('Usando for')
print('Inteiros de 3 até 12 com 12 incluso')
for i in range(3, 13, 1):
    print(i)

print('Inteiros de 0 até 9, excluindo 9, com passo de 2')
for i in range(0, 9, 2):
    print(i)

print('usando while')

print('Inteiros de 3 até 12 com 12 incluso')
i = 3
while i <= 12:
    print(i)
    i += 1

print('Inteiros de 0 até 9, excluindo 9, com passo de 2')
i = 0
while i < 9:
    print(i)
    i += 2
