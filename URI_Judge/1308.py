n = int(input())

for i in range(n):
    try:
        num = int(input())
        val = (num - 1) * 2

        x = (3**2)-(4*(-val))
        x = x**(1/2)
        x1=(-3+x)/2

        print(int(x1)+1)        

    except EOFError:
        break 
