from math import ceil
while True:
  try:
    n, l, c = map(int, input().split(' '))
    palavras = input().split(' ')
    linhas = 1
    contLetras = 0
    for palavra in palavras:
      if contLetras > 0:
        if len(palavra) + contLetras + 1 <= c:
          contLetras += len(palavra) + 1
        else:
          contLetras = len(palavra)
          linhas += 1
      else:
          if len(palavra) + contLetras <= c:
            contLetras += len(palavra)
          else:
            contLetras = len(palavra)
            linhas += 1
    print(ceil(linhas/l))
  except EOFError:
    break
