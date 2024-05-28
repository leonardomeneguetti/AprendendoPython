#Laços de repetição evitam codogo repetido no programa
#A estrutura do for, tem uma quantidade conhecida de repetições:
#for contador in range(x, y, z):
#   Bloco_de_repetição
#O contador inicia no x, repete o laço até y-1 e z determina como esse passo a passo vai ser executado
#Conta de 0 a 5, sem o z, vai de 1 em 1
for i in range(0,6):
    print(i)
print('Fim')

#Conta de 0 a 5 de 2 em dois
for i in range(0,6,2):
    print(i)
print('Fim')

#Conta de 6 a 1, tirando 1 a cada loop
for i in range(6,0,-1):
    print(i)
print('Fim')

n = int(input('Digite um numero: '))
for i in range(0, n+1):
    print(i)
print('Fim')

s = int(input('Digite o começo: '))
e = int(input('Digite o final: '))
p = int(input('Digite o passo: '))
for i in range(s, e+1, p):
    print(i)
print('Fim')

soma = 0
for i in range(0,4):
    n = int(input('Digite um valor: '))
    soma += n
print(f'A soma de todos os numeros foi {soma}')

#Desafio 46
#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
#Biblioteca que coloca um tempo de espera
from time import sleep
for i in range(10,-1,-1):
    print(f'{i}...')
    sleep(1)
print('BUM! BUM! BUM! BUM! BUM!')
    
#Desafio 47
#Crie um programa que mostra na tela todos os números pares que estão no intervalo entre 1 e 50
for i in range(2,51,2):
    print(i)
print('Fim')

#Desafio 48
#Faça um programa que faça a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500
soma = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
print(f'A soma dos multiplos de 3, ímpares, até 500 deu {soma}')

#Desafio 49
#Refaça o exercício 9, mostrando a tabuada de um numero que o usuário escolher, só que agora utilizando um laço for
n = int(input('Digite um numero: '))
for i in range(0, 11):
    print(f'{n} X {i} = {n*i}')
print('Fim')

#Desafio 50
#Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Seo numero for ínpar, desconsidere-o
soma = 0
for i in range(0,6):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        soma += n
print(f'A soma de todos os valores pares digitados é {soma}')

#Desafio 51
#Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritmética. No final, mostre os 10 primeiros termos dessa progressão
n = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
for i in range(n, n + (razao * 10), razao):
    print(i)

#Desafio 52
#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
isPrimo = 'Sim'
n = int(input('Digite um número: '))
for i in range(2, n):
    if n % i == 0:
        isPrimo = 'Não'
print(f'{n} é um número primo? {isPrimo}')

#Desafio 53
#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
frase = input('Digite uma frase: ').replace(' ', '').upper()
isPalindromo = 'Sim'
for i in range(0, len(frase)):
    if frase[i] != frase[-(i+1)]:
        isPalindromo = 'Não'
print(f'{frase} é um palíndromo? {isPalindromo}')

#Desafio 54
#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
from datetime import date
maiorIdade = 0
menorIdade = 0
for i in range(0,7):
    ano = int(input('Digite o ano de nascimento: '))
    if date.today().year - ano < 21:
        menorIdade += 1
    else:
        maiorIdade += 1
print(f'{maiorIdade} são maiores de idade e {menorIdade} são menores de idade')

#Desafio 55
#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos
peso = float(input('Digite o peso: '))
maior = peso
menor = peso
for i in range(0,4):
    peso = float(input('Digite o peso: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso digitado foi {maior} Kg e o menor foi {menor} Kg')

#Desafio 56
#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final, mostre:
somaIdade = 0
nomeHMaisVelho = ''
idadeHMaisVelho = 0
mulheresMenos20 = 0
for i in range(0, 4):
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo (F ou M)')
    somaIdade += idade
    if sexo == 'M' and idade > idadeHMaisVelho:
        nomeHMaisVelho = nome
        idadeHMaisVelho = idade
    if sexo == 'F' and idade < 20:
        mulheresMenos20 += 1
    


# a)A média de idade do grupo
mediaIdade = somaIdade/4
print(f'Os participante têm em média {mediaIdade} anos')

# b)Qual o nome do homem mais velho
print(f'{nomeHMaisVelho} é o homem mais velho entre os participante')

# c)Quantas mulheres tem menos de 20 anos 
print(f'Tem {mulheresMenos20} mulher(es) com menos de 20 anos entre os participantes')
