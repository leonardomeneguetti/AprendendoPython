#Dicionários são variaveis compostas mutáveis com índices literais, ou seja, os índices são identificados por palavras 
#Para declarar um dicionario, basta usar dicionário = {'índice':valor, 'índice':valor, 'índice':valor, ...}
dicionario1 = {'nome': 'Leonardo', 'idade': 20}
#ou
dicio = dict()
#Para acessar os dado, basta chamar o índice literal dicionário['índice']
print(dicionario1['nome'])
print(dicionario1['idade'])
print(f'O {dicionario1['nome']} tem {dicionario1['idade']} anos')
#Para adicionar mais dados no dicionário use dicionário['novo_indice'] = valor
dicionario1['sexo'] = 'M'
print(dicionario1)
#Para modificar um dos valores, use dicionário['indice'] = novo_valor
dicionario1['nome'] = 'Rogério'
print(dicionario1)
#Para remover elementos use del dicionário['índice']
#Considerando essa estrutura de dionário
filme1 = {'titulo': 'A lista de Schindler', 'ano': 1993, 'diretor': 'Steven Spielberg'}
#'titulo', 'ano' e 'diretor' são as chaves(keys)
#'A lista de Schindler', 1993 e 'Steven Spielberg' são os valores(values)
#Os dois conjuntos juntos são os itens(items)
#Você pode acessar os valores sem as chaves e vice-versa ou os itens completos
print(filme1.values())
print(filme1.keys())
print(filme1.items())
#Os dicionários são bem úteis em estruturas for, usando 
for key, value in filme1.items():
    print(f'O {key} é {value}')
#Também é possível colocar dicionários dentro de outras variáveis compostas
filme2 = {'titulo': 'Oldboy', 'ano': 2003, 'diretor': 'Park Chan-wook'}
filme3 = {'titulo': 'Vingadores: Ultimato', 'ano': 2019, 'diretor': 'Irmãos Russo'}
lista = list()
lista.append(filme1)
lista.append(filme2)
lista.append(filme3)
print(lista[0]['titulo'])
print(lista[2]['ano'])
print(lista[1]['diretor'])

#Quando for reutilizar um mesmo dicionário no for, tem q usar a função dicionário.copy() no append, para não lincar o dicionário com a lista, mas sim copiá-lo
#Jeito errado
estado = {}
brasil = []
for c in range(0,3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado)
print(brasil)

#Jeito certo
estado = {}
brasil = []
for c in range(0,3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())
print(brasil)

#Desafio 90
#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
aluno = {}
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'
print('-'*30)
print(f'Nome: {aluno["nome"]}')
print(f'Média: {aluno["media"]}')
print(f'Situação: {aluno["situacao"]}')

#Desafio 91
#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aletórios. Guarde esses resultados em um dicionário.
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1,6), 
        'jogador2': randint(1,6), 
        'jogador3': randint(1,6), 
        'jogador4': randint(1,6)}

print('Valore sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(0.25)

ranking = {}
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for pos, i in enumerate(ranking):
    print(f'{pos+1}º lugar: {i[0]} com {i[1]}')

#Desafio 92
#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário.
#Se a CTPS for diferente de zero, o dicionário também receberá o ano de contratação e o salário.
#Calcule e acrescente, além da idade, com quanos anos a pessoa vai se aposentar
from datetime import date

pessoa = {}
print('Informe:')
pessoa['nome'] = input('Nome: ')
pessoa['idade'] = date.today().year - int(input('Ano de nascimento: '))
pessoa['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$'))
    anoQAposenta = pessoa['contratacao'] + 35
    nascimento = date.today().year - pessoa['idade']
    pessoa['aposentadoria'] = anoQAposenta - nascimento

for k, v in pessoa.items():
    print(f'{str(k).capitalize()}: {v}')

#Desafio 93
#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador, quantas partidas ele jogou.
#Depois vai ler a quantidade de gols por partida. No final, tudo isso será guardado em um dicionário, incluíndo o total de gols feitos durante o campeonato
jogador = {}
jogador['nome'] = input('Nome: ')
qtdPartidas = int(input('Partidas jogadas: '))
jogador['Gols'] = list()
jogador['totalGol'] = 0
for i in range(0, qtdPartidas):
    gols = int(input(f'Gols feitos na {i+1}ª partida: '))
    jogador['totalGol'] += gols
    jogador['Gols'].append(gols)

print('='*40)
print(f'O jogador {jogador["nome"].capitalize()} jogou {len(jogador["Gols"])} partidas')
for i in range(0, len(jogador["Gols"])):
    print(f'Na partida {i+1}, fez {jogador["Gols"][i]} gols')
print(f'Fez um total de {jogador["totalGol"]} gols')

#Desafio 94
#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados em um dicionário e
#todos os dicionários em uma lista. No final, mostre: 
pessoas = []
pessoa = {}
soma = 0
while True:
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo: [M/F] ')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    pessoas.append(pessoa.copy())
    r = input('Deseja continuar? [S/N] ')
    if r in 'Nn':
        break

#a) Quantas pessoas foram cadastradas
print(f'Foram cadastradas {len(pessoas)} pessoas')

#b) A média de idade do grupo
media = soma/len(pessoas)
print(f'A média de idade é {media} anos')

#c) Uma lista com todas as mulheres
print('As mulheres cadastradas foram', end=' ')
for i in pessoas:
    if i['sexo'] in 'Ff':
        print(f'{i['nome']}', end=' ')
print()

#d) Uma lista com todas as pessoas com idade acima da média
print('As pessoas com idade acima da média foram', end=' ')
for i in pessoas:
    if i['idade'] > media:
        print(f'{i['nome']}', end=' ')

#Desafio 95
#Aprimore o desafio 93(Aula 19) para que ele funcione com vários jogadores, incluindo um sistema de visualização de 
#detalhes do rendimento de cada jogador
time = []
jogador = {}
while True:
    jogador['nome'] = input('Nome: ')
    qtdPartidas = int(input('Partidas jogadas: '))
    jogador['gols'] = list()
    jogador['total'] = 0
    for i in range(0, qtdPartidas):
        gols = int(input(f'Gols feitos na {i+1}ª partida: '))
        jogador['total'] += gols
        jogador['gols'].append(gols)
    time.append(jogador.copy())
    r = input('Deseja continuar? [S/N] ')
    if r in 'Nn':
        break

print('-='*30)
print(f'{'Cod '}', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k+1:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para) '))-1
    if busca == 999:
        break
    if busca >= len(time):
        print('Não existe jogador com esse código')
    else:
        print(f'Levantamento do jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'No jogo {i+1} fez {g} gols.')
