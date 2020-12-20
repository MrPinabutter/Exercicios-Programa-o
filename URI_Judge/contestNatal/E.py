def isConectado(arestas, vertice, visitados=[], maxi=0):
    if vertice not in visitados:
        visitados.append(vertice)
    cop = arestas.copy()
    for vizinho in cop:
        if vertice in vizinho:
            if vertice == vizinho[1]:
                arestas.remove(vizinho)
                isConectado(cop, vizinho[0], visitados, maxi)
            else:
                arestas.remove(vizinho)
                isConectado(arestas, vizinho[1], visitados)
    return len(visitados) == maxi 

n, l = input().split(' ')

n = int(n)
l = int(l)

coords = []
for i in range(l):
    x, y = map(int, input().split(' '))
    coords.append((x, y)) 

print("COMPLETO" if isConectado(coords.copy(), 1, maxi=n) else "INCOMPLETO") 
