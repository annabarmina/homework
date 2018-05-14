with open('data.txt') as f:
	a = format(f.read())
	b = list(a.split(' '))

	with open('out-1.txt', 'w') as f:
		n = int(input())
		for i in b:
			if int(i) % n == 0:
				f.write(i+' ')

	with open('out-2.txt', 'w') as f:
		p = int(input())
		for i in b:
			f.write(str(int(i) ** p)+' ')