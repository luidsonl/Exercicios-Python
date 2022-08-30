# Desenvolva um algoritmo que solicite ao usuário o preço de um produto e percentual de desconto a ser aplicado a ele. Calcule e exiba o valor do desconto e o preço final do produto

price = float(input('Informe o preço do produto  '))
discount = float(input('Informe o percentual do desconto (0 - 100)  '))

discountValue = price * (discount / 100)
finalPrice = price - discountValue
print('O preço do produto é {} reais e o desconto é de {}%'.format(price, discount))
print('O valor do desconto é {} reais e o valor final do produto é {} reais'.format(discountValue, finalPrice))
