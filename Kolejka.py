#!/usr/bin/env python3

#implementcja kolejki

class Kolejka_elem():
	def __init__(self,new,prev=None):
		self.new = new
		self.prev = prev

class Kolejka():
	def __init__(self):
		self.first = None
		self.ostatni = None
	def Dodaj(self,elem):
		if self.first == None:
			d = Kolejka_elem(elem,self.ostatni)
			self.first = d
			self.ostatni = d
		else:
			d = Kolejka_elem(elem,None)
			self.ostatni.prev = d
			self.ostatni = d
	def Zabiez(self):
		self.first = self.first.prev
	def Pokaz(self):
		if self.first == None:
			return None
		else:
			return self.first.new
	def is_Empty(self):
		if self.first == None:
			return True
		else:
			return False

'''
K = Kolejka()
K.Dodaj(1)
K.Dodaj(2)
K.Dodaj(3)
print(K.Pokaz())
K.Zabiez()
print(K.Pokaz())
K.Zabiez()
K.Zabiez()
print(K.Pokaz())
K.Dodaj(3)
print(K.Pokaz())
print(K.is_Empty())
'''



		
