from random import randint
from random import shuffle
Joueur = ["Joueur1", "Joueur2", "Joueur3", "Joueur4", "Joueur5"]
Nombre = [0, 1, 2, 3, 4, 5, 6]
pointer = []
nb = 0
shuffle(Nombre)

class SetRole:
	"""docstring for SetRole"""
	def __init__(self, k, v):
		ListeRole = ["Test1", "Test2", "Test3", "Test4", "Test5", "Test6", "Test7"]
		print(Nombre)
		nb = Nombre[-1]
		Nombre.pop(-1)
		print(Nombre)
		#print("NB DU RANDINT: ", nb)
		self.id = k
		self.name = v
		self.role = ListeRole[nb]

for k,v in enumerate(Joueur):
	test = SetRole(k, v)
	pointer.append(test)
	print(pointer[k].id, pointer[k].name, pointer[k].role)

