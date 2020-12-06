n = int(input())

for i in range(n):
    frase = input()
    meio = int(len(frase)/2-1)
    final = len(frase) - 1
    novaFrase = frase[meio::-1] + frase[final:meio:-1]
    print(novaFrase)