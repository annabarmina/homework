from collections import namedtuple


def return_namedtuple(*cort):
	def decorator(func):
		def wrapper(*args, **kwargs):
			result = func(*args, **kwargs)
			if isinstance(result, tuple):
				ncort = namedtuple('ncort', list(cort))
			return ncort(*result)
		return wrapper
	return decorator
'''
@return_namedtuple('a', 'b', 'c')
def func():
    return 'Python', 'is', 'programming language'

r = func()
print(r.c)

@return_namedtuple('one', 'two')
def func():
    return 1, 2

r = func()
print(r.one) # 1
print(r.two) # 2
'''