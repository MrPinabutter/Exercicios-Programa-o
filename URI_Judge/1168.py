n = int(input())

for i in range(n):
    word = input()
    
    cont = 0
    for letter in word:
        if letter == '1':
            cont += 2
        if letter == '2':
            cont += 5
        if letter == '3':
            cont += 5
        if letter == '4':
            cont += 4
        if letter == '5':
            cont += 5
        if letter == '6':
            cont += 6
        if letter == '7':
            cont += 3
        if letter == '8':
            cont += 7
        if letter == '9':
            cont += 6
        if letter == '0':
            cont += 6
    print(f'{cont} leds')