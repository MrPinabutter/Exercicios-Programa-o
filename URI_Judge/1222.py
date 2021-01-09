from math import ceil
while True:
  try:
    n, l, c = map(int, input().split(' '))
    palavras = input().split(' ')
    linhas = 1
    contLetras = 0
    for palavra in palavras:
      if len(palavra) + contLetras <= c:
        contLetras += len(palavra)
      else:
        contLetras = len(palavra)
        linhas += 1
    print(linhas)
  except EOFError:
    break
