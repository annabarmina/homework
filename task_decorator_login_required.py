import hashlib

def make_token(username, password):
	s = username + password
	return hashlib.md5(s.encode()).hexdigest()

def login_required(func):
	def wrapper(*args, **kwargs):
		with open('token.txt', 'r') as f:
			token = f.read()
		tr = 3
		n = 0
		while tr:
			login = input('Введите логин: ')
			passw = input('Введите пароль: ')
			login_passw = make_token(login, passw)

			if login_passw == token:
				n = 1
				break
			tr -= 1
				
		if n == 1:
			return func(*args, **kwargs)
		else:
			return None
	return wrapper