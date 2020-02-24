def prob(n, p, j):
    tent = p  # valor para calcular a diferença
    soma = 0
    for quant in range(1, n+1):
        if quant > 1:
            tent = (1-p) * tent

        soma += tent
        if j == quant:
            val = tent
    return val/soma


def valida(a, b, c):
    if (a, b, c >= 1) or (a, b, c <= 1000):
        return
    else:
        a, b, c = input().split(' ')
        a = int(a)
        b = float(b)
        c = int(c)
        return valida(a, b, c)


c = int(input()) # Casos
for vezes in range(c):
    n, p, j = input().split(' ')
    n = int(n)    # numero de jogadores
    p = float(p)  # probabilidade de vitoria
    j = int(j)    # indice do jogador (varia de 1 a n)

    valida(n, p, j)

    res = prob(n, p, j)
    print('{:.4f}'.format(res))
