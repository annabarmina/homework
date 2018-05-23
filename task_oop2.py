from abc import ABCMeta, abstractmethod

class Course(object):
	
	def __init__(self, name, duration):
		self.__name = name
		self.__duration = duration

class Person(object):
	__slots__ = ('__firstname', '__lastname')

	def __init__(self, firstname, lastname):
		self.__firstname = firstname
		self.__lastname = lastname

	def get_full_name(self):

class Teacher(Person):
	def __init__(self, id_teacher, specialization, course)

	def add_teacher(self)

	def add_specialization(self)

	def add_course(Course)

	def add_group(Students_Group)

class Students(Person):
	def __init__(self, id_student, id_group)

	def add_group(Students_Group)


class Students_Group(object):
	__slot__ = ('id_group',)

	def __init(self, id_group)

	def add_group(self)

	def add_student(Students)

