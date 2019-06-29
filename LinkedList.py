class Node:
	def __init__(self, dataval):
		self.dataval =dataval
		self.nextval =None

class LinkedList:
	def __init__(self):
		self.headval =None

	def printList(self):
		printval = self.headval
		while printval is not None:
			print(printval.dataval)
			printval = printval.nextval
	
	def insertAtBegining(self, newdata):
		newNode = Node(newdata)
		newNode.nextval = self.headval
		self.headval = newNode

	def insertAtEnd(self, data):
		newNode = Node(data)
		if(self.headval is None):
			self.headval = newNode
		else:
			last = self.headval
			while last.nextval is not None:
				last = last.nextval
			last.nextval = newNode

	
list1= LinkedList()
x = Node(1)
list1.headval = x
list1.headval.nextval = Node(2)
list1.insertAtBegining(3)
list1.insertAtEnd(5)
list1.printList()