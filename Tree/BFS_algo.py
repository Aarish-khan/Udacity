#create a queue to use in BFS algorithm

class Queue:
	def __init__(self):
		self.items = list()

	def size(self):
		return len(self.items)

	def is_empty(self):
		return len(self.items) == 0


	def front(self):
		return self.items[0]

	def enq(self,item):
		self.items.append(item)

	def deq(self):
		if len(self.items)>0:
			return self.items.pop(0)
		else:
			return None

	def __repr__(self):
		if self.is_empty():
			return "queue is empty"
		else:
			s = "<Enqueue here>\n---------------\n"
			s += "\n---------------\n".join(item.value for item in self.items)
			s += "\n---------------\n<dequeue here>\n\n"

			return s



# q =Queue()

# print(f"initial size of q is: {q.size()}")
# print(q)

# print("inserting a element \'apple\'")
# q.enq("apple")
# print(f"size of q after inserting apple: {q.size()}")
# print(q)


#defining tree for doing bfs
#tree is consisting of nodes therefor defining nodes class first
class Node:
	def __init__(self,value = None):
		self.value = value
		self.left = None
		self.right = None

	#define get and set functions for node class
	def get_value(self):
		return self.value

	def set_value(self,value):
		self.value = value


	def get_left_node(self):
		return self.left

	def get_right_node(self):
		return self.right

	def set_left_node(self,node):
		self.left = node

	def set_right_node(self,node):
		self.right = node

	def has_left_child(self):
		return self.left != None

	def has_right_child(self):
		return self.right != None

	def __repr__(self):
		s = f"Node: {self.value}"
		return s




# node0 = Node("apple")
# node1 = Node("banana")

# node0.set_left_node(node1)

# print(node0.get_left_node().value)
# print(node1.has_left_child())

class Tree:
	def __init__(self,value = None):
		self.root = Node(value)

	def get_root(self):
		return self.root


#creating a tree  for traversing purpose
tree = Tree("apple")
tree.get_root().set_left_node(Node("banana"))
tree.get_root().set_right_node(Node("cherry"))
tree.get_root().get_left_node().set_left_node(Node("dates"))


#bfs implementaion algorithm

def bfs(tree):
	#create a visit array
	visit_order = list()
	#create a queue
	q =Queue()

	#take the root node from tree
	node = tree.get_root()
	#insert/enqueue it into our q
	q.enq(node)

	count = 3
	while count:
		#deque element from queue
		node = q.deq()
		#mark it into visit_order
		visit_order.append(node)

		#if this node has left child enqueue them into q
		if node.has_left_child():
			q.enq(node.get_left_node())
		#if this node has right child enqueu them into q
		if node.has_right_child():
			q.enq(node.get_right_node())

		print(f"visit order: {visit_order}")
		print(q)
		count -=1


	return visit_order

bfs(tree)

