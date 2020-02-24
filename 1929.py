# Condição de existencia de um triangulo
def formtri(a, b, c):
    return (abs(a - b) < c < a + b) and (abs(a - c) < b < a + c) and (abs(b - c) < a < b + c)


# Verificação de valores no paramentro
def verifica(a):
    if (a >= 1) or (a <= 100):
        return
    else:
        a = int(input('ERRO, digite novamente'))
        return verifica(a)


a = int(input('Digite o valor de A: '))
verifica(a)

b = int(input('Digite o valor de B: '))
verifica(b)

c = int(input('Digite o valor de C: '))
verifica(a)

d = int(input('Digite o valor de D: '))
verifica(b)

# Todas as possibilidades
if formtri(a, b, c) or formtri(a, b, d) or formtri(a, c, d) or formtri(b, c, d):
    print('S')
else:
    print('N')
