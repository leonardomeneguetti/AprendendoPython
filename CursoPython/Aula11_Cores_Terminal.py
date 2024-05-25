#O python permite alterar as cores no terminal sem bibliotecas, só precisa digitar
#\033[style;text;backm
print('\033[0;33;44mTeste\033[m')

#style pode ser:
#0 para nenhum
#1 para bold
#4 para underline
#7 para negative

#text pode ser: 
#30 para branco
#31 para vermelho
#32 para verde
#33 para amarelo
#34 para azul
#35 para magenta
#36 para ciano
#37 para cinza

#back pode ser: 
#40 para branco
#41 para vermelho
#42 para verde
#43 para amarelo
#44 para azul
#45 para magenta
#46 para ciano
#47 para cinza

print('\033[0;30;41mOlá mundo!\033[m')
print('\033[4;33;44mOlá mundo!\033[m')
print('\033[1;35;43mOlá mundo!\033[m')
print('\033[30;42mOlá mundo!\033[m')
print('\033[mOlá mundo!\033[m')
print('\033[7;30mOlá mundo!\033[m')