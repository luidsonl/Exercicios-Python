print('Exercício 2')
# Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual
# operação ele deseja realizar: adição (+), subtração (-), multiplicação (*) ou divisão (/).
# Exiba na tela o resultado da operação desejada

print('Calculadora de 2 números')

add = 1
sub = 2
mult = 3
div = 4

num1 = float(input('Informe o primeiro número '))

print('Informe a operação desejada')
op = int(input('Use 1 para adição, 2 para subtração, 3 para multiplicação e 4 para divisão '))

num2 = float(input('informe o segundo número'))

if op == add:
    res = num1 + num2
    print('o resultado de {} + {} é igual a {}'.format(num1, num2, res))
elif op == sub:
    res = num1 - num2
    print('o resultado de {} - {} é igual a {}'.format(num1, num2, res))
elif op == mult:
    res = num1 * num2
    print('o resultado de {} X {} é igual a {}'.format(num1, num2, res))
elif op == div:
    res = num1 / num2
    print('o resultado de {} / {} é igual a {}'.format(num1, num2, res))
else:
    print('Operação inválida')
