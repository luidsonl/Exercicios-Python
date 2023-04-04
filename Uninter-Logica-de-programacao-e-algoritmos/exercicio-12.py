# Escreva uma função que calcule o fatorial de um npuymero recebido como parâmetro e retorne o seu resultado
# Faça uma validação dos dados por meio de uma outtra função, permitindo que somente valores positivos sejam aceitos
# Crie o help da sua função

print('Exercício 1')


def validate(text, min, max):
    x = int(input(text))
    while (x < min) or (x > max):
        x = int(input(text))
    return x


def fatorial(num):
    """
    Retorna o fatorial de um número
    :param num:
    :return:
    """
    fat = 1
    if num == 0:
        return fat
    for i in range(1, num + 1, 1):
        fat *= i
    return fat


x = validate('Qual valor você deseja saber o fatorial? ', 0, 99)

print('O valor de {}! é {}.'.format(x, fatorial(x)))
