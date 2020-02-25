# Função para encontrar um caminho até os ladrões
def caminho(lab, cords, ant_cord=[-1, -1]):
    # Posição atual
    a, b = cords

    # Verificação se alguma recurssiva encontrou a casa desejada
    ver = False

    # Impedir que o jogo continue com as casa iniciais ou finais obstruídas
    if lab[a][b] == '1':
        return False

    # Caso vitória inicia a volta da recursiva
    if a == 4 and b == 4:
        return True

    # Vitória dos COPS
    if ver:
        return True

    # Trajetória abaixo
    if a < 4:
        # Verifica se é possivel essa rota
        if lab[a + 1][b] == '0':
            # Impéde a visíta do bloco anterior
            if ant_cord[0] != a + 1 or ant_cord[1] != b:
                prox_cord = [a + 1, b]
                ver = caminho(lab, prox_cord, cords)
                # Quebra da recursiva
                return ver

    # Trajetória a direita
    if b < 4:
        if lab[a][b + 1] == '0':
            if ant_cord[0] != a or ant_cord[1] != b+1:
                prox_cord = [a, b + 1]
                ver = caminho(lab, prox_cord, cords)
                return ver

    # Trajetória a esquerda
    if b > 0:
        if lab[a][b - 1] == '0':
            if ant_cord[0] != a or ant_cord[1] != b - 1:
                prox_cord = [a, b - 1]
                ver = caminho(lab, prox_cord, cords)
                return ver

    # Trajetória acima
    if a > 0:
        if lab[a - 1][b] == '0':
            if ant_cord[0] != a - 1 or ant_cord[1] != b:
                prox_cord = [a - 1, b]
                ver = caminho(lab, prox_cord, cords)
                return ver

    # Vitória dos ROBBERS
    return False


caso = int(input('Digite a quantidade de casos: '))
cord = [0, 0]
for i in range(caso):
    lab = []
    for j in range(5):
        lista = input().split()
        lab.append(lista)
    if caminho(lab, cord):
        print('COPS')
    else:
        print('ROBBERS')
print()