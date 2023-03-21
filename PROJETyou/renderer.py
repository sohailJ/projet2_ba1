"""
Nom : Bouanane
Prénom : Yousseff
Matricule : 000575893
"""
from grid import Grid
from grid import Node


class GridRenderer:
	"""Used for dungeon rendering"""
	def __init__(self, grid: Grid):
		"""return : None
		build the render of the grid"""
		def add_node_render(representation: dict, pos: (int, int), node: Node):
			node_list_representation = node.get_bool_list_representation()
			tl_x = pos[0] * 3
			tl_y = pos[1] * 3
			representation[(tl_x, tl_y)] = ' '
			representation[(tl_x + 2, tl_y)] = ' '
			representation[(tl_x, tl_y + 2)] = ' '
			representation[(tl_x + 2, tl_y + 2)] = ' '

			# 4 way wall
			if node_list_representation == [False, False, False, False]:
				representation[(tl_x + 1, tl_y + 1)] = '┼'
				representation[(tl_x, tl_y + 1)] = representation[(tl_x + 2, tl_y + 1)] = '─'
				representation[tl_x + 1, tl_y] = representation[(tl_x + 1, tl_y + 2)] = '│'

			# 3 way walls
			elif node_list_representation == [False, False, False, True]:
				representation[(tl_x + 2, tl_y + 1)] = ' '
				representation[(tl_x + 1, tl_y + 1)] = '┤'
				representation[(tl_x, tl_y + 1)] = '─'
				representation[(tl_x + 1, tl_y)] = representation[(tl_x + 1, tl_y + 2)] = '│'

			elif node_list_representation == [False, False, True, False]:
				representation[(tl_x + 1, tl_y + 2)] = ' '
				representation[(tl_x + 1, tl_y + 1)] = '┴'
				representation[(tl_x, tl_y + 1)] = representation[(tl_x + 2, tl_y + 1)] = '─'
				representation[(tl_x + 1, tl_y)] = '│'

			elif node_list_representation == [False, True, False, False]:
				representation[(tl_x, tl_y + 1)] = ' '
				representation[(tl_x + 1, tl_y + 1)] = '├'
				representation[(tl_x + 2, tl_y + 1)] = '─'
				representation[(tl_x + 1, tl_y)] = representation[(tl_x + 1, tl_y + 2)] = '│'

			elif node_list_representation == [True, False, False, False]:
				representation[(tl_x + 1, tl_y)] = ' '
				representation[(tl_x + 1, tl_y + 1)] = '┬'
				representation[(tl_x + 2, tl_y + 1)] = representation[(tl_x, tl_y + 1)] = '─'
				representation[(tl_x + 1, tl_y + 2)] = '│'

			# 2 ways walls
			elif node_list_representation == [False, False, True, True]:
				representation[(tl_x + 1, tl_y + 2)] = representation[(tl_x + 2, tl_y + 1)] = ' '
				representation[(tl_x + 1, tl_y + 1)] = '┘'
				representation[(tl_x, tl_y + 1)] = '─'
				representation[(tl_x + 1, tl_y)] = '│'

			elif node_list_representation == [False, True, True, False]:
				representation[(tl_x + 1, tl_y + 2)] = representation[(tl_x, tl_y + 1)] = ' '
				representation[(tl_x + 1, tl_y + 1)] = '└'
				representation[(tl_x + 2, tl_y + 1)] = '─'
				representation[(tl_x + 1, tl_y)] = '│'

			elif node_list_representation == [True, False, False, True]:
				representation[(tl_x + 1, tl_y + 2)] = representation[(tl_x + 2, tl_y + 1)] = ' '
				representation[(tl_x + 1, tl_y + 1)] = '┐'
				representation[(tl_x, tl_y + 1)] = '─'
				representation[(tl_x + 1, tl_y + 2)] = '│'

			elif node_list_representation == [True, True, False, False]:
				representation[(tl_x + 1, tl_y)] = representation[(tl_x, tl_y + 1)] = ' '
				representation[(tl_x + 1, tl_y + 1)] = '┌'
				representation[(tl_x + 2, tl_y + 1)] = '─'
				representation[(tl_x + 1, tl_y + 2)] = '│'
			# 1 way walls
			elif node_list_representation == [True, False, True, False]:
				representation[(tl_x + 1, tl_y + 1)] = '│'
				representation[(tl_x, tl_y + 1)] = representation[(tl_x + 2, tl_y + 1)] = ' '
				representation[(tl_x + 1, tl_y)] = representation[(tl_x + 1, tl_y + 2)] = '│'

			elif node_list_representation == [False, True, False, True]:
				representation[(tl_x + 1, tl_y + 1)] = '─'
				representation[(tl_x, tl_y + 1)] = representation[(tl_x + 2, tl_y + 1)] = '─'
				representation[tl_x + 1, tl_y] = representation[(tl_x + 1, tl_y + 2)] = ' '
				return '─'
			# no walls
			elif node_list_representation == [True, True, True, True]:
				representation[(tl_x + 1, tl_y + 1)] = '─'
				representation[(tl_x, tl_y + 1)] = representation[(tl_x + 2, tl_y + 1)] = '─'
				representation[tl_x + 1, tl_y] = representation[(tl_x + 1, tl_y + 2)] = ' '
			else:
				raise 'not supposed to happen'

		self.width = grid.width * 3
		self.height = grid.height * 3
		# self.pos_symbol = {position: get_symbol_representing_node(node) for position, node in grid.nodes.items()}
		self.pos_symbol = {}
		for position, node in grid.nodes.items():
			add_node_render(self.pos_symbol, position, node)

	def show(self):
		"""
		displays dungeon
		@return: None
		"""
		for i in range(self.width+1):
			row = ''
			for j in range(self.height+1):
				row += self.pos_symbol[(i, j)]
			print(row)
