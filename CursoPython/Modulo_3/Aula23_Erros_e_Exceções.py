#Erros no python são os erros sintáticos, que são acusados pela IDE, ou seja, erros de digitação
#Também podem ser erros de lógica, que apenas com teste podem ser identificados
#Exceção é o nome dado aos diversos possíveis erros de semântica do python, alguns exemplos de exceções

#print(x)
#Exceção: "NameError: name 'x' is not defined"

n = int(input('Numero: ')) #Se for digitado algo que nã é um int
print(n)
#Exceção: "ValueError: invalid literal for int() with base 10: 'oito'"

a = int(input('Numerador: '))
b = int(input('Denominador: ')) #Se for digitado 0 para a variável b
r = a / b
print(r)
#Exceção: "ZeroDivisionError: division by zero"

a = 2
b = '2'
r = a / b
print(r)
#Exceção: "TypeError: unsupported operand type(s) for /: 'int' and 'str'"

lst = [1, 2, 3]
print(lst[3])
#Exceção: "IndexError: list index out of range"

#import uteis #Esse módulo só existem em outra pasta
#Exceção: "ModuleNotFoundError: No module named 'uteis'"

#Para tratar os diferentes tipos de exceções do python, use a estrutura
#try:
#    operação_que_gera_exceção
#except Classe_da_Exceção: (Pode aparecer repetidas vezes)
#    operação_caso_ocorra_exceção
#else: (opcional)
#    operação_caso_não_ocorra_exceção
#finally:
#    operação_que_vai_ocorrer_sempre

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: ')) #Se for digitado 0 para a variável b
    r = a / b
except (TypeError, ValueError):
    print('ERRO: Tivemos um problema com os tipos de dados digitados')
except ZeroDivisionError:
    print('ERRO: Não é possível dividir um número por 0')
except KeyboardInterrupt:
    print('ERRO: O usuário preferiu não informar os dados')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally: 
    print('Obrigado! Volte Sempre :)')

#Desafio 113
#Reescreva a função leiaInt() que fizemos no desafio 104(Aula 21), incluindo agora a possibilidade da digitação de um númerod e tipo inválido.
#Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('\033[0;31mERRO! Digite um valor inteiro válido\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mUsuário preferio não digitar esse número\033[m')
            return 0
        else: 
            return n
        
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print('\033[0;31mERRO! Digite um valor válido\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mUsuário preferio não digitar esse número\033[m')
            return 0
        else: 
            return n

n = leiaInt('Digite um número Inteiro: ')
f = leiaFloat('Digite um número Real: ')
print(f'Você acabou de digitar o número inteiro \"{n}\" e o número real \"{f}\"')

#Desafio 114
#Crie um código em Python que teste se o site Pudim está acessível pelo computador usado
import urllib.error
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[0;31mO site Pudim não está acessível no momento.\033[m')
else:
    print('\033[0;32mConsegui acessar o site Pudim com sucesso!\033[m')