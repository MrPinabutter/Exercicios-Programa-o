# Função para encontrar um caminho até os ladrões
def caminho(lab, cords, ant_cord=[-1, -1]):
    a, b = cords
    if lab[a][b] == '1':
        return False
    elif a == 4 and b == 4:
        return True

    if a < 4:   # Primeiro é tentado todos para baixo
        if lab[a + 1][b] == '0':
            prox_cord = [a + 1, b]
            return caminho(lab, prox_cord, cords)

    if b < 4:   # Tentado todos á direita
        if lab[a][b + 1] == '0':
            if ant_cord[0] != a or ant_cord[1] != b+1:
                prox_cord = [a, b + 1]
                return caminho(lab, prox_cord, cords)

    if b > 0:   # Tentado caminho á esquerda
        if lab[a][b - 1] == '0':
            prox_cord = [a, b - 1]
            return caminho(lab, prox_cord, cords)
        else:
            return False
    return False


caso = int(input())
cord = [0, 0]
for i in range(caso):
    lab = []
    input()
    for j in range(5):
        lista = input().split()
        lab.append(lista)
    if caminho(lab, cord):
        print('COPS')
    else:
        print('ROBBERS')
print()
