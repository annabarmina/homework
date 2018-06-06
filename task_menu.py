from abc import ABCMeta, abstractmethod


class CommandException(Exception):
	pass

class Command(metaclass=ABCMeta):
	@abstractmethod
	def execute(self, *args, **kwargs):
		pass

class ShowCommand(Command):
	def __init__(self, task_id):
		self.task_id = task_id

class ListCommand(Command):
	def __init__(self):
		pass

class AddCommand(Command):
	def __init__(self):
		pass

class DoneCommand(Command):
	def __init__(self):
		pass

class ReturnedCommand(Command):
	def __init__(self):
		pass

class Menu(metaclass=ABCMeta):

	def __init__(self):
		self.commands = {}
		self.counter = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self.counter < len(self.commands):
			command = list(self.commands.items())[self.counter]
			self.counter += 1
			return command
		else:
			#self.counter = 0
			raise StopIteration('No more!')

	
	#@classmethod
	def add_command(self, name, klass):
		if not name:
			raise CommandException('Command must have a name!')
		if not issubclass(klass, Command):
			raise CommandException('Class "{}" is not Command!'.format(klass))
		self.commands[name] = klass

	#@classmethod
	def execute(self, name, *args, **kwargs):
		command = self.commands.get(name)
		if command is None:
			raise CommandException('Command with name "{}" not found'.format(name))
		return command.execute(args, kwargs)

if __name__ == '__main__':
	menu = Menu()
	menu.add_command('show', ShowCommand)
	menu.add_command('done', DoneCommand)
	menu.add_command('returned', ReturnedCommand)
	menu.execute('show')
	menu.execute('show', 1, 2)
	menu.execute('done')
	#menu.execute('list')

	for i in menu:
		print(i)

	for name, command in menu:
		print(name, command)
		#print(command)