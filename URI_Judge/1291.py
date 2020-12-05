from math import sin, cos
pi = 3.14159265358979323846
while True:
    try:
        a = float(input())
        
        areaTotal = a**2
        areaSemiCirculo = (pi * a**2)/4

        areaSetorCircular = areaSemiCirculo/3

        base = sin((15*pi)/180) * a * 2
        altura = cos((15*pi)/180) * a

        areaTriangular = (base * altura) / 2

        areaQuadrado = base ** 2

        areaSemiSetor = areaSetorCircular - areaTriangular

        s1 = areaSemiSetor * 4 + areaQuadrado

        print(f'{s1:.3f}', end=' ')

        areaFlor = (areaSemiCirculo - a**2/2 )*4 - (2 * s1)

        print(f'{areaFlor:.3f}', end=' ')

        areaRestante = areaTotal - areaFlor - s1 

        print(f'{areaRestante:.3f}')
    except EOFError:
        break