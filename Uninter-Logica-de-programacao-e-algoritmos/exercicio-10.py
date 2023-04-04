# Escreva um algoritmo que leia um valor e que imprima a quantidadde de céludas necessároas para pagar esses mesmo
# valor. Para simplificar, vamos trabalhar apenas com valores inteiros e com cédulas de R$100, 50, 20, 10, 5 e 1

value = int(input('Digite o valor que deseja sacar '))

while value > 0:
    if value >= 100:
        c100 = value // 100
        print('{} notas de 100 reais'.format(c100))
        value -= (c100 * 100)
        if not value:
            break
    if value >= 50:
        c50 = value // 50
        print('{} notas de 50 reais'.format(c50))
        value -= (c50 * 50)
        if not value:
            break
    if value >= 20:
        c20 = value // 20
        print('{} notas de 20 reais'.format(c20))
        value -= (c20 * 20)
        if not value:
            break
    if value >= 10:
        c10 = value // 10
        print('{} notas de 10 reais'.format(c10))
        value -= (c10 * 10)
        if not value:
            break
    if value >= 5:
        c5 = value // 5
        print('{} notas de 5 reais'.format(c5))
        value -= (c5 * 5)
        if not value:
            break
    if value >= 2:
        c2 = value // 2
        print('{} notas de 2 reais'.format(c2))
        value -= (c2 * 2)
        if not value:
            break
    if value >= 1:
        c1 = value
        print('{} notas de 1 real'.format(c1))
        value -= (c1 * 1)
