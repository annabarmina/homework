from collections import namedtuple

def return_namedtuple(*cort):
	def decorator(func):
		def wrapper(*args, **kwargs):
			result = func(*args)
			if isinstance(result, tuple):
				ncort = namedtuple('ncort', cort)
				namedcort = ncort(*result)
			return namedcort
		return wrapper
	return decorator
'''
@return_namedtuple('a', 'b', 'c')
def func():
    return 'Python', 'is', 'programming language'

r = func()
print(r.c)
'''