while(True):
  n = int(input())
  if n == 0:
    break
  sumTot = 0
  sumIncorrect = 0
  uniqueCorrects = 0
  lastOut = {}
  problemsSolved = ''
  for i in range(n):
    letter, num, isCorrect = input().split(' ')
    num = int(num)
    lastOut[letter] = [isCorrect, lastOut[letter][1] if lastOut.get(letter) else 0]
    if isCorrect == 'correct':
      if letter not in problemsSolved:
        sumTot += num
        uniqueCorrects+=1
        problemsSolved += letter
    else:
      lastOut[letter] = [isCorrect, 20 + lastOut[letter][1] if lastOut.get(letter) else 20]
  for item, value in lastOut.items():
    if value[0] == 'correct':
      sumTot += value[1]
  print(uniqueCorrects, sumTot)

