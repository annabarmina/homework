i = int(input())
if i % 4 != 0 or (i % 100 == 0 and i % 400 != 0):
  print('no')
else: print('yes')
