from abc import ABCMeta, abstractmethod
import os
import json, pickle

class ParamHandlerException(Exception):
	def __init(self, *args):
		super().__init__(self, *args)


class ParamHandler(metaclass=ABCMeta):
	types = {}

	def __init__(self, source):
		self.source = source
		self.params = {}


	def add_param(self, key, value):
		self.params[key] = value


	def get_all_params(self):
		return self.params


	@abstractmethod
	def read(self):
		pass     
		"""Чтение из файла"""


	@abstractmethod
	def write(self):
		pass
		"""Запись в файл"""


	@classmethod
	def add_type(cls, name, klass):
 		if not name:
 			raise ParamHandlerException('Type must have a name!')
 		
 		if not issubclass(klass, ParamHandler):
 			raise ParamHandlerException(
				'Class "{}" is not ParamHandler!'.format(klass)
 			)
 		cls.types[name] = klass		


	@classmethod
	def get_instance(cls, source, *args, **kwargs):
 		_, ext = os.path.splitext(str(source).lower())
 		ext = ext.lstrip('.')
 		klass = cls.types.get(ext)

 		if klass is None:
 			raise ParamHandlerException('Type {} not found'.format(ext))

 		return klass(source, *args, **kwargs)


class JsonParamHandler(ParamHandler):
	def __init__(self, source):
		super().__init__(source)

	def read(self):
		with open(self.source) as f:
			result = json.load(f)
		return result
	"""
	Чтение из json файла и присвоение значений в self.params
	"""
	
	def write(self):
		with open(self.source, 'w') as f:
			json.dump(self.params, f)


class PickleParamHandler(ParamHandler):
	def __init__(self, source):
		super().__init__(source)

	def read(self):
		with open(self.source) as f:
			result = pickle.load(f)
		return result
	"""
	Чтение из pickle файла и присвоение значений в self.params
	"""
	
	def write(self):
		with open(self.source, 'w') as f:
			pickle.dump(self.params, f)

	"""
	Запись в формат pickle параметров self.params
	"""

if __name__=='main':
	ParamHandler.add_type("json", JsonParamHandler)
	ParamHandler.add_type("pickle", PickleParamHandler)

	p_config = ParamHandler.get_instance('.params.pickle')
	p_config.add_param('key1', 'val1')
	p_config.write()
	print(p_config.read())

	j_config = ParamHandler.get_instance('.params.json')
	j_config.add_param('key1', 'val1')
	j_config.write()
	print(j_config.read())
