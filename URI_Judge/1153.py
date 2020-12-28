n = int(input())

c = 1
total = 1
for i in range(1, n+1):
    total *= c
    c+=1
print(total)