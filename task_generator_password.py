from string import ascii_letters, digits
import random

valid_values = list(digits + ascii_letters)

def password_generator(n):
	while 1:
		p = ''
		for i in range(n):
			p = p + random.choice(valid_values)
		yield p