def bin2dec(number):
	st = 2
	return(all2dec(number, st))

def oct2dec(number):
    st = 8
    return(all2dec(number, st))


def hex2dec(number):
    st = 16
    return(all2dec(number, st))


def all2dec(number, st):
	number = str(number[::-1])
	dec = 0
	hexlit = ('a', 'b', 'c', 'd', 'e', 'f')
	for i in range(len(number)):
		if number[i] in hexlit:
		    dec += (hexlit.index(number[i]) + 10) * st ** i
		else:
		    dec += int(number[i]) * st ** i
	return(dec)


def dec2bin(number):
	st = 2
	return(dec2all(number, st))


def dec2oct(number):
    st = 8
    return(dec2all(number, st))


def dec2hex(number):
    st = 16
    return(dec2all(number, st))


def dec2all(number, ss):
	final = ''
	hexlit = ('a', 'b', 'c', 'd', 'e', 'f')
	while number != 0:
		if number % ss >=10:
			final += hexlit[(number % ss) - 10]
		else:
			final += str(number % ss)
		number = number // ss
	return(final[::-1])
	"""
		a = number % ss
		if a >= 10: 
			a = hexlit[a]
		dec.append(str(la))
		#dec.insert(0, str(a))
		number = number // ss
		dec_final = dec[::-1]
	return(''.join(dec_final))
	"""