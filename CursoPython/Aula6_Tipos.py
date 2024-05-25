#Na hora de receber o dado, precisa fazer o casting para fazer a soma
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
soma = n1 + n2
#Formas antigas
# print('A soma entre', n1, 'e', n2, 'é', soma)
# print('A soma entre {} e {} é {}'.format(n1, n2, soma))
#Forma mais atual, não passada no curso
print(f'A soma entre {n1} e {n2} vale {soma}')

n = input('Digite um valor: ')
#Verifica se é um numero
print(n.isnumeric)
#Verifica se é uma letra
print(n.isalpha)
#Verifica se é numero e/ou letra
print(n.isalnum)
#Verifica se tudo é letra maiúscula
print(n.isupper)
#Verifica se é printável
print(n.isprintable)

#Desafio 2
#Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ele
algo = input('Digite algo: ')
print(type(algo))
print(algo.isnumeric)
print(algo.isalpha)
print(algo.isalnum)
print(algo.isupper)
print(algo.isprintable)
#Verifica se é decimal
print(algo.isdecimal)
#Verifica se tudo é letra minúscula
print(algo.islower)
#Verifica se pertence aos simbolos ascii
print(algo.isascii)
#Verifica se é um espaço
print(algo.isspace)
#Verifica se é um digito
print(algo.isdigit)
#Verifica se é uma palavra reservada
print(algo.isidentifier)
#Verifica se a primeira letra de cada palavra é maiúscula
print(algo.istitle)