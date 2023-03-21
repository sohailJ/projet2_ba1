"""
Nom : Bouanane
Prénom : Yousseff
Matricule : 000575893
"""


import grid
import box
import pos2d
import renderer

if __name__ == "__main__":
    out_box = box.Box(pos2d.Pos2D(0, 0), pos2d.Pos2D(2, 1))
    in_box = box.Box(pos2d.Pos2D(1, 1), pos2d.Pos2D(2, 2))

    base_grid = grid.Grid(2, 2)
    # base_grid.accessible_neighbours(pos2d.Pos2D(0 , 0))

    # base_grid.isolate_box(out_box)
    rendered = renderer.GridRenderer(base_grid)
    rendered.show()

    # base_grid.isolate_box(in_box)
    # rendered = renderer.GridRenderer(base_grid)
    # rendered.show()
