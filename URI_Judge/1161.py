def fatorial(a):
    prod = 1
    for i in range(1, a+1):
        prod *= i
    return prod

while True:
    try:
        a, b = input().split(' ')
        a = int(a)
        b = int(b)
        print(fatorial(a) + fatorial(b))
    except EOFError:
        break
