# Um cinema cobra preços diferentes para os ingressos de acordo com a idade de uma pessoa
# se a pessoa tiver menos de 3 anos de idade, o ingresso será gratuito, se tiver entre 3 e 12 anosm o
# ingresso custará R$15, se tiver mais dde 12 anos, custará R& 30

count = 0
total = 0
sumAge = 0

while True:
    age = input('Informe a idade da pessoa. Digite (pronto) para finalizar operação ')
    if age == 'pronto':
        break
    age = int(age)
    sumAge += age
    if age <= 3:
        count += 1
    elif age < 3 and age <= 12:
        count += 1
        total += 15
    elif age > 12:
        count += 1
        total += 30
    else:
        print('Valor inválido')

# Após encerrar o laço, apresente na tela o total de pessoas que compraram ingressos,
# o total de dinheiro arrecadado e a média de idade das pessoas

print('{} pessoas compraram o ingresso'.format(count))
print('A média de idade é de {} anos'.format(sumAge/count))
print('O total de dinheiro arrecadado foi de {} R$'.format(total))
print('Cada pessoa pagou em média {} R$'.format(total/count))
