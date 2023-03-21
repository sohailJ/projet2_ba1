"""
Nom : Bouanane
Prénom : Yousseff
Matricule : 000575893
"""
from box import Box
from pos2d import Pos2D


class Node:
    def __init__(self, up: bool, left: bool, down: bool, right: bool):
        """
        Node constructor
        @param up:
        @param left:
        @param down:
        @param right:
        """
        self.up = up
        self.left = left
        self.down = down
        self.right = right

    def get_bool_list_representation(self):
        """
        @return: [self.up, ..., self.right]
        """
        return [self.up, self.left, self.down, self.right]


class Grid:
    def __init__(self, width: int, height: int):
        """
        Build a grid with walls on the edges. Remarks:
        1) the grid is larger than the box (+1) since top left corner of
        the box is in the center of the tof left tile of the grid. Same reasoning applies to the other 3 corners.
        2) the top left corner is (0,0) and down right corner (width, height)
        @param width: width of the box
        @param height: height of the box
        """
        self.width = width
        self.height = height

        self.nodes = {(i, j): Node(False, False, False, False) for i in range(width + 1) for j in range(height + 1)}

        # set corners
        self.nodes[(0, 0)] = Node(False, False, True, True)
        self.nodes[(width, 0)] = Node(False, True, True, False)
        self.nodes[(width, height)] = Node(True, True, False, False)
        self.nodes[(0, height)] = Node(True, False, False, True)

        # set top and bottom walls: left and right bools at true
        for i in range(0, width):
            setattr(self.nodes[(i, 0)], 'right', True)
            setattr(self.nodes[(i + 1, 0)], 'left', True)
            setattr(self.nodes[(i, height)], 'right', True)
            setattr(self.nodes[(i + 1, height)], 'left', True)

        # set left and right walls (excluding corners): top and down bools at true
        # for j in range(1, height):
          #  setattr(self.nodes[(0, j)], 'down', True)
           # setattr(self.nodes[(0, j + 1)], 'up', True)
            #setattr(self.nodes[(width, j)], 'down', True)
            #setattr(self.nodes[(width, j + 1)], 'up', True)

    def add_wall(self, pos1: Pos2D, pos2: Pos2D) -> None:
        """
        Add wall between pos1 and pos2 if they are adjacent
        @param pos1: instance of Pos2D representing a position
        @param pos2: instance of Pos2D representing a position
        @return: None
        """
        if not pos1 or not pos2 or pos1 == pos2:
            return None

        x1, y1 = pos1.x, pos1.y
        x2, y2 = pos2.x, pos2.y
        if x1 == x2:
            if y1 + 1 == y2:
                setattr(self.nodes[(x1, y1)], 'right', True)
                setattr(self.nodes[(x2, y2)], 'left', True)
            elif y1 - 1 == y2:
                setattr(self.nodes[(x1, y1)], 'left', True)
                setattr(self.nodes[(x1, x2)], 'right', True)

        elif y1 == y2:
            if x1 + 1 == x2:
                setattr(self.nodes[(x1, y1)], 'down', True)
                setattr(self.nodes[(x2, y2)], 'up', True)
            elif x1 - 1 == x2:
                setattr(self.nodes[(x1, y1)], 'up', True)
                setattr(self.nodes[(x1, y1)], 'down', True)


    def remove_wall(self, pos1: Pos2D, pos2: Pos2D) -> None:
        """
        Removes wall between pos1 and pos2 if they are adjacent
        @param pos1: instance of Pos2D representing a position
        @param pos2: instance of Pos2D representing a position
        @return: None
        """
        if not pos1 or not pos2 or pos1 == pos2:
            return None

        if pos1.x == pos2.x:
            if pos1.y < pos2.y:
                setattr(self.nodes[(pos1.x, pos1.y)], 'right', False)
                setattr(self.nodes[(pos2.x, pos2.y)], 'left', False)
            else:
                setattr(self.nodes[(pos1.x, pos1.y)], 'left', False)
                setattr(self.nodes[(pos2.x, pos2.y)], 'right', False)

        if pos1.y == pos2.y:
            if pos1.x < pos2.x:
                setattr(self.nodes[(pos1.x, pos1.y)], 'down', False)
                setattr(self.nodes[(pos2.x, pos2.y)], 'up', False)
            else:
                setattr(self.nodes[(pos1.x, pos1.y)], 'up', False)
                setattr(self.nodes[(pos2.x, pos2.y)], 'down', False)

    def isolate_box(self, box: Box) -> None:
        """
        create a walls corresponding to the box
        @param box: instance of class Box representing a rectangle
        @return: None
        """
        # considering a box like:
        # (x0, y0) -----------------------
        #         |                       |
        #         |                       |
        #         |                       |
        #          ----------------------- (x1, y1)
        x0 = box.tl.x
        y0 = box.tl.y
        x1 = box.br.x
        y1 = box.br.y
        print(x0, y0, x1, y1)
        # set horizontal walls
        for i in range(x0, x1):
            print(f'add_wall(Pos2D({i}, {y0}), Pos2D({i + 1}, {y0}))')
            self.add_wall(Pos2D(i, y0), Pos2D(i + 1, y0))
            print(f'add_wall(Pos2D({i}, {y1}), Pos2D({i + 1}, {y1}))')
            self.add_wall(Pos2D(i, y1), Pos2D(i + 1, y1))

        # set vertical walls
        for j in range(y0, y1):
            print(j)
            self.add_wall(Pos2D(x0, j), Pos2D(x0, j + 1))
            self.add_wall(Pos2D(x1, j), Pos2D(x1, j + 1))

    def accessible_neighbours(self, pos: Pos2D) -> [Pos2D]:
        """
        @param pos: instance of Pos2D representing a position
        @return: list of neighbors of pos
        """
        node = self.nodes.get((pos.x, pos.y))
        positions = [(pos.x, pos.y + 1), (pos.x - 1, pos.y), (pos.x, pos.y - 1), (pos.x + 1, pos.y)]
        accessibility = node and [node.up, node.left, node.down, node.right]
        return [position for position, is_accessible in zip(positions, accessibility) if is_accessible]
