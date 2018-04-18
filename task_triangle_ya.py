a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
c1 = int(input())
c2 = int(input())
a = ((a1-b1)**2 + (a2-b2)**2)
b = ((b1-c1)**2 + (b2-c2)**2)
c = ((c1-a1)**2 + (c2-a2)**2)
if a + b == c or a + c == b or b + c == a:
  print('yes')
else: 
  print('no')
