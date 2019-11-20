#!/usr/bin/env python3

#Implementacja stosu

#Klasa Stosu na liscie
class Stos(object):
	def __init__(self):
		self.lista = []
	def push(self,elem):
		self.lista.append(elem)
	def pop(self):
		self.lista.pop()
	def Top(self):
		return self.lista[-1]
	def Size(self):
		return len(self.lista)
	def isEmpty(self):
		if len(self.lista) == 0: return True
		else: return False

#Klasa elementu stosu
class Stos_elem():
	def __init__(self,new = 0,prev = None):
		self.new = new
		self.prev = prev

#Klasa stosu zrobiona na wskaźnikach
class Stos_wskaz():
	def __init__(self):
		self.gora = None

	def Push(self,elem):
		d = Stos_elem(elem, self.gora)
		self.gora = d

	def Top(self):
		if self.gora != None:
			return self.gora.new
		return None
	def Pop(self):
		if self.gora != None:
			self.gora = self.gora.prev

	def isEmpty(self):
		if self.gora == None: 
			return True
		return False

'''
E = Stos()
E.push(1)
E.push(2)
E.pop()
E.push(55)
print(E.Top())
print(E.isEmpty())
print(E.Size())

# Stos na wskaznikach
S = Stos_wskaz()
S.Push(1)
S.Push(2)
S.Push(3)
S.Push(4)
S.Pop()
print(S.Top())
print(S.isEmpty())
'''