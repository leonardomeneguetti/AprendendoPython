#Tuplas são os arrays do python
#Eles podem ser "fatiados" do mesmo jeito que as strings(Aula 09)
#As tuplas são criadas colocando seus valores entre parênteses ou sem nada em volta
tupla = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
tupla = 1, 2, 3, 4, 5, 6, 7
#tupla[x:y:z], para selecionar um intervalo de valores de x até y-1, pulando z valores
print(tupla[1:7:2])
#Tuplas podem ser usadas para substituir o range() nas estruturas for
for i in tupla:
    print(i)
#As tuplas são IMUTÁVEIS, ou seja, fazer isso não é possível
tupla[4] = 9
print(tupla)

#Outros jeitos de fazer o for com a tupla, caso a posição seja algo relevante
for i in range(0, len(tupla)):
    print(f'{tupla[i]} na posição {i}')

for posicao, letra in enumerate(tupla):
    print(f'{letra} na posição {posicao}')

#Tuplas podem ser mostradas ordenadas, usando a função sorted(tupla)
tuplaDesordenada = 'G','F','E','D','C','B','A'
print(sorted(tuplaDesordenada))

#Operações de soma entre tuplas funcionam igual em strings
a = (1, 2, 3)
b = (3, 4, 5, 6)
c = a + b
print(c)

#As tuplas tem a função tupla.index(valor), que funciona igual a função string.find(valor)
print(c.index(4))

#Tuplas não precisam ter todos os dados do mesmo tipo
pessoa = ('Leonardo', 20, 'M', 80.23)
print(f'{pessoa[0]} tem {pessoa[1]} anos, é do sexo {pessoa[2]} e pesa {pessoa[3]} kilos')

#A dunção del(variável) apaga uma variável da memória
tuplaNova = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
del(tuplaNova)
print(tuplaNova) #Vai dar erro por não estar definido
del(tupla[1]) #Dá erro, pois a tupla não pode ser modificada

#Desafio 72
#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de 0 até 20.
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
            'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
n = -1
while n > 20 or n < 0:
    n = int(input('Digite um número de 0 a 20: '))
    if n > 20 or n < 0:
        print('Tente novamente. ', end='')
print(f'Você digitou o número {extenso[n]}')

#Desafio 73
#Crie uma tupla preenchida com o 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
brasileirao = ('Flamengo', 'Bahia', 'Botafogo', 'São Paulo', 'Athletico-PR', 'Bragantino', 'Palmeiras', 'Internacional', 
               'Cruzeiro', 'Atlético-MG', 'Fortaleza', 'Grêmio', 'Vasco da Gama', 'Juventude', 'Fluminense', 'Criciúma', 
               'Corinthians', 'Atlético-GO', 'EC Vitória', 'Cuiabá')

#a) Apenas os 5 primeiros colocados
print(brasileirao[:5])

#b) Os últimos 4 colocados.
print(brasileirao[-4:])

#c) Uma lista com os times em ordem alfabética
print(sorted(brasileirao))

#d) Em que posição está o time Chapecoense
print(brasileirao.index('Chapecoense')) #Chapecoense ta na série B

#Desafio 74
#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de numeros gerados e também indique o menor e o maior valor que estão na tupla.
import random
aleatorios = (random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))
print('Os valores sorteados foram: ', end='')
maior = 0
menor = 11
for i in aleatorios:
    print(i, end=' ')
    if i > maior:
        maior = i
    if i < menor:
        menor = i
print(f'\nO maior valor foi o {maior} e o menor foi o {menor}')

#Desafio 75
#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
numeros = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))

#a) Quantas vezes apareceu o numero 9
print(f'O número 9 apareceu {numeros.count(9)} vezes')

#b) Em que posição foi digitado o primeiro valor 3
if 3 in numeros:
    print(f'O número 3 apareceu pela primeira vez na {numeros.index(3)+1}ª posição')
else:
    print('O número 3 não foi digitado')

#c) Quais foram os números pares
print('Os números pares digitados foram: ', end='')
for i in numeros:
    if i % 2 == 0:
        print(i, end=', ')
    
#Desafio 76
#Crie umm programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular
produtos = ('Camisa PP', 24.99, 'Camisa P', 29.99, 'Camisa M', 34.99, 'Camisa G', 39.99, 'Camisa GG', 44.99,
             'Calça PP', 34.99, 'Calça P', 39.99, 'Calça M', 44.99, 'Calça G', 49.99, 'Calça GG', 54.99)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for i in range(0, len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]:.<32}', end='')
    else:
        print(f'R$ {produtos[i]}')
print('-'*40)

#Desafio 77
#Crie um programa que tenha uma tupla com várias palavras(sem acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('CACHORRO', 'GATO', 'PEIXE', 'PASSARO', 'JACARE', 'COBRA')
for i in palavras:
    print(f'Na palavra {i} temos ', end='')
    for j in i:
        if j in 'AEIOU':
            print(j.lower(), end=' ')
    print('')