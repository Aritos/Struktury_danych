#!/usr/bin/env python3

#Implementacja Listy.
#TODO: sort,insert,index,extend,count,copy

class Lista_elem():
	def __init__(self,elem,next=None):
		self.elem = elem
		self.next = next

class Lista():
	def __init__(self):
		self.first = None
		self.ostatni = None

	def __repr__(self):
		if self.first == None:
			return '[]'
		return '[' + str(self.first.elem) + str(self.ost(self.first.next))

	def __len__(self):
		return self.rek_len(self.first)

	def ost(self,ostat):
		if ostat == None:
			return ']'
		else:
			return ', ' + str(ostat.elem) + str(self.ost(ostat.next))

	def rek_len(self,ostat):
		if ostat == None:
			return 0
		else:
			return 1 + self.rek_len(ostat.next)

	def append(self,elem):
		if self.first == None:
			d = Lista_elem(elem,self.ostatni)
			self.first = d
			self.ostatni = d
		else:
			d = Lista_elem(elem,None)
			self.ostatni.next = d
			self.ostatni = d

	def clear(self):
		self.first = None

	def pop(self):
		d = self.first
		while d.next != None:
			poprzedni = d
			d = d.next
		poprzedni.next = None
		return d.elem

	def remove(self,elem):
		d = self.first
		while d.elem != elem:
			poprzedni = d
			d = d.next
		poprzedni.next = d.next

	def reverse(self,e = None,d = None):
		if d == None:
			d = self.first
		if d.next == None:
			d.next = e
			self.first = d
		else:
			self.reverse(d,d.next)
			d.next = e





'''
L = Lista()
L.append(1)
L.append(2)
L.append(3)
L.append(4)
L.append(5)
print(L)
L.reverse()
print(L)
'''