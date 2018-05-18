'''
def fibonacci(n):
  #fib = [1 for i in range(0,2)]
  #fib = [(fib[i-1] + fib[i-2]) for i in range(2,n)]
  fib = [1 if i < 2
  		(fib[i-1] + fib[i-2]) if i>2 for i in range(n)]
  #for i in range(2,n):
  #	fib.append(fib[i-1] + fib[i-2])
  return(fib)
'''
def fibonacci(n):
	a = 1
	b = 1
	for i in range(n):
		yield a
		a, b = b, a + b

#for i in fibonacci(10):
#	print(i)

