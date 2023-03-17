"""
Nom : Bouanane
Prénom : Yousseff
Matricule : X
"""


class Pos2D:
	def __init__(self, x: int, y: int):
		"""return : None
		doit construire un point représentant la position (x,y)."""
		self.x = x
		self.y = y

	def __eq__(self, other: Pos2D):
		"""return : bool
		permet de tester l'égalité entre deux instances via une expression 
		sous la forme point1 == point2 """

