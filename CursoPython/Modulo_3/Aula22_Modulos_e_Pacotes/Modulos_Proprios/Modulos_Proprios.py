#Modularização é o ato de dividir o programa em módulos, diferentes arquivos com funções com o mesmo tema/propósito
#O objetivo final da modularização é facilitar o entendimento, a manutenção do código, a organização e a reutilização do código
#Pro python, todo arquivo .py é um módulo, então para chamar um arquivo criado por você, com suas funções, é só usar import nome_do_aruivo_sem_.py

import uteis #Fazendo o import do arquvio uteis.py
num = int(input('Digite um valor: '))
print(f'O fatorial de {num} é {uteis.fatorial(num)}') #É necessário chamar o módulo durante a chamada da função, para evitar conflitos entre funções com mesmo nome em módulos diferentes
print(f'O dobro de {num} é {uteis.dobro(num)}') 
print(f'O fatorial de {num} é {uteis.triplo(num)}') 

#Desafio 107
#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade()
#Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda
p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é R${moeda.metade(p):.2f}')
print(f'O dobro de {p} é R${moeda.dobro(p):.2f}')
print(f'Aumentando 10% temos R${moeda.aumentar(p, 10):.2f}')
print(f'Reduzindo 13% temos R${moeda.diminuir(p, 13):.2f}')

#Desafio 108
#Adapte o código do desafio 107(Aula 22), criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário
p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10% temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Reduzindo 13% temos {moeda.moeda(moeda.diminuir(p, 10))}')

#Desafio 109
#Modifique as funções que foram criadas no desafio 107(Aula 22) para que elas aceitem um parâmetro a mais,
#informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108(Aula 22)
p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, False)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10% temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13% temos {moeda.diminuir(p, 10, True)}')

#Desafio 110
#Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações
#geradas pelas funções que já temos no módulo criado até aqui
p = float(input('Digite o preço: R$'))
moeda.resumo(p, 80, 35)

#Desafios 111 e 112 estão na pasta Pacotes