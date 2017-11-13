class queue(object):
	"""docstring for queue"""
	def __init__(self):
		self.item =[]

	def push(self,data):
		self.item.append(data)

	def pop(self):
		return self.item.pop(0)

	def size(self):
		return len(self.item)

	def peak(self):
		return self.item[0]

	def print_queue(self):
		print(self.item)

	def size(self):
		return len(self.item)

	def empty(self):
		del self.item[:]

	def is_empty(self):
		return self.item == []