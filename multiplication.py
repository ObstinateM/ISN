#1 2 3 4 5
#2 4 6 8 10
#3 6 9 12 15
#4 8 12 16 20
#5 10 15 20 25
#Écrivez un programme qui affiche une table de multiplication allant jusqu'à 20 fois 20

#i = 0 # Compteur de tour
#j = 0 # Compteur de tour
#m = 0 # table de multiplication
#
#
#while i < 21:
#	i += 1
#	m += 1
#	while j < 6:
#		print(m * 1, m * 2, m * 3, m * 4, m * 5, m * 6, m * 7, m * 8, m * 9, m * 10, m * 11, m * 12, m * 13, m * 14, m * 15, m * 16, m * 17, m * 18, m * 19, m * 20)
#		break

i = 1
for loop in range(20):
	j = 1
	for loop in range(20):
		print(i * j, end = " ")
		j += 1
	print()
	i += 1