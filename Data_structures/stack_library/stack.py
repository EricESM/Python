class stack:
	"""docstring for stack"""
	def __init__(self, data_size = None):
		if data_size == None:
			self.item =[]
		else:
			self.item[size]

	def print_stack(self):
		print(self.item)

	def size(self):
		return len(self.item)

	def push(self,data):
		self.item.append(data)
		
	def pop(self):
		return self.item.pop()

	def empty(self):
		del self.item[:]

	def is_empty(self):
		return self.item == []

	def peak(self):
		return self.item[len(self.item)-1]
