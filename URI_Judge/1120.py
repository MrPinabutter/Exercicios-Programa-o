while(True):
    dig, num = input().split(' ')
    if dig == "0" and num == "0":
        break
    new = ''
    ver = True
    for i in num:
        if i == dig:
            continue
        if ver and i == '0':
            continue
        ver = False
        new += i
    
    print(new if new != '' else 0)