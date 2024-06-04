#Listas funcionam de maneira parecida com as tuplas, mas são mutáveis, então boa parte dos métodos que funcionam na tupla, funcionam aqui
#Para declarar uma lista usa-se colchetes
lista = [1, 2, 3, 4, 5, 6, 7]
print(lista)
#Ou usa-se o método list(elemento_1, elemento_2, elemento_3, ...)
lista2 = list(range(10, 21))
print(lista2)
#Com listas é possível alterar elementos em tempo de execução
lista[4] = 9
print(lista)
#Para adicionar novos elementos à lista, use lista.append('elemento_novo')
lista.append(8)
print(lista)
#Também pode ser usado lista.insert(index, 'elemento_novo')
lista.insert(0,0)
print(lista)
#É possível remover elementos da lista, usando del lista[index]
del lista[0]
print(lista)
#Ou usando lista.pop(index), o método pop, sem index remove o último elemento
lista.pop()
print(lista)
#Ou ainda lista.remove('elemento'), que remove a primeira aparição do elemento específicado
lista.remove(9)
print(lista)
#O método lista.reverse() inverte a ordem dos elementos e o método lista.sort() ordena os elementos em ordem crescente/alfabética
lista.reverse()
print(lista)
lista.sort()
print(lista)
#Fazendo desse jeito, ao invés de copiar uma lista, você está fazendo uma ligação entre elas, então o que for modificado em uma, também é modificado na outra
a = [9, 5, 7, 2]
b = a #Aqui está fazendo uma ligação entre a lista e uma variável
b[2] = 3
print(f'Lista A: {a}')
print(f'Lista B: {b}')
#Para criar uma cópia, faça assim
a = [9, 5, 7, 2]
c = a[:] #Aqui está passando os elementos de a para c
c[2] = 3
print(f'Lista A: {a}')
print(f'Lista C: {c}')

#Desafio 78
#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista
#No final, mostre qual foi o maior e o menor valor digitados e as suas respectivas posições
valores = []
maior = 0
menor = 0
for i in range(0,5):
    valores.append(int(input('Digite um valor: ')))
    if i == 0:
        maior = valores[0]
        menor = valores[0]
    elif valores[i] < menor:
        menor = valores[i]
    elif valores[i] > maior:
        maior = valores[i]
print(f'O maior valor foi {maior} nas posições ', end='')
for pos, i in enumerate(valores):
    if i == maior:
        print(f'{pos}', end=' ')
print('')
print(f'O menor valor foi {menor} nas posições ', end='')
for pos, i in enumerate(valores):
    if i == menor:
        print(f'{pos}', end=' ')

#Desafio 79
#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista
#Caso o número já esteja lá dentro, ele não será adicinado
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente
valores = []
r = 's'
while r in 'Ss':
    n = (int(input('Digite um valor: ')))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado')
    else: 
        print('Valor já está na lista, não será adicionado')
    r = input('Deseja continuar? [S/N] ')
    if r in 'Nn':
        break
valores.sort()
print(valores)

#Desafio 80
#Crie um programa onde o usuário possa digitar 5 números e cadastre-os em uma lista, já na posição correta de inserção(sem usar sort()).
#No final, mostre a lista ordenada na tela.
valores = []
for i in range(0,5):
    n = int(input('Digite um valor: '))
    if i == 0 or n > valores[-1]:
        valores.append(n)
        print('O valor foi colocado no final da lista')
    else:
        for pos, i in enumerate(valores):
            if n <= i:
                valores.insert(pos, n)
                print(f'O valor foi colocado na {pos+1}ª posição')
                break
print(valores)

#Desafio 81
#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
valores = []
r = 's'
while r in 'Ss':
    valores.append((int(input('Digite um valor: '))))
    r = input('Deseja continuar? [S/N] ')
    if r in 'Nn':
        break

#a) Quantos números foram digitados
print(f'Foram digitados {len(valores)} números')

#b) A lista de valores, ordenada de forma decrescente
valores.sort()
valores.reverse()
print(f'A lista em ordem decrescente fica {valores}')

#c) Se o valor 5 foi digitado e está ou não na lista
if 5 in valores:
    print('O valor 5 foi digitado')
else: 
    print('O valor 5 não foi digitado')

#Desafio 82
#Crie um programa que vai ler vários números e colocar em uma lista
#Depois disso, crie uma lista que vai conter apenas os valores pares e outra que vai conter apenas os ímparesa
#Ao final, mostre os conteúdos das 3 listas
valores = []
r = 's'
while r in 'Ss':
    valores.append((int(input('Digite um valor: '))))
    r = input('Deseja continuar? [S/N] ')
    if r in 'Nn':
        break
pares = []
impares = []
for n in valores:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'Lista completa: {valores}')
print(f'Lista dos pares: {pares}')
print(f'Lista dos ímpares: {impares}')

#Desafio 83
#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se 
#a expressão passada está com os parênteses abertos e fechados na ordem correta
expressão = input('Digite uma expressão matemática com parênteses: ')
if expressão.count('(') == expressão.count(')') and expressão[0] != ')' and expressão[-1] != '(':
    print('A expressão é válida')
else:
    print('A expressão não é válida')
