print('Exercício 1')
# Escreva um algoritmo que leia os dois valores numéricos e que pergunte
# ao usuário qual operação ele deseja realizar: adição, subração, multiplicação, divisão
# e sair. Exiba na tela o resultado da operação desejada
# Repita até que a opção saída seja escolhida
# (exercício construído na aula 3)

print('Calculadora de 2 números')

add = '+'
sub = '-'
mult = '*'
div = '/'
stop = 'sair'

while True:

    print('Iniciando operação. Caso queira sair, digite (sair)')
    num1 = input('Informe o primeiro número. ')
    if num1 == stop:
        break

    print('Informe a operação desejada')
    op = input('Use (+) para adição, (-) para subtração, (*) para multiplicação e (/) para divisão')
    if op == stop:
        break

    num2 = input('informe o segundo número')
    if num2 == stop:
        break
    if op == add:
        res = float(num1) + float(num2)
        print('o resultado de {} + {} é igual a {}'.format(num1, num2, res))
    elif op == sub:
        res = float(num1) - float(num2)
        print('o resultado de {} - {} é igual a {}'.format(num1, num2, res))
    elif op == mult:
        res = float(num1) * float(num2)
        print('o resultado de {} X {} é igual a {}'.format(num1, num2, res))
    elif op == div:
        res = float(num1) / float(num2)
        print('o resultado de {} / {} é igual a {}'.format(num1, num2, res))
    else:
        print('Operação inválida')
print('Programa finalizado')
