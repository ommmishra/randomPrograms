class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

class Tree:
	def __init__(self):
		self.headval = None

	def insert(self, val):
		
		

	def search(self, rootNode, val)
		current = rootNode
		if current.data is None:
			return "Not Found"
		elif data < current.data:
			current = current.left
			if current.data is None:
				return "Not Found"
			return search(current, val)
		elif  data > current.data
			current = current.right
			if current.data is None:
				return "Not Found"
			return search(current, val)
		else:
			print(str(val) + " Found")

