#As estruturas condicinais aninhadas no python são formadas assim:

#if condição1 == True:
#   Bloco_Condição1
#elif condição2 == True:
#   Bloco_Condição2
#elif condição 3 == True:
#   Bloco_Condição3
#else:
#   Bloco_Se_Todos_False

#Em outras linguagens, usa-se o 'else if', mas o python diminui a expressão para 'elif'
#Para entrar no elif, a condição anterior tem que ser False

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2
print(f'A sua média foi {media:.1f}')
if media > 6:
    print('Sua média foi boa! PARABÉNS!')
elif media == 6:
    print('Passou raspando! PARABÉNS, MAS ESTUDE MAIS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

nome = input('Qual seu nome? ')
if nome == 'Leonardo':
    print('Que nome bonito!')
elif nome == 'Rozicleyde' or nome == 'Cleudinete':
    print('Que nome diferente!')
else:
    print('Que nome normal!')
print(f'Tenha um bom dia, {nome}!')

#Desafio 36
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, 
#o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder
#30% do salário ou então o empréstimo será negado.
valorCasa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário?'))
anos = int(input('Em quantos anos pretende dividir o valor? '))
prestacao = valorCasa/(anos*12)
if prestacao <= salario*0.3:
    print(f'O empréstimo foi aprovado, no valor de R${prestacao:.2f} por mês')
else:
    print('O empréstimo não pode ser aprovado, pois o valor da prestação corresponde a mais que 30% do seu salário')

#Desafio 37
#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 
#2 para octal e 3 para hexadecimal
num = int(input('Digite um número inteiro qualquer: '))
opcao = int(input("""Escolha a base de conversão:
[1] Binário
[2] Octal
[3] Hexadecimal 
Sua escolha: """))
if opcao == 1:
    print(f'{num} em Binário é {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} em Octal é {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} em Hexadecimal é {hex(num)[2:]}')
else:
    print('Valor inválido')

#Desafio 38
#Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais
num1 = int(input('Digite o primeiro valor inteiro: '))
num2 = int(input('Digite o segundo valor inteiro: '))
if num1 > num2:
    print('O primeiro valor é maior')
elif num2 > num1:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')

#Desafio 39
#Faça um programa que leia o ano de nascimento de um jovem e informe: 
# - Se ele ainda vai se alistar
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date
nasc = int(input('Digite o ano em que nasceu: '))
idade = date.today().year - nasc
if idade > 18:
    print(f'Já passou do tempo do alistamento há {idade - 18} anos')
elif idade < 18:
    print(f'Vai precisar se alistar em {18 - idade} anos')
else:
    print('É a hora de se alistar!')

#Desafio 40
#Crie um programa que leia duas notas de um aluno e calcule a média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média acima de 7.0: APROVADO
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2
print(f'A sua média foi {media:.1f}')
if media < 5:
    print('REPROVADO!')
elif media >= 7:
    print('APROVADO!')
else:
    print('RECUPERAÇÃO!')

#Desafio 41
#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER
nasc = int(input('Digite o ano em que o atleta nasceu: '))
idade = date.today().year - nasc
if idade <= 9:
    print('Categoria Mirim')
elif idade <= 14:
    print('Categoria Infantil')
elif idade <= 19:
    print('Categoria Junior')
elif idade <= 20:
    print('Categoria Sênior')
else:
    print('Categoria Master')

#Desafio 42
#Refaça o desafio 35 dos triângulos(Aula 10), acrescentando o recuros de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print(f'Os segmentos {a}, {b} e {c} podem formar um triângulo equilátero')
    elif a != b != c != a:
        print(f'Os segmentos {a}, {b} e {c} podem formar um triângulo escaleno')
    else:
        print(f'Os segmentos {a}, {b} e {c} podem formar um triângulo isósceles')
else:
    print(f'Os segmentos {a}, {b} e {c} não podem formar um triângulo')

#Desafio 43
#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura em m: '))
imc = peso / (altura*altura)
if imc < 18.5:
    print(f'{imc} está abaixo do peso')
elif imc < 25:
    print(f'{imc} está no peso ideal')
elif imc < 30:
    print(f'{imc} está com sobrepeso')
elif imc < 40:
    print(f'{imc} está com obesidade')
else:
    print(f'{imc} está com obesidade mórbida')

#Desafio 44
#Elaborar um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
preco = float(input('Digite o valor do produto: '))
opcao = int(input("""Qual o método de pagamento: 
[1] À vista dinheiro/cheque
[2] À vista no cartão
[3] Em até 2x no cartão
[4] 3x ou mais no cartão
Sua escolha: """))
if opcao == 1:
    print(f'Com um desconto de 10%, o preço será de {preco*0.9:.2f}')
elif opcao == 2:
    print(f'Com um desconto de 5%, o preço será de {preco*0.95:.2f}')
elif opcao == 3:
    print(f'Cada parcela será de {preco/2:.2f}, com um valor total de {preco}')
elif opcao == 4:
    vezes = int(input('Em quantas vezes deseja dividir? '))
    preco *= 1.2
    if vezes <= 2:
        print('Temos outras formas de pagamento que abrangem esse valor')
    else:
        print(f'Com juros de 20% e dividindo o valor em {vezes} vezes, cada aparcela será de {preco/vezes:.2f}, com um valor total de {preco}')
else:
    print('Valor inválido')

#Desafio 45
#Crie um programa que faça o computador jogar jokempo com você
import random
jogadas = ['PEDRA', 'PAPEL', 'TESOURA']
cpu = random.choice(jogadas)
print(cpu)
jogador = input('Digite a sua jogada: ').strip()
print('Jo')
print('Kem')
print('Po!')
if jogador.upper() == cpu:
    print('Empatou!')
elif jogador.upper() == 'PEDRA':
    if cpu == 'PAPEL':
        print('Você perdeu!')
    else:
        print('Você ganhou!')
elif jogador.upper() == 'PAPEL':
    if cpu == 'PEDRA':
        print('Você ganhou!')
    else:
        print('Você perdeu!')
elif jogador.upper() == 'TESOURA': 
    if cpu == 'PEDRA':
        print('Você perdeu!')
    else:
        print('Você ganhou!')
else:
    print('Valor inválido')