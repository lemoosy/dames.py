from itertools import permutations
from os import system


def sum_diagonals(matrix, x, y):

	initial_position = (x, y)
	i = matrix[y][x]

	for x_coef in [-1, 1]:
		for y_coef in [-1, 1]:
			while 0 <= x + x_coef < len(matrix[0]) and 0 <= y + y_coef < len(matrix):
				x += x_coef
				y += y_coef
				i += matrix[y][x]
			x, y = initial_position

	return i


def main():

	# permet d'obtenir toute les permutations possible avec une liste de 0 à 7
	for positions_y in permutations(range(8)):

		# création d'une matrice 8x8 vide
		matrix = [[0 for k in range(8)] for i in range(8)]
	
		for x in range(8):
			# s'il n'y a aucune dame sur les diagonales de la position, on place la dame
			if sum_diagonals(matrix, x, positions_y[x]) == 0:
				matrix[positions_y[x]][x] = 1
				# si toutes les dames sont placées, on affiche la combinaison
				if x == 7:
					for line in matrix:
						print(line)
					print()
			else:
				break


main()
input()
