"""
Nom : Bouanane
Prénom : Yousseff
Matricule : X
"""

"""
une classe Node et une classe Grid se chargeant, à deux, de la représentation donnée
ci-dessus. La classe  Node doit contenir 4 booléens demandés, mais le reste vous
est laissée totalement au choix; et la classe Grid doit contenir des méthodes suivantes..
"""
class Node:
	pass



class Grid:
	def __init__(self, width: int, height: int):
		"""return : None
		construit une grille par défaut qui est vide, hormis les murs formant le contour"""
		pass

	def add_wall(self, pos1: Pos2D, pos2: Pos2D):
		"""return : None
		ajoute un mur entre les positions pos1 et pos2 si ces deux cases sont adjacentes"""
		pass

	def remove_wall(self, pos1: Pos2D, pos2: Pos2D):
		"""return : None
		retire un tel mur"""

	def isolate_box(self, box: Box):
		"""return : None
		ajoute les murs afin de former le rectangle box"""

	def accessible_neighbours(self, pos: Pos2D):
		"""return : list[Pos2D]
		renvoie une liste contenant toutes les cases accessibles depuis pos"""


