n = int(input())

bon = 0 # a cada 8
arq = 0 # a cada 4
mus = 0 # a cada 6
des = 0 # a cada 12

for i in range(n):
    nome, tipo, hora = input().split(' ')
    hora = int(hora)
    if tipo == 'bonecos':
        bon += hora
    elif tipo == 'arquitetos':
        arq += hora
    elif tipo == 'musicos':
        mus += hora
    elif tipo == 'desenhistas':
        des += hora

brinquedos = int(bon/8) + int(arq/4) + int(mus/6) + int(des/12)
print(brinquedos)