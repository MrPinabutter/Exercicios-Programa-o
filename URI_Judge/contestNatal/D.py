n = int(input())
acts = input().split(' ')

acts = [int(x) for x in acts]
acts = sorted(acts)

gifts = 0
cont = 1
for idx, x in enumerate(acts):
    if idx == 0:
        ant = x
        gifts += cont
    elif x != ant:
        cont += 1
        gifts += cont
        ant = x
    else:
        gifts += cont
        ant = x
    
    

print(gifts)