#Existem casos em que durante a execução de um loop, é necessário interromper tudo e sair do do loop, para isso existe o comando break
#while condição == True:
#   Blobo_de_repetição
#   if condição_de_interrupção == True
#       break
i = 0
while True:
    print(i, end=' -> ')
    i += 1
    if i > 999:
        break
print('Acabou')

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')

#Desafio 66
#Crie um programa que leia vários numeros inteiros pelo teclado. O programa só vai para quando o usuário digitar 999, que é a condição de parada.
#No final, mostre quantos numeros foram digitados e qual foi a soma entre eles
n = 0
i = 0
soma = 0
while n != 999:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    i += 1
    soma += n
print(f'Foram digitados {i} números e a soma total entre eles foi {soma}')

#Desafio 67
#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo
while True:
    n = int(input('Digite um número: '))
    if n < 0:
        break
    print('=' * 40)
    print(f'TABUADO DO {n}')
    for i in range(0,11):
        print(f'{n} X {i} = {n*i}')
    print('=' * 40)
print('PROGRAMA ENCERRADO')

#Desafio 68
#Faça um programa que jogue par ou ímpar com o jogador. O jogo só será interrompido quando o jogador perder. Mostrando o total de vitórias consecutivas 
#que ele conquistou no final do jogo
import random
jogadas = ['PAR', 'IMPAR']
vitorias = 0
while True:
    userEscolha = input('Par ou ímpar? (Sem acento): ').strip().upper()
    if userEscolha in jogadas:
        if userEscolha == 'PAR':
            cpuEscolha = 'IMPAR'
        else: 
            cpuEscolha = 'PAR'
        userNumero = int(input('Escolha um número de 0 a 10: '))
        cpuNumero = random.randint(0,10)
        soma = cpuNumero + userNumero
        print(f'O computador escolheu {cpuNumero}, então a soma deu {soma}.')
        resto = soma % 2
        if resto == 0:
            if userEscolha == 'PAR':
                print('Você ganhou')
                vitorias += 1
            else:
                print('Você perdeu! O jogo acabou')
                break
        else: 
            if userEscolha == 'IMPAR':
                print('Você ganhou')
                vitorias += 1
            else:
                print('Você perdeu! O jogo acabou')
                break
    else:
        print('Valor inválido, digite novamente.')
print(f'Você ganhou {vitorias} vez(es) seguida(s)')

#Desafio 69
#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoas cadastrada, o programa deve perguntar se o usuário deseja continuar.
#No final, mostre:
mais18 = 0
homens = 0
mulheresMenos20 = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ''
    while sexo not in 'MF':
        sexo = input('Digite o sexo [M/F]: ').strip().upper()
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheresMenos20 += 1
    resposta = ''
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').strip().upper()
    if resposta == 'N':
        break

#a) quantas pessoas tem mais de 18 anos.
print(f'{mais18} pessoas tinham mais de 18 anos')

#b) quantos homens foram cadastrados.
print(f'{homens} homens foram cadastrados')

#c) quantas mulheres tem menos de 20 anos
print(f'{mulheresMenos20} mulheres com menos de 20 anos foram cadastradas')

#Desafio 70
#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
mais1000 = 0
nomeMaisBarato = ''
precoMaisBarato = 0
i = 0
total = 0
while True:
    produto = input('Digite o nome do produto: ').strip()
    preco = float(input('Digite o preço do produto: '))
    total += preco
    if preco > 1000:
        mais1000 += 1
    if i == 0:
        nomeMaisBarato = produto
        precoMaisBarato = preco
    else: 
        if preco < precoMaisBarato:
            nomeMaisBarato = produto
            precoMaisBarato = preco
    i += 1
    resposta = ''
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').strip().upper()
    if resposta == 'N':
        break

#a) Qual é o total gasto na compra
print(f'O total gasto na compra foi R${total:.2f}')

#b) Quantos produtos custam mais de R$1000,00
print(f'{mais1000} produtos custam mais de R$1000,00')

#c) Qual é o nome do produto mais barato 
print(f'O produto mais barato foi o(a) {nomeMaisBarato}, que custa R${precoMaisBarato:.2f}')

#Desafio 71
#Crie um programa que simule o funcionamento de um caixa eletrônic. No início, pergunte ao usuário qual será o valor a ser sacado(numero inteiro)
#e o programa vai informar quantas cédulas de cada valor serão entregues(Cédulas de R$50, R$20, R$10 e R$1)
while True:
    n = int(input('Qual valor deseja sacar? R$'))
    if n <= 0:
        break
    resto = 0
    c50 = n // 50
    resto = n % 50
    c20 = resto // 20
    resto %= 20
    c10 = resto // 10
    resto %= 10
    c1 = resto
    print(f"""Vão ser sacadas: 
{c50} cédulas de R$50,00
{c20} cédulas de R$20,00
{c10} cédulas de R$10,00
{c1} cédulas de R$1,00""")




