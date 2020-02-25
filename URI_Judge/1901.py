tam = int(input()) # Tamanho da floresta
lista = []
floresta = []

# Preenchendo a lista
for i in range(tam):
    lista = input().split()
    floresta.append(lista)

visitadas = []

# Descobrindo as coordenadas
for i in range(2*tam):
    a, b = input().split()
    a = int(a)-1
    b = int(b)-1
    if floresta[a][b] not in visitadas: # Evita repetições
        visitadas.append(floresta[a][b])

# Contando valores
print(len(visitadas))