#Desafio 111
def aumentar(n, pct, monet=False):
    n *= (1+pct/100)
    if monet == True:
        return moeda(n)
    return n
    
def diminuir(n, pct, monet=False):
    n *= (1-pct/100)
    if monet == True:
        return moeda(n)
    return n
    
def dobro(n, monet=False):
    n *= 2
    if monet == True:
        return moeda(n)
    return n
    
def metade(n, monet=False):
    n /= 2
    if monet == True:
        return moeda(n)
    return n

def moeda(n, moeda=False):
    return f'R${n:.2f}'

def resumo(n, amnt, dmnç):
    print('-' * 40)
    print(f'{'RESUMO DO VALOR':^40}')
    print('-' * 40)
    print(f'{'Preço analisado:':<30}', end='')
    print(f'{moeda(n):<10}')
    print(f'{'Dobro do preço:':<30}', end='')
    print(f'{dobro(n, True):<10}')
    print(f'{'Metade do preço:':<30}', end='')
    print(f'{metade(n, True):<10}')
    print(f'{amnt}{'% de aumento:':<28}', end='')
    print(f'{aumentar(n, amnt, True):<10}')
    print(f'{dmnç}{'% de redução:':<28}', end='')
    print(f'{diminuir(n, dmnç, True):<10}')
    print('-' * 40)