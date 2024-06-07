#Funções são rotinas, partes do código que se repetem, então definimos como função e chamamos ela sempre que necessário, ao invés de reescrever o código
def mensagem(msg):
    n = len(msg)
    print('-'*n)
    print(f'{msg}')
    print('-'*n)

mensagem('Aprendendo Python')
mensagem('Leonardo Meneguetti')

def soma(a, b):
    s = a + b
    print(f'{a} + {b} = {s}')

soma(a=4, b=5) #Forma de declarar mais explicita, ou se for necessário inverter a ordem
soma(b=8, a=9)
soma(2, 1)

#O Python tem a capacidade de empacotar parâmetros, que permite uma função receber váriadas quantidades de parâmetros
def contador(*num): #No momento que os parâmetros são desempacotados, eles são colocados em uma tupla
    tam = len(num)
    print(f'Recebi {tam} parâmetros')
    for i in num:
        print(i, end=' ')
    print('FIM!')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

def somaV2(* valores):
    soma = 0
    for num in valores:
        soma += num
    print(f'Somando os valores {valores}, temos {soma}')

somaV2(2, 1, 7)
somaV2(8, 0)
somaV2(4, 4, 7, 6, 2)

#Se for passado direto uma variável composta, como uma lista, o empactamento não é necessário
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos]  *= 2
        pos += 1

valores = [7, 2, 5, 0, 4]
print(valores)
dobra(valores)
print(valores)

#Desafio 96
#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
#e mostre a área do terreno
def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {area}m²')

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)

#Desafio 97
#Faça um programa que tenha uma função chamada escreva(), que recebe um texto qualquer como parâmetro 
#e mostre uma mensagem com tamanho adaptável
def escreva(msg):
    n = len(msg) + 4
    print('='*n)
    print(f'  {msg}')
    print('='*n)

while True:
    txt = input('Mensagem (vazio para parar): ')
    if txt == '':
        break
    escreva(txt)

#Desafio 98
#Faça um programa que tenha uma função contador(), que receba três parâmetros: início, fim e passo e realize a contagem.
from time import sleep
def contador(inicio, fim, passo):
    print('='*40)
    if passo < 0:
        print(f'Contagem de {inicio} até {fim} de {-passo} em {-passo}')
        for i in range(inicio, fim-1, passo):
            print(i, end=' ', flush=True)
            sleep(0.25)
        print('FIM!')
    elif passo == 0:
        print(f'Contagem de {inicio} até {fim} de {1} em {1}')
        if inicio > fim:
            for i in range(inicio, fim-1, -1):
                print(i, end=' ', flush=True)
                sleep(0.25)
            print('FIM!')
        else:
            for i in range(inicio, fim+1, 1):
                print(i, end=' ', flush=True)
                sleep(0.25)
            print('FIM!')
    else:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        if inicio > fim:
            for i in range(inicio, fim-1, -passo):
                print(i, end=' ', flush=True)
                sleep(0.25)
            print('FIM!')
        else:
            for i in range(inicio, fim+1, passo):
                print(i, end=' ', flush=True)
                sleep(0.25)
            print('FIM!')

#a) De 1 até 10, de 1 em 1
contador(1, 10, 1)

#b) De 10 até 0, de 2 em 2
contador(10, 0, 2)

#c) Uma contagem personalizada
print('='*40)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)

#Desafio 99
#Faça um programa que tenha uma função chamada maior(), que receba vários parêmetros com valores inteiros
#Seu programa tem q analisar todos os valores e dizer qual deles é o maior
def maior(*num):
    print('='*80)
    print('Analisando os valores passados...')
    if len(num) == 0:
        maior = 0
        print(f'Nenhum valor foi informado')
    else:
        maior = num[0]
        for i in num:
            if i > maior:
                maior = i
            print(i, end=' ', flush=True)
            sleep(0.25)
        print(f'Foram informados {len(num)} valores ao todo')
        print(f'O maior número informado foi {maior}')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

#Desafio 100
#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar()
#A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
#a soma entre todos os valores pares sorteados pela função anterior
from random import randint
sorteados = []
def sorteia(lista): #Os parametros passados para a função não são cópias dos originais, mas sim, um ponteiro
    print('Sorteando 5 valores:', end=' ')
    for i in range(0,5):
        n = randint(0,10)
        lista.append(n)
        print(n, end=' ', flush=True)
        sleep(0.25)
    print('PRONTO!')
    
def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {lista}, temos {soma}')

sorteia(sorteados)
somaPar(sorteados)