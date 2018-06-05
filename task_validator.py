from abc import ABCMeta, abstractmethod
from datetime import datetime


class ValidatorException(Exception):
	pass

class Validator(metaclass=ABCMeta):
	types = {}

	@abstractmethod
	def validate(self, value):
		pass

	
	@classmethod
	def get_instance(cls, name):
		klass = cls.types.get(name)
		if klass is None:
			raise ValidatorException('Validator with name "{}" not found'.format(name))
		return klass()

	@classmethod
	def add_type(cls, name, klass):
		if not name:
			raise ValidatorException('Validator must have a name!')
		if not issubclass(klass, Validator):
			raise ValidatorException('Class "{}" is not Validator!'.format(klass))
		if name in Validator.types:
			raise ValidatorException('Class "{}" is already exists'.format(klass))
		Validator.types[name] = klass

class EMailValidator(Validator):
	"""проверяет корректность введенного email"""
	def validate(self, email):
		if '@' in email:
			return True
		else:
			return False

class DateTimeValidator(Validator):
	"""проверяет корректтность даты"""
	def validate(self, value):
		for key in ['%Y-%m-%d',
						'%Y-%m-%d %H:%M',
						'%Y-%m-%d %H:%M:%S',
						'%d.%m.%Y',
						'%d.%m.%Y %H:%M',
						'%d.%m.%Y %H:%M:%S',
						'%d/%m/%Y',
						'%d/%m/%Y %H:%M',
						'%d/%m/%Y %H:%M:%S']:
			try:
				if datetime.strptime(value, key):
					return True
			except:
				pass
		return False
		
Validator.add_type('email', EMailValidator)
Validator.add_type('datetime', DateTimeValidator)	

if __name__ == '__main__':
	value = Validator.get_instance('datetime')
	a = '10.12.1990'
	print(a, value.validate(a))