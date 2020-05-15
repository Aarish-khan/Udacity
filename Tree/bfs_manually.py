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
			s += "\n---------------\n<dequeue here>"
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


#creating a tree object for traversing purpose
tree = Tree("apple")
tree.get_root().set_left_node(Node("banana"))
tree.get_root().set_right_node(Node("cherry"))
tree.get_root().get_left_node().set_left_node(Node("dates"))


#Now the real game of bfs starts
#first we will manuallly traverse tree in bfs manner than afterwards we will implement algorithm
q = Queue()
visit_order = []

#so starting from root node 
node = tree.get_root()
# enqueue this in our queue
q.enq(node)
print(q)


#algorithm iteration 1:
#1.dequeue the next node from queue
# 2.mark it visited 
# 3.add its children in queue

node = q.deq()
visit_order.append(node.value)

if node.has_left_child():
	q.enq(node.get_left_node())
if node.has_right_child():
	q.enq(node.get_right_node())

print(f"visited order: {visit_order}")
print(q)

#algorithm iteration 2:
#1.dequeue the next node from queue
# 2.mark it visited 
# 3.add its children in queue

node = q.deq()
visit_order.append(node.value)
if node.has_left_child():
	q.enq(node.get_left_node())
if node.has_right_child():
	q.enq(node.get_right_node())

print(f"visited order: {visit_order}")
print(q)


#algorithm iteration 3:
#1.dequeue the next node from queue
# 2.mark it visited 
# 3.add its children in queue

node = q.deq()
visit_order.append(node.value)
if node.has_left_child():
	q.enq(node.get_left_node())
if node.has_right_child():
	q.enq(node.get_right_node())

print(f"visited order: {visit_order}")
print(q)


#algorithm iteration 4:
#1.dequeue the next node from queue
# 2.mark it visited 
# 3.add its children in queue

node = q.deq()
visit_order.append(node.value)
if node.has_left_child():
	q.enq(node.get_left_node())
if node.has_right_child():
	q.enq(node.get_right_node())

print(f"visited order: {visit_order}")
print(q)







