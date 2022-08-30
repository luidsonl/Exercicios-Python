# Aluno : Luidson Lima Santos;
# --------------------------INÍCIO DO PROGRAMA---------------------------------------

print('Bem vindo a pizzaria do Luidson Lima Santos')

print('-' * 25 + 'Cardápio' + '-' * 25)
# Desenha o menu na tela do usuário
print('| Código |  Descrição  |Pizza Média - M |Pizza Grande -G |')
print('|   21   |  Napolitana |   20,00 R$     |   26,00 R$     |')
print('|   22   |  Margherita |   20,00 R$     |   26,00 R$     |')
print('|   23   |  Calabresa  |   25,00 R$     |   32,50 R$     |')
print('|   24   |  Toscana    |   30,00 R$     |   39,00 R$     |')
print('|   25   |  Portuguesa |   30,00 R$     |   39,00 R$     |')
# A variável 'total' vai armazenar o valor final a ser pago
total = 0
# Cria o menu com um loop "while"
while True:
    # Receberá o tamanho da pizza
    tamanho = input('Qual o tamanho da pizza que deseja? (M/G) ')
    if tamanho == 'M':
        incremento = 1
    # Caso o usuário escolha uma pizza tamanho G, essa será 30% mais cara
    elif tamanho == 'G':
        incremento = 1.3
    else:
        # Informará que a opção é invalida e voltará para o início do loop
        print('Opção inválida')
        continue
    while True:
        # Receberá o código referente ao sabor da pizza
        codigo = int(input('Entre com o código do sabor desejado'))
        # Atribui ao código 21 o valor de 20 R$
        if codigo == 21:
            # informa a pizza pedida
            print('Você pediu uma pizza Napolitana')
            # O "total" receberá o valor do sabor multiplicado pelo incremento referente ao tamanho
            total += 20 * incremento
            # Quebra o loop
            break
        # Atribui ao código 22 o valor de 20 R$
        if codigo == 22:
            # Informa a pizza pedida
            print('Você pediu uma pizza Margherita')
            # O "total" receberá o valor do sabor multiplicado pelo incremento referente ao tamanho
            total += 20 * incremento
            # Quebra o loop
            break
        # Atribui ao código 23 o valor de 25 R$
        elif codigo == 23:
            print('Você pediu uma pizza Calabresa')
            total += 25 * incremento
            break
        # Atribui ao código 24 o valor de 30 R$
        elif codigo == 24:
            print('Você pediu uma pizza Toscana')
            total += 30 * incremento
            break
        # Atribui ao código 25 o valor de 30 R$
        elif codigo == 25:
            print('Você pediu uma pizza Portuguesa')
            total += 30 * incremento
            break
        else:
            # Informa que o valor é inválido e retorna ao início do loop
            print('Opção inválida')
            continue
    # Pergunta se o usuário deseja realizar mais alguma operação
    print('Deseja mais alguma coisa?')
    print('1 - sim')
    print('0 - não')
    continuar = int(input(''))
    if continuar == 1:
        continue
    else:
        break
# Ao final informa o valor total a ser pago
print('O total a ser pago é {} R$'.format(total))
