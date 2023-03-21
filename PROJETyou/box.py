"""
Nom : Bouanane
Prénom : Yousseff
Matricule : 000575893
"""
from pos2d import Pos2D


class Box:
	"""Afin de pouvoir généraliser la notion de point/position, écrivez une classe
	Box représentant un rectangle défini par deux points"""

	def __init__(self, tl: Pos2D, br: Pos2D):
		self.tl = tl
		self.br = br
