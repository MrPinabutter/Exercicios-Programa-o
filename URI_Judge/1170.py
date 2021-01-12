n = int(input())
for i in range(n):
    x = float(input())
    cont = 0
    while x > 1:
        cont += 1
        x = x / 2
    print(cont, 'dias')
