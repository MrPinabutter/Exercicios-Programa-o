n = int(input())
c = 0
duendes = []
while c < n:
    teste = input()
    if teste != '':
        nome, idade = teste.split(' ')
        duendes.append((nome, int(idade)))
        c += 1

# Ordenando tudo por nome
duendes.sort(key=lambda x: x[0])

# Ordenando tudo por idade
duendes.sort(key=lambda x: x[1], reverse=True)

# Separação de grupos
vezes = int(len(duendes)/3)
for y in range(vezes):
    print(f"Time {y+1}")
    for i in range(y, len(duendes), vezes):
        print(duendes[i][0], duendes[i][1])
    print()

