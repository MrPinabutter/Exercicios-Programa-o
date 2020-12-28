n = int(input())

for i in range(n):
    v = int(input())
    c = 0
    signal = 1
    for j in range(v):
        c += 1 * signal
        signal*=-1
    print(c)