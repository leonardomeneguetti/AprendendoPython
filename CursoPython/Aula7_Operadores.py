#Operadores aritméticos
# + para adição
# - para subtração
# * para multiplicação, também serve para string, repetindo ela
# / para divisão
# // para divisão inteira (sem virgula)
# % para resto da divisão
# ** para exponencial == pow(base, potência)
# para cálculo de raiz, use x**(1/y)

#Ordem de precedencia
# 1: ( )
# 2: **
# 3: *, /, //, %
# 4: +, -

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print(f'A soma vale {n1+n2}')
print(f'A subtração vale {n1-n2}')
print(f'A multiplicação vale {n1*n2}')
# :.xf depois do nome da variável, para que um valor decimal fique com x casas decimais
print(f'A divisão vale {n1/n2:.3f}')
print(f'A divisão inteira vale {n1//n2}')
print(f'O resto vale {n1%n2}')
#Colocando end='sequência_de_char', o print não pula linha para o proximo print e coloca a sequencia de char no final
print(f'A potência vale {n1**n2}', end='. ')

#Curiosiade
#No python, n existe tipo long ou BigDecimal, o limite de uma variável é o limite da memória
#Usando o print(f'string {variável}'), depois do nome da variável, pode colocar:
# :x, para fazer a variável ocupar x caracteres
# :>x, para fazer a variável ocupar x caracteres e estar alinhada à direita
# :<x, para fazer a variável ocupar x caracteres e estar alinhada à esquerda
# :^x, para fazer a variável ocupar x caracteres e estar centralizada
# :char^x, para fazer a variável ocupar x caracteres, estar centralizada e com o char específico em volta dela
nome = input('Qual seu nome? ')
print(f'Bem vindo {nome:=^20}!') # Bem vindo ========nome========!

#Desafio 5
#Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor
valor = int(input('Digite um numero inteiro: '))
print(f'O antecessor de {valor} é {valor-1} e seu sucessor é {valor+1}')

#Desafio 6
#Crie um algorítmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada
valor = int(input('Digite um numero inteiro: '))
print(f'O dobro de {valor} é {valor*2}, seu triplo é {valor*3} e sua raiz quadrada é {valor**(1/2):.3f}')

#Desafio 7
#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
print(f'A média das notas do aluno foi {(nota1+nota2)/2:.2f}')

#Desafio 8
#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
metros = float(input('Digite um valor em metros: '))
print(f'{metros} metros são iguais a {metros*100} centímetros ou {metros*1000} milímetros')

#Desafio 9
#Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada
n = int(input('Digite um numero inteiro: '))
print(f'{n} * 0 = {n*0}')
print(f'{n} * 1 = {n*1}')
print(f'{n} * 2 = {n*2}')
print(f'{n} * 3 = {n*3}')
print(f'{n} * 4 = {n*4}')
print(f'{n} * 5 = {n*5}')
print(f'{n} * 6 = {n*6}')
print(f'{n} * 7 = {n*7}')
print(f'{n} * 8 = {n*8}')
print(f'{n} * 9 = {n*9}')
print(f'{n} * 10 = {n*10}')

#Desafio 10
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. US$ 1.00 == R$ 3.27
n = float(input('Digite o valor em reais: '))
print(f'{n} reais são {n/3.27:.2f} dólares')

#Desafio 11
#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade necessária de tinta para pintá-la,
#sabendo que cada litro de tinta pinta 2m²
largura = float(input('Digite a largura da parede, em metros: '))
altura = float(input('Digite a altura da parede, em metros: '))
area = largura * altura
print(f'A área de uma parede de {largura}m X {altura}m é {area}m² e são necessários {area/2}litros de tinta')

#Desafio 12
#Faça um algorítmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
preco = float(input('Digite o preço do produto: '))
print(f'Com os 5% de desconto, o preço cai de R${preco:.2f} para R${preco*0.95:.2f}')

#Desafio 13
#Faça um algorítmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input('Digite o salario do funcionário: '))
print(f'Com os 15% de aumento, o salário cresce de R${salario:.2f} para R${salario*1.15:.2f}')

#Desafio 14
#Escreva um programa que converta uma temperatura digitada em °C e converta para °F
temp = float(input('Digite a temperatura em °C: '))
print(f'{temp} graus Celsius em graus Farenheit é {(temp * 9 / 5) + 32}')

#Desafio 15
#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado
km = float(input('Quantos kilômetros foram rodados? '))
dias = float(input('Quantos dias ficou alugado? '))
preco =  km * 0.15 + dias * 60
print(f'Como o carro ficou alugado por {dias} dias e rodou {km} Km, o preço do aluguel é R${preco}')