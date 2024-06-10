#Interactive help - usando a função help() no console do python, muda o console, abrindo um menu de ajuda.
#Nesse menu de ajuda, você pode digitar qualquer função ou biblioteca do python, e irá mostrar a documentação completa dela.
#Para sair do menu ajuda, digite quit
help(print) #No VSCode só funciona assim
print(print.__doc__) #Outra forma de trazer a documentação de uma função

#Docstrings - forma de documentar as funções criadas por você, para ajudar outros devs a entender os parâmetros
def contador(i, f, p):
    #As docstrings são escritas na linha logo abaixo de def, e ficam entre aspas duplas, se o objetivo é realmente criar 
    #uma biblioteca para outros usarem, escreva em inglês
    """
        -> Faz uma contagem e mostra na tela
        :param i: início da contagem
        :param f: fim da contagem
        :para p: passo da contagem
        :retur: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')

help(contador) #Com a docstring, o comando help mostra toda a documentação que você criou para a função

#Parâmetros opcionais - Faz exatamente o que o nome implica, se uma funão recebe menos parâmetros do que ela espera, ela ainda funciona
#É possível fazer isso colocando um valor padrão para a variável
def somar(a=0,b=0,c=0): #Colocando c=0, se a chamada não enviar 3 parâmntros, o terceiro recebe um valor padrão
    s = a + b + c
    print(f'A soma vale {s}')

somar(3,2,5)
somar(8,4)

#Escopo de variáveis - Existem variáveis globais e variáveis locais, as globais funcionam no programa todo
#As locais funcionam dentro do if, ou dentro da função onde foram criadas
def teste(b):
    global a #Se for colocado assim, qualquer modificação feita a essa variável ocorre globalmente
    a = 8 #Sem o atributo global, tem o mesmo nome que a variável global, mas são completamente diferentes, com o atributo global, altera a variável global
    b += 4 #A alteração aqui, não interfere na global
    c = 2 #Só existe dentro da função
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5 #Variável global
teste(a)
print(f'A fora vale {a}')

#Funções com retorno - A função return variável permite que uma função retorne um valor ao final de sua execução
def somar(a=0,b=0,c=0): #Colocando c=0, se a chamada não enviar 3 parâmntros, o terceiro recebe um valor padrão
    s = a + b + c
    return s

r1 = somar(3,2,5)
r2 = somar(8,4)
r3 = somar(7)
print(f'Os cálculos feitos deram {r1}, {r2} e {r3}')

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

def parOuImpar(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    
n = int(input('Digite um número: '))
if parOuImpar(n):
    print('É par')
else:
    print('Não é ímpar')

#Desafio 101
#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
#retornando um valor literal indicando se essa pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições
def voto(ano):
    from datetime import date #Importa só pra função
    idade = date.today().year - ano
    if  18 <= idade <= 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif idade >= 16 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else: 
        return f'Com {idade} anos: NÃO VOTA'
    
print('-'*40)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))

#Desafio 102
#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular
#e o outro chamado show, que será um valor lógico opcional indicando se será mostrado ou não o cálculo do fatorial
def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor fatorial de um número n
    """
    f = 1
    for i in range(n, 0, -1):
        f *= i
        if show:
            if i > 1:
                print(f'{i} x', end=' ')
            else:
                print(f'{i} =', end=' ')
    return f
    
help(fatorial)
print('-'*40)
print(fatorial(6, True))

#Desafio 103
#faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros: o nome de um jogador e quantos gols ele marcou
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente
def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

nome = input('Nome do jogador: ').strip()
gols = input('Número de gols: ').strip()
ficha(nome, gols)

#Desafio 104
#Crie um programa que tenha uma função leiaInt(), que vai funcionar de forma semelhante à função input(),
#só que vazendo a validação para aceitar apenas um valor numérico.
def leiaInt(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            return n
        print('\033[0;31mERRO! Digite um número inteiro válido\033[m')

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

#Desafio 105
#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#- Quantidade de notas
#- A maior nota
#- A menor nota
#- A média da turma
#- A situação (opcional)
#Adiciona também as docstrings
def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos;
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: (opcional) indica se deve ou não adicionar situação
    :retur: dicionário com quantidade de notas, maior nota, menor nota, média da turma e (opcional) situação da turma
    """
    notas = dict()
    notas['total'] = len(n)
    s = 0
    for pos, i in enumerate(n):
        if pos == 0:
            notas['maior'] = i
            notas['menor'] = i
        else:
            if i > notas['maior']:
                notas['maior'] = i
            if i < notas['menor']:
                notas['menor'] = i
        s += i
    notas['media'] = s/notas['total']
    if sit:
        if notas['media'] >= 7:
            notas['situacao'] = 'BOA'
        elif notas['media'] >= 6:
            notas['situacao'] = 'RAZOÁVEL'
        else:
            notas['situacao'] = 'RUIM'
    return notas

resp = notas(5.5, 9.5, 10, 6.5, 2, 7, 4)
print(resp)
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
resp = notas(3.5, 10, 6.5, sit=True)
print(resp)
resp = notas(3.5, 2, 6.5, sit=True)
print(resp)
help(notas)

#Desafio 106
#Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
#Quando ao usuário digitar FIM, o progrma encerrará.
from time import sleep
while True:
    print('Sistema de ajuda PyHelp')
    cmd = input('Função ou biblioteca > ')
    if cmd in 'FIMfim':
        break
    print(f'Acessando o manual do comando {cmd}...')
    sleep(1)
    help(cmd)