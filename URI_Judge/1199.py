while(True):
    n = input()
    if '-' in n:
        break
    if 'x' in n:
        print(int(n, 16))
    else:
        hexa = f'{hex(int(n))}'
        new = ''
        for x in hexa:
            if x == 'a' or x == 'b' or x == 'c' or x == 'd' or x == 'e' or x == 'f':
                new += x.upper()
            else:
                new += x
        print(new)
