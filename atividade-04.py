# Aluno: Luidson Lima Santos;
# --------------------------INÍCIO DO PROGRAMA---------------------------------------
# Declara uma lista vazia que irá conter os produtos cadastrados
listaProdutos = []
# Cria variável "registroProduto" que irá armazenar o registro do produto
registroProduto = 0
# --------Começo da função cadastrarProduto-----------------
def cadastrarProduto(codigo):
    print('-' * 15 + 'Cadastrar Produto' + '-' * 15)
    print('O codigo do produto é {}'.format(codigo))
    # Recebe os valores do usuário
    nome = input('Informe o nome do produto ')
    fabricante = input('Informe o fabricante do produto ')
    valor = float(input('Informe o valor do produto (R$) '))
    # Adiciona os valores informados em um dicionário
    dicionarioProduto = {
        'codigo': codigo,
        'nome': nome,
        'fabricante': fabricante,
        'valor': valor
    }
    # Adiciona uma cópia do dicionário dentro do array "listaProdutos"
    listaProdutos.append(dicionarioProduto.copy())


# --------fim da  funçao cadastrarProduto---------------------
# --------Começo da funçao consultarProduto-----------------------
def consultarProduto():
    # Cria um loop
    while True:
        print('-' * 15 + 'Consultar Produto' + '-' * 15)
        # Exibe as opções de consulta
        print('Use os comandos a seguir\n'
              '1 - para consultar todos os produtos\n'
              '2 - para consultar produto pelo código\n'
              '3 - para consultar produto pelo fabricante\n'
              '4 - para retornar')
        # Testa se há algum erro no formato da entrada
        try:
            opConsultar = int(input('>>'))
            # Testa se a opção escolhida é igual a um
            if opConsultar == 1:
                # Executa a exibição de todos os produtos
                print('-' * 15 + 'Consultar Todos' + '-' * 15)
                # Cria um loop para cada produto da lista
                for produto in listaProdutos:
                    # Cria um loop para cada iten do dicionário do produto
                    for key, value in produto.items():
                        # Imprime os valores das chaves e dos elementos
                        print('{}: {}'.format(key, value))
            # Testa se a opção escolhida é igual a 2
            elif opConsultar == 2:
                print('-' * 15 + 'Consultar pelo Código' + '-' * 15)
                # Recebe o codigo do produto e armazena na variável "entrada"
                entrada = int(input('Informe o código do produto'))
                # Cria um loop para verificar a lista de produtos
                for produto in listaProdutos:
                    # Testa se a chave código é igual a variável entrada
                    if produto['codigo'] == entrada:
                        # Caso seja, inicia um loop com os itens do dicionário
                        for key, value in produto.items():
                            # Exibe a chave e o seu valor
                            print('{}: {}'.format(key, value))
            # Testa se a opçãp escolhida é igual a 3
            elif opConsultar == 3:
                print('-' * 15 + 'Consultar pelo Fabricante' + '-' * 15)
                # Recebe o nome da fabricante e armazena na variável "entrada"
                entrada = input('Informe o fabricante do produto')
                # Cria um loop para verificar a lista de produtos
                for produto in listaProdutos:
                    # Testa se a chave "fabricante" tem valor igual a entrada
                    if produto['fabricante'] == entrada:
                        # Caso seja, inicia um loop com os itens do dicionário
                        for key, value in produto.items():
                            # Exibe a chave e o seu valor
                            print('{}: {}'.format(key, value))
            # Verifica se o valor informado é igual a 4
            elif opConsultar == 4:
                # Encerra o loop
                break
            # Caso o usuário informe um valor que não consta na lista de opções, exibe mensagem de valor inválido
            else:
                print('Valor inválido')
        # Se ocorrer erro no formato da entrada, é exibida uma mensagem de erro e o loop é reiniciado
        except ValueError:
            print('Formato inválido')
            continue


# --------Fim da funçao consultarProduto-------------------
# --------Começo da funçao removerProduto-----------------
def removerProduto():
    print('-' * 15 + 'Remover Produto' + '-' * 15)
    # Recebe o valor do código do produto a ser removido e armazena na variável entrada
    entrada = int(input('Digite o código do produto que deseja remover '))
    # Cria um loop para verificar os produtos da lista
    for produto in listaProdutos:
        # Testa se a chave "codigo" do dicionário do produto é igual a entrada
        if produto['codigo'] == entrada:
            # Se verdade, remove o produto da lista
            listaProdutos.remove(produto)


# --------Fim da funçao removerProduto---------------

# --------Início da função main-----------
print('Bem vindo ao programa de registro de produtos de Luidson Lima Santos')

# Cria um loop
while True:
    # Testa a ocorrência de erros do valor informado
    try:
        print('-' * 15 + 'Digite a operação desejada:' + '-' * 15)
        # Recebe um valor inteira e atribui a variável opcao
        opcao = int(input('1 - Cadastrar Produto\n'
                          '2 - Consultar Produto\n'
                          '3 - Remover Produto\n'
                          '4 - Sair\n'
                          '>>'))
        # Testa se o valor da opção é igual a 1
        if opcao == 1:
            # Atribui + 1 a varável de registro e chama a função cadastrarProduto() com o valor do registro
            registroProduto += 1
            cadastrarProduto(registroProduto)
        # Testa se o valor da opção é igual a 2 e chama a função consultarProduto()
        elif opcao == 2:
            consultarProduto()
        # Testa se o valor da opção é igual a 3 e chama a função removerProduto
        elif opcao == 3:
            removerProduto()
        # Testa se a opção é igual a 4, imprime a mensagem de finalização e quebra o loop
        elif opcao == 4:
            print('Programa Finalizado')
            break
        # Caso o usuário informe um número inválido, informa que o valor é inválido
        else:
            print('Número inválido')
    except ValueError:
        print('Formato inválido')
# --------Fim da função main
