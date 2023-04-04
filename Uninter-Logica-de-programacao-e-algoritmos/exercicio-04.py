print('Expressões booleanas')

# O somatorio de 2 com 2 é menor do que 4
print(2 + 2 < 4)

# O valor 7//3 é igual a 1+1
print(7 // 3 == 1 + 1)

# A soma de 3 elevado ao quadrado com 5 elevado ao quadrado é igual a 25
print(3 ** 2 + 5 == 25)

# A soma de 2,4 e 6 é maior do que 12
print(2 + 4 + 6 > 12)

# 1387 é divisível por 19
print(1387 % 19 == 0)

# 31 é par
print(31 % 2 == 0)

# O menor valor entre: 34, 29 e 31 é menor do que 30
print(min(34, 29, 31) < 30)

print('Condicionais simples')

# Se a idade é maior que 60, escreva: "Você tem direito ao benefício"
idade = 61
if idade > 60:
    print('Você tem direito ao benefício')

# Se o dano é meior do que 10 e o escudo é igual a 0, escreva: "você esta morto"
dano = 11
escudo = 0
if dano > 10 and escudo == 0:
    print('Você está morto')

# Se pelo moenos uma das variáveis booleanas norte, sul, leste e oeste resultarem em true, escreva: "você escapou"
norte = False
sul = False
leste = False
oeste = True
if norte or sul or leste or oeste:
    print('Você escapu!')

print('Condicional composta')

# Se ano é divisível por 4, escreva: 'Pode ser um ano bissexto'.
# Caso contrário, escreva: "Definitivamente não é um ano bissexto"
ano = 2022
if ano % 4 == 0:
    print('Pode ser um ano bissexto')
else:
    print('Definitivamente não é um ano bissexto')

# Se ambas as variáveis booleanas cima e baixo forem true, escreva "Decida-se", caso contrário, escreva:
# VocÊ escolheu um caminho!"
cima = False
baixo = True
if cima and baixo:
    print('Decida-se!')
else:
    print('Você escolheu um caminho!')
    