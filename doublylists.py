from collections import defaultdict

class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
		self.prev=None


class Doubly:
	def __init__(self):
		self.head = None


	def append(self, data):
		new_node = Node(data)
		if self.head is None:
			# new_node.prev = None
			self.head = new_node
		else:
			cur=self.head
			while cur.next:
				cur=cur.next

			cur.next=new_node
			new_node.prev=cur
			new_node.next=None


	def prepend(self,data):
		new_node=Node(data)
		if self.head is None:
			self.head = new_node
		else:
			self.head.prev = new_node
			new_node.next= self.head
			self.head = new_node
	def add_after(self,data,key):
		new_node=Node(data)
		cur=self.head

		while cur:
			if cur.data==key:
				nxt=cur.next
				cur.next=new_node
				new_node.prev=cur
				new_node.next=nxt
				nxt.prev=new_node
				return
			cur=cur.next

		print('key not found')

	def display(self):
		cur = self.head

		while cur:
			print(cur.data)
			cur=cur.next

	def reverse(self):
		temp = None
		cur=self.head

		while cur:
			temp=cur.prev
			cur.prev=cur.next
			cur.next=temp
			cur=cur.prev
		if temp:
			self.head=temp.prev

	def pairs_with_sum(self,sum_val):
		pairs = []
		p = self.head
		q=None
		while p:
			q=p.next
			while q:
				if p.data+q.data==sum_val:
					pairs.append([p.data,q.data])
				q=q.next
			p=p.next
		return pairs

	def remove_duplicates(self):
		cur = self.head
		duplicates=defaultdict(int)
		# prev=

		while cur:
			if duplicates[cur.data]==0:
				duplicates[cur.data]+=1
				cur=cur.next
			else:
				nxt=cur.next
				self.delete_node(cur)
				cur=nxt

	def delete(self,key):
		cur =self.head

		while cur:
			
			if cur.data==key and cur==self.head:
				#case 1:
				if not cur.next:
					cur=None
					self.head=None
					return
				# case 2:
				else:
					nxt=cur.next
					cur.next=None
					cur=None
					nxt.prev=None
					self.head=nxt
					return

			elif cur.data==key:
				#case 3
				if cur.next:
					nxt=cur.next
					prev=cur.prev
					prev.next=nxt
					nxt.prev=prev
					cur.next=None
					cur.prev=None
					cur=None
					return
				else:
					# case 4
					prev=cur.prev
					prev.next=None
					cur.prev=None
					cur=None
					return

			cur=cur.next

	def delete_node(self,node):
		cur =self.head

		while cur:
			
			if cur==node and cur==self.head:
				#case 1:
				if not cur.next:
					cur=None
					self.head=None
					return
				# case 2:
				else:
					nxt=cur.next
					cur.next=None
					cur=None
					nxt.prev=None
					self.head=nxt
					return

			elif cur==node:
				#case 3
				if cur.next:
					nxt=cur.next
					prev=cur.prev
					prev.next=nxt
					nxt.prev=prev
					cur.next=None
					cur.prev=None
					cur=None
					return
				else:
					# case 4
					prev=cur.prev
					prev.next=None
					cur.prev=None
					cur=None
					return

			cur=cur.next








my_list=Doubly()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)


my_list.prepend(0)
my_list.add_after(5,3)
# my_list.delete(0)
# my_list.display()
# print(my_list.pairs_with_sum(0))
# my_list.remove_duplicates()
my_list.display()
