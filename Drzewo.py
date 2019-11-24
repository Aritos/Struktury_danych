#!/usr/bin/env python3

#inplementacja drzewa
#TODO: 

class Node():
	def __init__(self,data=None,left=None,right=None):
		self.data = data
		self.left = left
		self.right = right

	def __repr__(self):
		return str(self.data)

	def setData(self,data):
		self.data = data

	def addLeftChild(self,child):
		self.left = child

	def addRightChild(self,child):
		self.right = child

class Tree():
	def __init__(self,root=None):
		self.root = root

	def preorder(self,tree):
		order = []
		order.append(tree.data)
		if tree.left != None:
			order.extend(self.preorder(tree.left))
		if tree.right != None:
			order.extend(self.preorder(tree.right))
		return order

	def inorder(self,tree):
		order = []
		if tree.left != None:
			order.extend(self.inorder(tree.left))
		order.append(tree.data)
		if tree.right != None:
			order.extend(self.inorder(tree.right))
		return order	

	def postorder(self,tree):
		order = []
		if tree.left != None:
			order.extend(self.postorder(tree.left))
		if tree.right != None:
			order.extend(self.postorder(tree.right))
		order.append(tree.data)
		return order

	def depth_of_tree(self,tree):
		if tree == None:
			return 0

		left = self.depth_of_tree(tree.left)
		right = self.depth_of_tree(tree.right)
		if left > right:
			return 1 + left
		else:
			return 1 + right

def main():
	tree = Node(1)
	tree.left = Node(2)
	tree.right = Node(3)
	tree.left.left = Node(4)
	tree.left.right = Node(5)
	tree.left.right.left = Node(6)
	tree.right.left = Node(7)
	tree.right.left.left = Node(8)
	tree.right.left.left.right = Node(9)

	T = Tree()
	print(T.inorder(tree))
	print(T.depth_of_tree(tree))


if __name__ == "__main__":
    main()
