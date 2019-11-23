#!/usr/bin/env python3

#inplementacja drzewa
#TODO: 

class Node():
	def __init__(self,key=None,parent=None,left=None,right=None):
		self.key = key
		self.parent = parent
		self.left = left
		self.right = right

	def __repr__(self):
		return str(self.key)

	def setKey(self,key):
		self.key = key

	def addParent(self,parent):
		self.parent = parent

	def addLeftChild(self,child):
		self.left = child

	def addRightChild(self,child):
		self.right = child

class Tree():
	def __init__(self,root=None):
		self.root = root

	def preorder(self,top):
		order = []
		order.append(top.key)
		if top.left != None:
			order.extend(self.preorder(top.left))
		if top.right != None:
			order.extend(self.preorder(top.right))
		return order

	def inorder(self,top):
		order = []
		if top.left != None:
			order.extend(self.inorder(top.left))
		order.append(top.key)
		if top.right != None:
			order.extend(self.inorder(top.right))
		return order	

	def postorder(self,top):
		order = []
		if top.left != None:
			order.extend(self.postorder(top.left))
		if top.right != None:
			order.extend(self.postorder(top.right))
		order.append(top.key)
		return order

'''
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)
a.addLeftChild(b)
a.addRightChild(c)
b.addLeftChild(d)
b.addRightChild(e)
c.addLeftChild(f)
c.addRightChild(g)

aa = Node(8)
bb = Node(9)
d.addLeftChild(aa)
d.addRightChild(bb)

D = Tree()

print("preorder",D.preorder(a))
print("inorder",D.inorder(a))
print("postorder",D.postorder(a))
'''

