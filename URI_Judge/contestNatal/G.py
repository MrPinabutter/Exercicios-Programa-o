def fatorial(n):
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1
    return fat

n = int(input())

for i in range(n):
    n, k, x = input().split(' ')
    n = int(n)
    k = int(k)
    x = int(x)

    falha = x / 100
    acerto = 1 - falha
    comb = fatorial(n)/(fatorial(k)*fatorial(n-k))

    chance = acerto**(n-k) * falha**(k) * comb * 100

    print(f'A chance de Basy acertar o numero no dia {i+1} eh {chance:.2f}%')



