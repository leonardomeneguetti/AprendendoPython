#A estrutura de repetição while é usada quando não há como saber o limite de repetições
#A estrutura se forma do seguinte modo:
#while condição == True:
#   Bloco_de_repetição

#O while pode ser usado nas mesmas situações que o for, pois
for i in range(1,10):
    print(i)
print('Fim')
#É igual a
i = 1
while i < 10:
    print(i)
    i += 1
print('Fim')
#Porém, nesse caso, o for é mais eficiente, pois o limite é conhecido

#Mas em casos de limite desconhecido ou laços infinitos, o for não pode ser utilizado
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')
#Nesse caso, o laço vai ficar se repetindo infinitamente, a não ser que o usuário digite 0

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} numeros pares e {impar} numeros ímpares')
#Nesse exemplo, tendo que tratar também quando a condição de parada acontecer, pode ser melhorada usando o que vai ser passado na proxima aula

#Desafio 57
#Faça um programa que leia o sexo de uma pessoa, mas só aceita os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('Digte o seu sexo [M/F]: ').upper()
    if sexo != 'M' and sexo != 'F':
        print('Valor inválido, tente novamente.')
if sexo == 'M':
    print(f'Você é do sexo masculino')
else:
    print(f'Você é do sexo feminino')


#Desafio 58
#Melhoro o jogo do desafio 28(Aula 10) onde o computador vai "pensar" em um numero de 0 a 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando
#no final quantos palpites foram necessários para vencer.
import random
palpites = 0
resposta = random.randint(0,10)
chute = -1
while chute != resposta:
    chute = int(input('Digite o seu chute [0-10]: '))
    palpites += 1
print(f'Parabéns, você acertou em {palpites} palpite(s)')

#Desafio 59
#Crie um programa que leia dois valores e mostre um menu na tela:
#[1]Somar
#[2]Multiplicar
#[3]Maior
#[4]Novos números
#[5]Sair
#Seu programa deverá realizar a operaão solicitada em cada caso
a = float(input('Digite um valor: '))
b = float(input('Digite outro valor: '))
opcao = 0
maior = 0
while opcao != 5:
    print("""O que deseja fazer com esses numero?
[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos números
[5]Sair""")
    opcao = int(input('Sua escolha: '))
    if opcao == 1:
        print(f'A soma entre {a} e {b} é {a+b}')
    if opcao == 2:
        print(f'A multiplicação entre {a} e {b} é {a*b}')
    if opcao == 3:
        if a > b:
            maior = a
        else:
            maior = b
        print(f'O maior numero entre {a} e {b} é {maior}')
    if opcao == 4:
        a = float(input('Digite um novo valor: '))
        b = float(input('Digite outro novo valor: '))
    if opcao == 5:
        print('Saindo...')

#Desafio 60
#Faça um programa que leia um número e mostre seu fatorial

#Com while
n = int(input('Digite um valor: '))
fatorial = 1
i = n
while i > 0:
    fatorial *= i
    i -= 1
print(f'O fatorial de {n} é {fatorial}')

#Com for
n = int(input('Digite um valor: '))
fatorial = 1
for i in range(n, 0, -1):
    fatorial *= i
print(f'O fatorial de {n} é {fatorial}')

#Desafio 61
#Refaça o exercício 51(Aula 13), lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando while
n = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
cont = 0
while cont < 10:
    if cont < 9:
        print(n, end=', ')
    else: 
        print(n, end='.')
    n += razao
    cont += 1

#Desafio 62
#Melhore o desafio 61(Aula 14), perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos
n = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
maisTermos = -1
qtdTermos = 0
while maisTermos != 0:
    maisTermos = int(input('Digite quantos mais termos da PA você quer mostrar: '))
    if maisTermos != 0:
        qtdTermos += maisTermos
        cont = 0
        while cont < qtdTermos:
            if cont < qtdTermos - 1:
                print(n, end=', ') 
            else: 
                print(n, end='...\n')
            n += razao
            cont += 1

#Desafio 63
#Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci
n = int(input('Digite quantos serão os elementos: '))
antigo = 1
atual = 0
i = 0
while i < n:
    if i < n - 1: 
        print(atual, end=', ')
    else:
        print(atual, end='.')
    temp = atual
    atual += antigo
    antigo = temp
    i += 1

#Desafio 64
#Crie um programa que leia vários numeros inteiros pelo teclado. O programa só vai para quando o usuário digitar 999, que é a condição de parada.
#No final, mostre quantos numeros foram digitados e qual foi a soma entre eles
n = 0
i = 0
soma = 0
while n != 999:
    n = int(input('Digite um valor: '))
    if n != 999:
        i += 1
        soma += n
print(f'Foram digitados {i} números e a soma total entre eles foi {soma}')

#Desafio 65
#Crie um programa que leia vários numeros inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar
continuar = 'S'
i = 0
soma = 0
maior = 0
menor = 0
while continuar != 'N':
    n = int(input('Digite um valor: '))
    i += 1
    soma += n
    if i == 1:
        maior = n
        menor = n
    else: 
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = input('Deseja continuar? [S/N]: ').upper()
    
print(f'A média entre os números foi {soma/i}, o maior número foi {maior} e o menor foi {menor}')