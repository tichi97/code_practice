class node:
	def __init__(self,data=None):
		self.data = data
		self.next = None

class linked_list:
	def __init__(self):
		self.head = node()

	# add new node to end
	def append(self,data):
		new_node = node(data)
		cur = self.head

		while cur.next!=None:
			cur = cur.next

		cur.next=new_node

	def length(self):
		cur =self.head
		total=0
		while cur.next!=None:
			total+=1
			cur = cur.next

		return total

	def display(self):
		elems = []
		cur = self.head
		while cur.next!=None:
			cur=cur.next
			elems.append(cur.data)
		print(elems)



my_list = linked_list()
my_list.display()
