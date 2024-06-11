# #Pacotes são as bibliotecas do python, ou seja, conjuntos de módulos, separados por tema
# #Para criar um pacote, basta colocar os módulos que deseja dentro de uma pasta
# #Têm o mesmo objetivo da modularização, mas quando o escopo do projet é ainda maior
# #Para importar um módulo de um pacote, use from pacote import modulo

# from uteis import numeros
# num = int(input('Digite um valor: '))
# print(f'O fatorial de {num} é {numeros.fatorial(num)}') #É necessário chamar o módulo durante a chamada da função, para evitar conflitos entre funções com mesmo nome em módulos diferentes
# print(f'O dobro de {num} é {numeros.dobro(num)}') 
# print(f'O fatorial de {num} é {numeros.triplo(num)}') 

#Desafios 107, 108, 109 e 110 estão na pasta Modulos_Proprios

#Desafio 111
#Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado
#Trasnfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando
from utilidadesCeV import moeda
# p = float(input('Digite o preço: R$'))
# print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, False)}')
# print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
# print(f'Aumentando 10% temos {moeda.aumentar(p, 10, True)}')
# print(f'Reduzindo 13% temos {moeda.diminuir(p, 10, True)}')
# moeda.resumo(p, 80, 35)

#Desafio 112
#Dentro do pacote utilidadesCeV que criamos no desafio 11(Aula 22), temos um módulo chamado dado.
#Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação
#de dados para aceitar apenas valores que sejam monetários
from utilidadesCeV import dado
p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22)