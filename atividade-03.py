# Aluno: Luidson Lima Santos;
# --------------------------INÍCIO DO PROGRAMA---------------------------------------
# --------------Inicio da função volumeFeijoada--------------------------
def volumeFeijoada():
    print('-'*10 + 'Menu de seleção do volume de feijoada' + '-'*10)
    # Cria o loop
    while True:
        # Testa a ocorrência de erros de valores com o "try"
        try:
            # Cria a variável "volume" que receberá um falor float para a quantidade de feijoada desejada
            volume = float(input('Entre com a quantidade que deseja (ml):'))
            # Testa se o volume de feijoada é menor que 300ml ou maior que 5000ml.
            # Se verdade, retorna uma mensagem e reinicia o loop
            if volume < 300 or volume > 5000:
                print('Não aceitamos porções menores que 300ml ou maiores que 5000ml. Tente novamente')
                continue
            # caso a condição anterior seja falsa, irá retornar o volume * 0,08
            else:
                return volume * 0.08
        # Casos seja inserido algum formato inválido de valor, irá reiniciar o loop e exibir a mensagem
        except ValueError:
            print('Você não informou um número. Tente novamente')
            continue


# --------------Fim da função volumeFeijoada---------------------------
# --------------Inicio da função opcaoFeijoada--------------------------
def opcaoFeijoada():
    print('-'*10 + 'Menu de seleção de opção' + '-'*10)
    # Cria o loop
    while True:
        # Imprime as opções disponíveis
        print('Entre com a opção de feijoada')
        print('b - Básica (Feijão + paiol + costelinha)')
        print('p - Premium (Feijão + paiol + costelinha + partes de porco)')
        print('s - Suprema (Feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon)')
        # Recebe a opção informada e armazena na variável "escolha", de formato string
        escolha = str(input(''))
        # Testa se a variável é igual a "b", caso seja, retorna 1
        if escolha == 'b':
            return 1
        # Testa se a variável é igual a "p", caso seja, retorna 1.25
        elif escolha == 'p':
            return 1.25
        # Testa se a variável é igual a "s", caso seja, retorna 1.5
        elif escolha == 's':
            return 1.5
        # Caso o usuário informe um valor inválido, é exibida uma mensagem de erro e o loop é reiniciado
        else:
            print('Você não digitou uma opção válida')
            continue


# --------------Fim da função opcaoFeijoada---------------------------------
# -------------- Início da função acompanhamentoFeijoada---------------------
def acompanhamentoFeijoada():
    print('-' * 10 + 'Deseja mais algum acompanhamento?' + '-' * 10)
    # Cria a variável "acompanhamento" com valor 0, que será incrementada pelo valor do acompanhamento
    acompanhamento = 0
    # Cria o loop
    while True:
        # Testa a ocorrência de erros de valores com o "try"
        try:
            print('0- Não desejo mais acompanhamentos (encerrar pedido)')
            print('1- 200g de arroz')
            print('2- 150g de farofa especial')
            print('3- 100g de couve cozida')
            print('4- 1 laranja descascada')
            escolha = int(input())
            # Testa se o valor da escolha é igual a 0
            if escolha == 0:
                # Encerra o loop
                break
            # Testa se o valor da escolha é igual a 1
            elif escolha == 1:
                acompanhamento += 5
                # Incrementa 5 à variável "acompanhamento" e reinicia o loop
                continue
            # Testa se o valor da escolha é igual a 2
            elif escolha == 2:
                # Incrementa 6 à variável "acompanhamento" e reinicia o loop
                acompanhamento += 6
                continue
            # Testa se o valor da escolha é igual a 3
            elif escolha == 3:
                # Incrementa 7 à variável "acompanhamento" e reinicia o loop
                acompanhamento += 7
                continue
            # Testa se o valor da escolha é igual a 4
            elif escolha == 4:
                # Incrementa 3 à variável "acompanhamento" e reinicia o loop
                acompanhamento += 3
                continue
            # Informa que a opção informada inválida e reinicia o loop
            else:
                print('Você não digitou uma opção válida')
                continue
        # Caso seja inserido algum formato inválido, irá reiniciar o loop e exibir a mensagem de erro
        except ValueError:
            print('Você não informou um número. Tente novamente')
            continue
    # Após encerrar o loop retorna o valor do acompanhamento
    return acompanhamento


# --------------Fim da função acompanhamentoFeijoada-------------
# --------------Início da função main----------------------------
print('Bem vindo ao programa de feijoada do Luidson Lima Santos')

# Definiŕa uma variável para o resultado de cada função
vFeijoada = volumeFeijoada()
oFeijoada = opcaoFeijoada()
aFeijoada = acompanhamentoFeijoada()
# Definirá uma variável com o valor total
total = vFeijoada * oFeijoada + aFeijoada
print('O valor a ser pago é {} R$ (volume = {} R$ * opcao = {} + acompanhamento = {} R$)'.format(total, vFeijoada, oFeijoada, aFeijoada))
# --------------Fim da função main----------------------------------
