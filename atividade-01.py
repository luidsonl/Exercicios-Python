# Aluno : Luidson Lima Santos;
# --------------------------INÍCIO DO PROGRAMA---------------------------------------
print('Bem vindo a loja de Luidson Lima Santos')

# Recebe o valor do produto desejado e salva um valor float na variável 'valor'
valor = float(input('Informe o valor do produto '))
# Recebe a quantidade do produto e salva um valor int na variável 'quantidade'
quantidade = int(input('informe a quantidade que deseja comprar '))
# verifica se a quantidade de produtos é menor ou igual a quatro e se é maior que zero
if 0 < quantidade <= 4:
    # Define o valor da compra sem o desconto
    valorSemDesconto = valor * quantidade
    # Define o valor do desconto
    desconto = valorSemDesconto * 0
    # Define o valor com o desconto ao retirar o valor do desconto do valor inicial da compra
    valorComDesconto = valorSemDesconto - desconto
    # Retorna o valor sem o desconto
    print('O valor sem desconto foi {} R$'.format(valorSemDesconto))
    # Retorna o valor com o desconto e informa o percentual que foi descontado
    print('O valor com desconto foi {} R$        desconto de 0%'.format(valorComDesconto))
# Verifica se a quantidade de produtos é maior que 4 e menor ou igual a 19 e faz novamente o processo anterior, mas com
# Os valores relativos ao desconto de 3%
elif 4 < quantidade <= 19:
    valorSemDesconto = valor * quantidade
    desconto = valorSemDesconto * 0.03
    valorComDesconto = valorSemDesconto - desconto
    print('O valor sem desconto foi {} R$'.format(valorSemDesconto))
    print('O valor com desconto foi {} R$        (desconto de 3%)'.format(valorComDesconto))
# Verifica se a quantidade de produtos é maior que 19 e menor ou igual a 99 e faz novamente o processo anterior, mas com
# Os valores relativos ao desconto de 6%
elif 19 < quantidade <= 99:
    valorSemDesconto = valor * quantidade
    desconto = valorSemDesconto * 0.06
    valorComDesconto = valorSemDesconto - desconto
    print('O valor sem desconto foi {} R$'.format(valorSemDesconto))
    print('O valor com desconto foi {} R$        desconto de 6%'.format(valorComDesconto))
# Verifica se a quantidade de produtos é maior que 19 e faz novamente o processo anterior, mas com
# os valores relativos ao desconto de 10%
elif quantidade > 99:
    valorSemDesconto = valor * quantidade
    desconto = valorSemDesconto * 0.1
    valorComDesconto = valorSemDesconto - desconto
    print('O valor sem desconto foi {} R$'.format(valorSemDesconto))
    print('O valor com desconto foi {} R$        desconto de 10%'.format(valorComDesconto))
# Encerra o programa caso o usuário informe uma quantidade negativa de produtos
else:
    print('Quantidade inválida ! Encerrando programa!')
