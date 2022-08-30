print('Exercício 1')
# Faça um algoritmo que receba trÊs valores, representando os lados de um triângulo
# fornecidos pelo usuário. Verifique se os valores formam um triângulo e classifique como

# Equilátero (três lados iguais)
# Isóceles (dois lados iguais)
# Escaleno (três lados diferentes)

l1 = float(input('Digite a medida do lado 1 '))
l2 = float(input('Digite a medida do lado 2 '))
l3 = float(input('Digite a medida do lado 3 '))
isTriangle = False

if (l1 > 0 and l2 > 0 and l3 > 0) and (l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1):
    print('Pode ser um triângulo')
    isTriangle = True
else:
    print('Não pode ser um triângulo')

if isTriangle:
    if l1 == l2 and l1 == l3:
        print('É um triângulo equilátero')
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print('É um triângulo escaleno')
    else:
        print('É um triângulo isóceles')
