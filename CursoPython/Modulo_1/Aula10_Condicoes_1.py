#As estruturas condicinais no python são formadas assim:

#if condição == True:
#   Bloco_True
#else:
#   Bloco_False

#As condições do if não precisam de parenteses, tem que ter ':' antes do bloco de comando e os blocos de comando não ficam entre chaves

tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('----FIM----')

#Se os blocos de comando forem curtos, podem ser usados assim

#Bloco_True if condição == True else Bloco_Falsea

tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo' if tempo <= 3 else 'Carro velho')
print('----FIM----')

nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
media = (nota1+nota2)/2
print(f'A sua média foi {media:.1f}')
if media >= 6:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

#Desafio 28
#Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuário tentar 
#descobrir qual foi o número escolhido pelo computador. O programa deve escrever na tela se o usuário venceu ou perdeu
import random
resposta = random.randint(0,5)
chute = int(input('O computador escolheu um numero de 0 a 5. Tente adivinhar qual: '))
if chute == resposta:
    print('Você acertou! Parabéns!')
else:
    print(f'Você errou! A resposta certa era {resposta}')

#Desafio 29
#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada km acima do limite
velocidade = float(input('Digite a velocidade do veículo: '))
if velocidade > 80:
    print(f'O motorista será multado em R${(velocidade-80)*7:.2f}')

#Desafio 30
#Crie um programa que leia um numero inteiro e mostre na tela se ele é PAR ou ÍMPAR
n = int(input('Digite um número inteiro: '))
if n%2 == 0:
    print(f'{n} é PAR')
else:
    print(f'{n} é ÍMPAR')

#Desafio 31
#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule a passagem, cobrando R$0,50 por Km para viagens de até
#200km e R$0,45 para viagens mais longas
distancia = float(input('Digite a distancia da viagem: '))
if distancia <= 200:
    print(f'A passagem para uma viagem de {distancia} Km custa R${distancia*0.5}')
else:
    print(f'A passagem para uma viagem de {distancia} Km custa R${distancia*0.45}')

#Desafio 32
#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
n = int(input('Digite um número inteiro: '))
if n%4 == 0 and n%100 != 0 or n%400 == 0:
    print(f'{n} é um ano BISSEXTO')
else:
    print(f'{n} não é um ano BISSEXTO')

#Desafio 33
#Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor
a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior é {maior} e o menor é {menor}')

#Desafio 34
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%, para salários inferiores ou menores, o aumento é de 15%
salario = float(input('Digite o salario do funcionário: '))
if salario > 1250:
    print(f'O salário com o aumento de 10% será de R${salario*1.1:.2f}')
else:
    print(f'O salário com o aumento de 15% será de R${salario*1.15:.2f}')

#Desafio 35
#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print(f'Os segmentos {a}, {b} e {c} podem formar um triângulo')
else:
    print(f'Os segmentos {a}, {b} e {c} não podem formar um triângulo')