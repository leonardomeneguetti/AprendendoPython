#Quando estamos trabalhando com listas, podemos criar listas dentro de listas
pessoas = [['Leonardo', 20],['Marcia', 26],['Antonio', 30]]
#Para acessar indices na lista dentro da lista, basta apenas fazer
print(pessoas)
print(f'Nome: {pessoas[0][0]}')
#Se não indicar o indice da lista interna, mostra ela completa
print(f'Pessoa: {pessoas[0]}')
#Podemos também colocar uma lista já existente dentro de outra
pessoa = ['José', 16]
pessoas.append(pessoa[:])
print(pessoas)

#Um exemplo mais completo de uso
galera = list()
dado = list()
totmai = totmen = 0

for i in range(0,3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores de idade e {totmen} menores de idade')


#Desafio 84
#Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
pessoas = list()
dado = list()
maior = menor = 0
while True:
    dado.append(input('Nome: '))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    if maior == menor == 0:
        maior = dado[1]
        menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    dado.clear()
    r = input('Deseja continuar? [S/N] ')
    if r in 'Nn':
        break

#a) Quantas pessoas foram cadastradas
print(f'Foram cadastradas {len(pessoas)} pessoas')

#b) Uma listagem com as pessoas mais pesadas
print(f'O maior peso foi {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(p[0], end='... ')

#c) Uma listagem com as pessoas mais leves
print(f'O menor peso foi {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(p[0], end='... ')

#Desafio 85
#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
#separados os valores pares e impares. No final, mostre os valores pares e ímpares em ordem crescente.
num = [[], []]
for i in range(0, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
num[0].sort()
num[1].sort()
print(f'Valores pares: {num[0]}')
print(f'Valores ímpares: {num[1]}')

#Desafio 86
#Crie um programa que crie uma matriz 3x3 e preencha com valores lidos pelo teclado
#No final, mostre a matriz na tela, com formatação correta
matriz = [[], [], []]
for i in range(0,3):
    for j in range(0,3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))

for i in matriz:
    for j in i:
        print(f'[  {j}  ]', end='')
    print('')

#Desafio 87
#Aprimore o exercício anterior, mostrando no final
matriz = [[], [], []]
soma = soma3 = maior = 0
for i in range(0,3):
    for j in range(0,3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))
        if matriz[i][j] % 2 == 0:
            soma += matriz[i][j]
        if j == 2:
            soma3 += matriz[i][j]
        if i == 1:
            if matriz[i][j] > maior:
                maior = matriz[i][j]

for i in matriz:
    for j in i:
        print(f'[  {j}  ]', end='')
    print('')

#a) A soma de todos os valores pares digitados
print(f'A soma de todos os valores pares digitados é {soma}')

#b) A soma dos valores da terceira coluna
print(f'A soma dos valores da tercera coluna é {soma3}')

#c) O maior valor da segunda linha
print(f'O maior valor da asegunda linha é {maior}')

#Desafio 88
#Faça um programa que ajude um jogador da Mega Sena a criar palpites. O programa vai perguntar quantos jogos serão gerados
#e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
import random
from time import sleep

jogos = []
n = int(input('Quantos jogos deseja criar? '))
for i in range(0, n):
    jogo = []
    j = 0
    while j < 6:
        n = random.randint(1, 60)
        if n not in jogo:
            jogo.append(n)
            j += 1
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()

print('Sorteando os jogos...')
for pos, i in enumerate(jogos):
    sleep(0.5)
    print(f'Jogo {pos+1}: {i}')


#Desafio 89
#Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim
#contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente
alunos = list()
while True:
    aluno = list()
    aluno.append(input('Digite o nome do aluno: '))
    notas = list()
    notas.append(float(input('Digite a primeira nota: ')))
    notas.append(float(input('Digite a segunda nota: ')))
    aluno.append(notas[:])
    aluno.append((notas[0]+notas[1])/2)
    notas.clear()
    alunos.append(aluno[:])
    aluno.clear()
    r = input('Deseja continuar? [S/N] ')
    if r in 'Nn':
        break

print(f'{' Boletim ':=^23}')
print(f'{'No.':<4}', end='')
print(f'{'NOME':<14}', end='')
print(f'{'MÉDIA':<7}')
print(f'{'-'*23}')
for pos, i in enumerate(alunos):
    print(f'{pos+1:<4}', end='')
    print(f'{i[0]:<14}', end='')
    print(f'{i[2]:>5}')
print(f'{'-'*23}')

id = 0
while id != 999:
    id = int(input('Mostrar as notas de qual aluno? (999 interrompe) '))
    if id == 999:
        break
    if id <= len(alunos):
        print(f'As notas de {alunos[id-1][0]} são {alunos[id-1][1]}')
    else: 
        print('Esse aluno não foi encontrado, tente novamente')