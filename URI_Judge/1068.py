while True:
    try:
        expressao = input()
        abre = 0
        fecha = 0

        fechouAntesDeAbrir = False

        for letra in expressao:
            if letra == '(':
                abre += 1
            if letra == ')':
                fecha += 1
            if fecha > abre:
                fechouAntesDeAbrir = True
        if fecha == abre and not fechouAntesDeAbrir:
            print('correct')
        else:
            print('incorrect') 
    except EOFError:
        break