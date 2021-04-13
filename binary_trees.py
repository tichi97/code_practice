class Queue(object):
	def __init__(self):
		self.items=[]

	def enqueue(self,item):
		self.items.insert(0,item)

	def dequeue(self):
		if not self.is_empty():
			return self.items.pop()

	def is_empty(self):
		return len(self.items)==0

	def peek(self):
		if not self.is_empty():
			return self.items[-1].value

	def __len__(self):
		return self.size()

	def size(self):
		return len(self.items)
class Stack(object):
	def __init__(self):
		self.items=[]

	def push(self,item):
		self.items.append(item)

	def pop(self):
		if not self.is_empty():
			return self.items.pop()

	def is_empty(self):
		return len(self.items)==0

	def peek(self):
		if not self.is_empty():
			return self.items[-1].value

	def __len__(self):
		return self.size()

	def size(self):
		return len(self.items)

class Node(object):
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None

class BinaryTree(object):
	def __init__(self, root):
		self.root = Node(root)

	def print_tree(self,traversal_type):
		if traversal_type == "preorder":
			return self.preorder_print(self.root, "")
		else:
			print("error")
#depth first search 
	def preorder_print(self,start,traversal):
		# Root - left - right

		if start:
			traversal+=(str(start.value)+ "-")
			traversal = self.preorder_print(start.left,traversal)
			traversal = self.preorder_print(start.right, traversal)

		return traversal

	#depth first search 
	def inorder(self,start):
		# left - root - right

		if start:
			self.inorder(start.left)
			print(start.value)
			self.inorder(start.right)
#depth first search 
	def postorder(self,start):
		# left - right - root
		if start:
			self.postorder(start.left)
			self.postorder(start.right)
			print(start.value)

	def size(self):
		if self.root is None:
			return 0

		stack = Stack()
		stack.push(self.root)
		size=1

		while stack:
			node = stack.pop()
			if node.left:
				size+=1
				stack.push(node.left)
			if node.right:
				size+=1
				stack.push(node.right)

		return size

	def size_rec(self,node):
		if node is None:
			return 0
		return 1+self.size_rec(node.left)+self.size_rec(node.right)

	def height(self, node):
		if node is None:
			return -1

		left_height= self.height(node.left)
		right_height= self.height(node.right)

		return 1 +max(left_height,right_height)

	#breadth first search
	def bfs(self,start):
		if start is None:
			return

		queue = Queue()
		queue.enqueue(start)

		while len(queue)>0:
			print(queue.peek())
			node = queue.dequeue()

			if node.left:
				queue.enqueue(node.left)
			if node.right:
				queue.enqueue(node.right)

	def reverse_level_order(self,start):
		if start is None:
			return

		q=Queue()
		stack=Stack()
		q.enqueue(start)

		while len(q)>0:
			node = q.dequeue()
			stack.push(node)

			if node.right:
				q.enqueue(node.right)
			if node.left:
				q.enqueue(node.left)

		while len(stack)>0:
			print(stack.pop().value)

	def maxPathSum(self,root):
		self.maximum = float('-inf')


		def dfs(root):
			if root is None:
				return 0

			left_max=max(0,dfs(root.left))
			right_max=max(0,dfs(root.right))
			self.maximum=max(self.maximum,(left_max+right_max+root.value))

			return max(left_max,right_max) + root.value

		dfs(root)
		return self.maximum

	# def sumRoottoLeaf(self,node,total):
	# 	if not node:
 #            return 0
            
 #        if node:
 #            total=total*10 +node.value
 #            if not node.left and not node.right:
 #                return total
 #            else:
 #                return dfs(node.left,total)+dfs(node.right,total)







#	1
#  /
#  2
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)


# print(tree.print_tree("preorder"))
tree.inorder(tree.root.left)
tree2=BinaryTree(tree.root.left)
tree2.inorder(tree2.root)
# tree.postorder(tree.root)

# print(tree.height(tree.root))
# tree.bfs(tree.root)
# tree.reverse_level_order(tree.root)
# print(tree.size_rec(tree.root))