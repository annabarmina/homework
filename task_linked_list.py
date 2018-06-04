class Node(object):
	'''определение элемента списка'''
	def __init__(self, value = None, next = None):
		self.value = value
		self.next = next

class LinkedList(object):
	'''определение связного списка'''
	def __init__(self, *args):
		self.first = None
		self.last = None
		self.length = 0

	def __str__(self):
		'''распечатка содержимого списка'''
		if self.first != None:
			current = self.first
			out = 'LinkedList [' + str(current.value)
			while current.next != None:
				current = current.next
				out += ', ' + str(current.value)
			return out +']'
		return 'LinkedList []'

	def clear(self):
		'''очистка списка'''
		self.__init__()

	def add(self, value):
		''' добавление элемента в конец спсика'''
		self.length += 1
		''' если список был пустой'''
		if self.first == None:
			self.last = self.first = Node(value, None)
		else:
			self.last.next = self.last = Node(value, None)

	def insert(self, index, value):
		'''добавляет элемент в указанную позицию, последующие элементы сдвигаются. 
		Если индекс больше или равен длине списка, то добавлять элемент в конец списка'''
		if self.first == None:
			self.last = self.first = Node(value, None)
			return
		if self.index == 0:
			self.first = Node(value, self.first)
			return
		curr=self.first
		count=0
		while curr:
			count += 1
			if count == index:
				curr.next = Node(value, curr.next)
				if curr.next.next == None:
					self.last = curr.next
				break
			curr = curr.next

	def get(self, index):
		'''возвращает значение элемента с указанным индексом. 
		Если индекс больше или равен длине списка, то выбросить исключение IndexError'''
		if self.first!= None:
			curr = self.first
			count = 0
			while curr != None:		
				if count == index:
					return curr.value
				count += 1
				

	def is_empty(self):
		if self.length() == 0:
			return True
		return False

	def len(self):
		self.length = 0
		if self.first!= None:
			self.length +=1
			curr = self.first
			while curr:
				curr = curr.next
				self.length += 1
		return self.length

'''	
L = LinkedList(1, 2, 3)
print(L)

L.add(1)
L.add(3)
L.add(6)
L.add(3)
L.insert(1, 4)


print(L)
print(L.last.value)
print(L.first.value)
print(L.length)
'''
