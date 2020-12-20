n, l = input().split(' ')

n = int(n)
l = int(l)

coords = []
for i in range(l):
    x, y = input().split(' ')
    x = int(x)
    y = int(y)
    if (x, y) not in coords and (y, x) not in coords:
        coords.append((x, y)) 

def isConectado(arestas, vertice, visitados=[], maxi=0):
    visitados.append(vertice)
    cont = 0
    ver = True
    cop = arestas.copy()
    for vizinho in cop:
        if vertice in vizinho:
            cont += 1
            arestas.remove(vizinho)
            if vertice == vizinho[1]:
                isConectado(arestas, vizinho[0], visitados, maxi)
            else:
                isConectado(arestas, vizinho[1], visitados)
        if cont > 2:
            ver = False
    return len(visitados) == maxi and ver
print("COMPLETO" if isConectado(coords.copy(), 1, maxi=maximo) else "INCOMPLETO") 
