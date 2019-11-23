#!/usr/bin/env python3

#Implementacja Listy.
#TODO: sort, copy

class Lista_elem():
	def __init__(self,elem,next=None):
		self.elem = elem
		self.next = next

class Lista():
	def __init__(self):
		self.first = None

	def __repr__(self):
		if self.first == None:
			return '[]'
		return '[' + str(self.first.elem) + str(self.ost(self.first.next))

	def __len__(self):
		return self.rek_len(self.first)

	def __iter__(self): 
		self.it = self.first
		return self

	def __next__(self):
		it = self.it

		if it == None: 
			raise StopIteration 

		self.it = it.next; 
		return it.elem

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
		d = Lista_elem(elem)
		if self.first == None:
			self.first = d
		else:
			p = self.first
			while p.next != None:
				p = p.next
			p.next = d

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

	def insert(self,poz,elem):
		new = Lista_elem(elem)
		if poz == 0:
			new.next = self.first
			self.first = new
		else:
			d = self.first
			for i in range(poz):
				poprzedni = d
				if poprzedni.next == None:
					poprzedni.next = new
					break
				d = d.next
			if poprzedni.next != new:
				poprzedni.next = new
				new.next = d

	def index(self,elem):
		d = self.first
		i = 0
		while d.elem != elem:
			poprzedni = d
			d = d.next
			i += 1
		return i

	def extend(self,ite):
		for i in ite:
			self.append(i)

	def count(self,elem):
		d = self.first
		i = 0
		while d != None:
			if d.elem == elem:
				i += 1
			d = d.next
		return i


#L = Lista()

