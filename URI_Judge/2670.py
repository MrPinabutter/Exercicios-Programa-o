n1 = int(input())
n2 = int(input())
n3 = int(input())

times = []
# primeiro andar
times.append(2*n2 + 4*n3)

# segundo andar
times.append(2*n1 + 2*n3)

# terceiro andar
times.append(4*n1 + 2*n2) 

print(min(times))
