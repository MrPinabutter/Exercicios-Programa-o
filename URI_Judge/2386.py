a = int(input())
n = int(input())

cont = 0
for i in range(n):
    fotons = int(input())
    if a * fotons >= 40000000:
        cont += 1

print(cont)