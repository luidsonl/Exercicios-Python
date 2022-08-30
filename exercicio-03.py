# Crie uma variável de string que receba uma frase qualquer. Crie uma segunda variável,
# agora contendo a metade da string digitada.
# Imprima na tela somente os dois últimos caracteres da segunda variável do tipo string.
phrase = input('Escreva uma frase ')
length = len(phrase)

phrase2 = phrase[:int(length/2)]
print(phrase2[-2:])
