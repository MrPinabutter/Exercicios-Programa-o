# Condição de existencia de um triangulo
def formtri(a, b, c):
    return (abs(a - b) < c < a + b) or (abs(a - c) < b < a + c) or (abs(b - c) < a < b + c)


# Verificação de valores no paramentro
def verifica(a, b, c, d):
    if (a, b, c, d >= 1) or (a, b, c, d <= 100):
        return
    else:
        a, b, c, d = input().split(' ')
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        return verifica(a, b, c, d)


a, b, c, d = input().split(' ')
a = int(a)
b = int(b)
c = int(c)
d = int(d)

verifica(a, b, c, d)
# Todas as possibilidades
if formtri(a, b, c) or formtri(a, b, d) or formtri(a, c, d) or formtri(b, c, d):
    print('S')
else:
    print('N')
