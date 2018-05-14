from string import ascii_lowercase, ascii_uppercase


change_values = str(ascii_lowercase)
change_values_u = str(ascii_uppercase)

def encode(s, ROTn):
	code = []
	#s = s.lower()
	for i in s:
		if i in change_values:
			new = change_values.find(i)+ROTn
			if new<26:
				code.append(change_values[new])
			else:
				code.append(change_values[new-26])
		elif i in change_values_u:
			new = change_values_u.find(i)+ROTn
			if new<26:
				code.append(change_values_u[new])
			else:
				code.append(change_values_u[new-26])
		else:
			code.append(i)
	return(''.join(code))
#encode('Hello, Python3!', 1)


def decode(s, ROTn):
	code = []
	for i in s:
		if i in change_values:
			new = change_values.find(i)-ROTn
			if new>=0:
				code.append(change_values[new])
			else:
				#code.append(25+new)
				code.append(change_values[26+new])
		elif i in change_values_u:
			new = change_values_u.find(i)-ROTn
			if new>=0:
				#code.append(26+new)
				code.append(change_values_u[new])
			else:
				#code.append(25+new)
				code.append(change_values_u[26+new])
		else:
			code.append(i)
	#print(code)
	return(''.join(code))
#decode("Gur pyrnare naq avpre gur cebtenz, gur snfgre vg'f tbvat gb eha. Naq vs vg qbrfa'g, vg'yy or rnfl gb znxr vg snfg", 13)