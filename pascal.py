# coding: utf8

""" Exercice 4: Triangle de Pascal
Ecrire, à l'aide d'une boucle while, un programme qui demande à l'utilisateur de saisir des nombres (avec arrêt en saisissant "s"), les stocke dans une liste "stock"
et affiche ensuite la liste "result" obtenue en commençant par le premier terme de "stock" puis par les nombres obtenus en sommant deux termes consécutifs de "stock".
Par exemple, la liste [1,1,2,3,5] donnera l'affichage [1,2,3,5,8]
Modifier (ou utiliser) ce programme avec une boucle while pour qu'il parte de la liste [1,0,0,0,0,0,0] et affiche les 6 listes suivantes obtenues par le même principe qu'en 1.
"""

Boucle = True # Boule infini d'input
stock = [0] # Stock les informations
result = [] # Stock le resultat
a = 0
b = 0
c = 0 # Résultat des 2 nombres
i = 0 # 1er nombre
j = 1 # 2nd nombre
k = 0 # compteur de nombre
l = 0 # compteur pour eviter les problemes si stock[j] n'existe pas

while Boucle:
	var = input("Entre un nombre : ")
	if var == "s":
		Boucle = False
	else:
		var = int(var)
		stock.append(var)
		k = k + 1

x = len(stock)
print("Stock : ",stock)

while l < k:
	while j < x: # Evite les problemes si stock[j] n'existe pas
		a = stock[i]
		b = stock[j]
		c = a + b
		break
	#print("A : ", a, "B : ", b, "C", c)
	result.append(c)
	l = l + 1
	i = i + 1
	j = j + 1

result.sort
print("Resultat : ", result)