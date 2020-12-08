while True:
    try:
        a, b = input().split(' ')
        a0, a1, a2, a3, a4, a5, a6, a7, a8, a9 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        for i in range(int(a), int(b) + 1):
            a0 += str(i).count('0')
            a1 += str(i).count('1')
            a2 += str(i).count('2')
            a3 += str(i).count('3')
            a4 += str(i).count('4')
            a5 += str(i).count('5')
            a6 += str(i).count('6')
            a7 += str(i).count('7')
            a8 += str(i).count('8')
            a9 += str(i).count('9')
        print(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9)
    except EOFError:
        break


