class node:
	def __init__(self,data):
		self.data = data
		self.next = None

class linked_list:
	def __init__(self):
		self.head = node(None)

	# add new node to end
	def append(self,data):
		new_node = node(data)
		cur = self.head

		while cur.next!=None:
			cur = cur.next

		cur.next=new_node

	def prepend(self,data):
		new_node = node(data)
		new_node.next=self.head.next
		self.head.next = new_node

	def insert_between(self,data,pos):
		new_node = node(data)
		cur=self.head

		while cur.next!=None:
			cur=cur.next
			if cur.data==pos:
				new_node.next=cur.next
				cur.next=new_node
				return

		print('Not found!')



		

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

	def get(self,index):
		if index>=self.length():
			print "ERROR: 'Get' Index out of range'"
			return None

		cur_index=0
		cur_node=self.head

		while True:
			cur_node = cur_node.next
			if cur_index==index: return cur_node.data
			cur_index+=1

	def erase(self,index):
		if index>=self.length():
			print "ERROR: 'Erase' Index out of range'"
			return 
		cur_index=0
		cur_node=self.head

		while True:
			last_node=cur_node
			cur_node=cur_node.next
			if cur_index==index:
				last_node.next = cur_node.next
				return
			cur_index+=1



my_list = linked_list()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.display()

my_list.prepend(5)
my_list.insert_between(4,2)


# print(my_list.get(2))
# my_list.erase(1)
my_list.display()

