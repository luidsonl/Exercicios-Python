# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. calcule o preço a pagar sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
print('O carro custa R$ 60 por dia e R$ 0,15 por km rodado.')
km = int(input('Quantos kilometros você percorreu?  '))
days = int(input('Quantos dias você ficou com o carro?'))
fee = (60 * days) + (0.15 * km)
print('Seu custo é de {} R$'.format(fee))
