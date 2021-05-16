n = int(input())
# buffer
input()
for i in range(n):
  arv = {}
  tot = 0
  while(True):
    try:
      arvore = input()
      if not arvore:
        break
      tot += 1
      if arv.get(arvore):
        arv[arvore] = arv[arvore] + 1 
      else: 
        arv[arvore] = 1
    except EOFError:
        break

  arv_sort = sorted(arv)

  for k in arv_sort:
    print(k, f'{arv[k]*100/tot:.4f}')
  
  if i != n-1:
    print()