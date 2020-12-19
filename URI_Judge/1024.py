times = int(input())
for i in range(times):
    word = input()

    stepOne = ''
    for letter in word:
        if (ord(letter) >= 65 and ord(letter) <=90) or (ord(letter) >= 97 and ord(letter) <= 122): 
            stepOne += chr(ord(letter)+3)
        else:
            stepOne += letter

    stepTwo = stepOne[::-1]

    stepThree = ''
    n = int(len(stepTwo)/2)

    for idx, letter in enumerate(stepTwo):
        if idx + 1 > n:
            stepThree += chr(ord(letter)-1)
        else:
            stepThree += letter

    print(stepThree)