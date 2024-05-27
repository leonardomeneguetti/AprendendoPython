#Para usar módulos no python, você precisa importá-los
#O import pode ser feito de modo mais generalista, trazendo todas as funções do módulo:
import math 
import random
#math é um módulo que facilita calculos
#Ou trazendo apenas algumas funcionalidades
# from math import sqrt, pow
#sqrt é uma funcionalidade do math que calcula raiz quadrada
#pow é uma funcionalidade do math que calcula potência

num = int(input('Digite um numero: '))
print(f'A potência de 2 de {num} é {math.pow(num, 2)}')
print(f'A raiz quadrada de {num} é {math.sqrt(num):.3f}')

#No site python.org, estão listadas várias bibliotecas e suas documentações

#Desafio 16
#Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira
num = float(input('Digite um numero real: '))
print(f'A parte inteira de {num} é {math.trunc(num)}')

#Desafio 17
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
catOp = float(input('Digite o cateto oposto: '))
catAdj = float(input('Digite o cateto adjacente: '))
hipotenusa = math.hypot(catOp, catAdj)
print(f'A hipotenusa do triâgulo é {hipotenusa}')

#Desafio 18
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
angulo = float(input('Digite um ângulo: '))
radiano = math.radians(angulo)
print(f'Seno: {math.sin(radiano):.3f}')
print(f'Cosseno: {math.cos(radiano):.3f}')
print(f'Tangente: {math.tan(radiano):.3f}')

#Desafio 19
#Um professor quer sortear um de seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
aluno1 = input('Nome do primeiro aluno: ')
aluno2 = input('Nome do segundo aluno: ')
aluno3 = input('Nome do terceiro aluno: ')
aluno4 = input('Nome do ultimo aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
sorteado = random.choice(lista)
print(f'O aluno escolhido foi: {sorteado}!')

#Desafio 20
#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programaque leia o nome dos quatro alunos e mostre a ordem sorteada
aluno1 = input('Nome do primeiro aluno: ')
aluno2 = input('Nome do segundo aluno: ')
aluno3 = input('Nome do terceiro aluno: ')
aluno4 = input('Nome do ultimo aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)

#Desafio 21 - Não era nem difícil, só muito chato, não fiz