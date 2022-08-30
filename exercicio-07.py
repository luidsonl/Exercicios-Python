# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
# Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências,
# I para indústrias e C para comércios
print('Exercício 3')

kwh = float(input('Quantos kWh? '))
t = str(input('Qual o tipo de instalação? (r para residência, c para comércio, i para indústria) '))

if t == 'r':
    if kwh < 500:
        value = kwh * 0.40
        print('O valor é de {}R$ '.format(value))
    else:
        value = kwh * 0.65
        print('O valor é de {}R$ '.format(value))

elif t == 'c':
    if kwh < 1000:
        value = kwh * 0.55
        print('O valor é de {}R$ '.format(value))
    else:
        value = kwh * 0.60
        print('O valor é de {}R$ '.format(value))

elif t == 'i':
    if kwh < 5000:
        value = kwh * 0.55
        print('O valor é de {}R$ '.format(value))
    else:
        value = kwh * 0.60
        print('O valor é de {}R$ '.format(value))

else:
    print('Operação inválida')
