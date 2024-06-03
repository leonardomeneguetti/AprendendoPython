#No python, a String é tratada como um array de characteres

#Fatiamento

#Para pegar um char da String, basta usar como array
frase = 'Curso em Vídeo Python'
print(frase[9])
#Resposta: 'V'

#Para percorrer a string a partir do fim
print(frase[-1])
#Resposta: 'n'

#O python permite pegar um pedaço dessa string, "string[x:y]", indo de x(start) a y-1(end), não tem problema se final for 1 a mais que o tamanho da frase
print(frase[9:21])
#Resposta: 'Vídeo Python'

#Se x ou y não forem incluídos, o python identifica como x=0 ou y=len(string)
print(frase[15:])
#Resposta: 'Python'
print(frase[:5])
#Resposta: 'Curso em'

#Colocar String[x:y:z], retorna a sequencia do caractere x ao y-1, pulando z caracteres
print(frase[9:21:2])
#Resposta: 'VdoPto'

#Análise

#len(string) retorna a quantidade de caracteres de uma string
print(len(frase))
#Resposta: '21'

#string.count('seq_de_char') retorna quantas vezes uma sequencia de caracteres aparece na stringa, é case sensitive
print(frase.count('o'))
#Resposta: '3'
#E você pode fazer isso num pedaço específico da string: string.count('seq_de_char', x, y)
print(frase.count('o', 0, 13))
#Resposta: '1'

#string.find('seq_de_char') retorna em qual índice a sequencia de characteres começa ou -1 se não encontrar, é case sensitive
print(frase.find('deo'))
#Resposta: '11'

#'seq_de_char' in string retorna se a sequencia de characteres aparece ou não na string, é case sensitive
print('Curso' in frase)
#Resposta: True

#Transformação

#string.replace('seq_de_char1', 'seq_de_char2') substitui a sequencia de caracteres 1 pela 2, é case sensitive
print(frase.replace('Python', 'Android'))
#Respostaa: 'Curso em Vídeo Android'

#string.upper() faz todas as letras ficarem maiúsculas
print(frase.upper())
#Resposta: 'CURSO EM VÍDEO PYTHON'

#string.lower() faz todas as letras ficarem minúsculas
print(frase.lower())
#Resposta: 'curso em vídeo python'

#string.capitalize() faz a primeira letra ficar em maiúsculo e todas as outras em minúsculo
print(frase.capitalize())
#Resposta: 'Curso em vídeo python'

#string.title() faz a primeira letra ficar em maiúsculo e todas as outras em minúsculo, mas para cada palavra
print(frase.title())
#Resposta: 'Curso Em Vídeo Python'

fraseCmMtSpc = '          Curso em Vídeo Python      '
#string.strip() remove espaços no começo e no final da string
print(fraseCmMtSpc.strip())
#Resposta: 'Curso em Vídeo Python'
#string.rstrip() remove somente espaços no final da string
print(fraseCmMtSpc.rstrip())
#Resposta: '          Curso em Vídeo Python'
#string.lstrip() remove somente espaços no começo da string
print(fraseCmMtSpc.lstrip())
#Resposta: 'Curso em Vídeo Python      '

#Divisão

#string.split('separador', maxSplit) divide pelo separador a string em uma lista de strings
frase = frase.split()
print(frase) #por padrão, separa pelos espaços e não tem máximo
#Resposta: ['Curso', 'em', 'Vídeo', 'Python']

#Junção

#'separador'.join(string) junta uma lista de string pelo separador
print('-'.join(frase))
#Resposta: Curso-em-Vídeo-Python

#Curiosidade
#"""text""" pode ser colocado em várias linhas e manter sua formatação(\n, \t, \f, \r)
print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut feugiat metus, 
vel pellentesque ante. Phasellus commodo mauris nibh, in pretium sem accumsan quis. 
Morbi imperdiet bibendum elit, sed sodales velit luctus at. Proin cursus lacus eget 
justo viverra, porta imperdiet nisl feugiat. Curabitur suscipit purus vitae odio suscipit 
placerat. Proin ipsum nisi, gravida a mi at, ultricies mollis quam. Maecenas in turpis sit 
amet ipsum fringilla imperdiet ultrices eget dui. Pellentesque ultrices, libero at congue
dapibus, metus ante aliquet massa, at porttitor mauris nisi quis dui. Donec non orci eget libero eleifend
pharetra eget non ex.""")

#Desafio 22
#Crie um programa que leia o nome completo de uma pessoa e mostre:
nome = input('Digite seu nome completo: ').strip()

#a) O nome com todas as letras maiúsculas
print(f'Nome com tudo maiúsculo: {nome.upper()}')

#b) O nome com todas as letras minúsculas
print(f'Nome com tudo minúsculo: {nome.lower()}')

#c) Quantas letras ao todo, sem considerar os espaços
print(f'Letras sem espaço: {len(nome.replace(' ', ''))}')

#d) Quantas letras tem o primeiro nome
print(f'Letras n primeiro nome: {len(nome.split()[0])}')

#Desafio 23
#Faça um program que leia um numero de 0 a 9999 e mostre na tela cada um dos dígitos separados
#Matematicamente
n = int(input('Digite um numero de 0 a 9999: '))
mil = n//1000
resto = n%1000
cen = resto//100
resto = resto%100
dez = resto//10
uni = resto%10
print(f'Unidade: {uni}\nDezena: {dez}\nCentena: {cen}\nMilhar: {mil}')

#Por string
n = str(n)
print(f'Unidade: {n[3]}\nDezena: {n[2]}\nCentena: {n[1]}\nMilhar: {n[0]}')

#Desafio 24
#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome Santo
cidade = input('Digite uma cidade: ').strip()
print(f'{cidade} começa com \'Santo\'?: {'Santo' in cidade.split()[0]}')

#Desafio 25
#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = input('Digite seu nome: ').strip()
print(f'Tem \'Silva\' no nome? {'Silva' in nome}')

#Desafio 26
#Faça um programa que leia uma frase pelo teclado e mostre: 
frase = input('Digite uma frase: ').upper().strip

#a) Quantas vezes aparece a letra "A"
print(f'A letra \'A\' aparece {frase.count('A')} vezes')

#b) Em que posição ela aparece a primeira vez
print(f'A letra \'A\' aparece primeiro no índice {frase.find('A')+1}')

#c) Em que posição ela aparece a última vez
print(f'A letra \'A\' aparece por último no índice {frase.rfind('A')+1}')

#Desafio 27
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = input('Digite seu nome: ').strip()
listaNomes = nome.split()
print(f'O primeiro nome é {listaNomes[0]}')
print(f'O último nome é {listaNomes[len(listaNomes)-1]}')