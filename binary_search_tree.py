class Node:
	def __init__(self,data=None):
		self.data = data
		self.left=None
		self.right=None

class BST:
	def __init__(self):
		self.root = None

	def insert(self,data):
		if self.root is None:
			self.root = Node(data)

		else:
			self._insert(data,self.root)

	def _insert(self,data,cur_node):
		if data<cur_node.data:
			if cur_node.left is None:
				cur_node.left = Node(data)
			else:
				self._insert(data,cur_node.left)
		elif data>cur_node.data:
			if cur_node.right is None:
				cur_node.right = Node(data)
			else: 
				self._insert(data,cur_node.right)
		else:
			print("already exists")
	def find(self,data):
		if self.root:
			is_found = self._find(data,self.root)
			return is_found
		else:
			return None

	def _find(self,data,cur_node):
		if data> cur_node.data and cur_node.right:
			return self._find(data,cur_node.right)
		elif data<cur_node.data and cur_node.left:
			return self._find(data,cur_node.left)
		if data==cur_node.data:
			return True
		return False

	def inorder(self,start):
		# left - root - right

		if start:

			self.inorder(start.left)
			print(start.data)
			self.inorder(start.right)



	def is_bst(self):
		if self.root:
			is_satisfied = self._is_bst(self.root,self.root.data)

			if is_satisfied is None:
				return True
			return False
		return True

	def _is_bst(self,cur_node,data):
		if cur_node.left:
			if data>cur_node.left.data:
				return self._is_bst(cur_node.left,cur_node.left.data)
			else:
				return False

		if cur_node.right:
			if data<cur_node.right.data:
				return self._is_bst(cur_node.right,cur_node.right.data)
			else:
				return False

bst=BST()
bst.insert(4)
bst.insert(8)
bst.insert(5)
bst.insert(10)

tree=BST()
tree.root=Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

# print(bst.find(2))

print(tree.inorder(tree.root,[]))
# print(tree.is_bst())
# print(bst.is_bst())

