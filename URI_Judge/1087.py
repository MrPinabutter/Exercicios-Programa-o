def minimoMov(rx, ry, x, y):
    if rx == x and ry == y:
        return 0
    if rx == x or ry == y:
        return 1
    if tanadiagonal(rx, ry, x, y):
        return 1
    else:
        return 2


# Verifica se as coordenadas estão em diagonal
def tanadiagonal(rx, ry, x, y):
    ax = rx
    ay = ry
    while ax != 0 and ay != 0:
        if ax == x and ay == y:
            return True
        else:
            ax = ax - 1
            ay = ay - 1

    ax = rx
    ay = ry
    while ax != 9 and ay != 9:
        if ax == x and ay == y:
            return True
        else:
            ax = ax + 1
            ay = ay + 1

    ax = rx
    ay = ry
    while ax != 0 and ay != 9:
        if ax == x and ay == y:
            return True
        else:
            ax = ax - 1
            ay = ay + 1

    ax = rx
    ay = ry
    while ax != 9 and ay != 0:
        if ax == x and ay == y:
            return True
        else:
            ax = ax + 1
            ay = ay - 1
    return False


while True:
    qx, qy, x, y = input().split()
    qx = int(qx)
    qy = int(qy)
    x = int(x)
    y = int(y)
    if qx == qy == x == y == 0:
        break
    print(minimoMov(qx, qy, x, y))
