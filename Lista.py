#!/usr/bin/env python3

#Implementacja Listy.
#TODO: remove,reverse,sort,insert,index,extend,count,copy

class Lista_elem():
	def __init__(self,new,prev=None):
		self.new = new
		self.prev = prev

class Lista():
	def __init__(self):
		self.first = None
		self.ostatni = None

	def __repr__(self):
		if self.first == None:
			return '[]'
		return '[' + str(self.first.new) + str(self.ost(self.first.prev))

	def __len__(self):
		return self.rek_len(self.first)

	def ost(self,ostat):
		if ostat == None:
			return ']'
		else:
			return ', ' + str(ostat.new) + str(self.ost(ostat.prev))

	def rek_len(self,ostat):
		if ostat == None:
			return 0
		else:
			return 1 + self.rek_len(ostat.prev)

	def append(self,elem):
		if self.first == None:
			d = Lista_elem(elem,self.ostatni)
			self.first = d
			self.ostatni = d
		else:
			d = Lista_elem(elem,None)
			self.ostatni.prev = d
			self.ostatni = d
	def clear(self):
		self.first = None

	def pop(self):
		self.first = self.first.prev

#	def remove(self,elem):
#		d = self.first
#		if d.new == elem: 

'''
L = Lista()
print(L)
L.append(1)
L.append(1)
L.append(2)
L.append(3)
L.append(4)
l = [1,2,3]
print(len(L))
'''
