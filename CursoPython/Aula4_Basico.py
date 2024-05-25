#Para mostrar algo na tela
print('Olá mundo!')

#Mostrando inteiros
print(7 + 4)
#11

#Não são inteiros
print('7' + '4')
#"74"

#Concatenar string com outro tipo não é feito assim
#print("Tua mãe é" + 10)
#mas sim, assim
print('Tua mãe é', 10)

#Em python, toda variável é um objeto
#Para interagir com o usuário, use input('mensagem'), que recebe uma string
nome = input('Qual seu nome?:')
idade = input('Quantos anos você tem?:')
peso = input('Qual seu peso?:')
print(nome, idade, peso)

#Desafio 1
#Crie um script em python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado
nome = input('Qual seu nome completo? ')
print('Olá', nome, '! Prazer em te conhecer')

#Desafio 2 
#Crie um script python que leia o dia, mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada
dia = input('Dia = ')
mes = input('Mês = ')
ano = input('Ano = ')
print('Você nasceu no dia', dia, 'de', mes, 'de', ano, '. Correto?')

#Desafio 3
#Crie um script em python que leia 2 numeros e mostre a soma entre eles
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
print(f'Soma = {n1 + n2}')