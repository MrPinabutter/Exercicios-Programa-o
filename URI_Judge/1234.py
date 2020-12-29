while True:
    try:
        string = input()
        newString = ''
        ver = True
        for letter in string:
            if letter != ' ':
                if ver:
                    newString += letter.upper()
                else:
                    newString += letter.lower()
                ver = not ver
            else:
                newString += letter
        print(newString)
    except EOFError:
        break
