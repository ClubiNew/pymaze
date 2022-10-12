import random
from util.canvas import Canvas
from util.cell import *
from util.position import *

def generate(canvas: Canvas, size_x: int, size_y: int):
    # create cells grid
    cells: list[Cell] = []

    for x in range(size_x):
        cells.append([])
        for y in range(size_y):
            # paths are at odd co-ordinates
            if x % 2 == 1 and y % 2 == 1:
                cells[x].append(Cell(Pos(x, y), CellType.PATH))
            else:
                cells[x].append(Cell(Pos(x, y), CellType.WALL))

    unvisited_paths: list[Cell] = []
    for row in cells:
        for cell in row:
            if cell.type == CellType.PATH:
                unvisited_paths.append(cell)

    # pick random starting cell
    start_cell: Cell = random_path(cells)
    unvisited_paths.remove(start_cell)
    start_cell.visited = True

    # begin walking
    while len(unvisited_paths) != 0:
        current_cell: Cell = random.choice(unvisited_paths)
        walk = []

        while not current_cell.visited:
            neighbors = current_cell.get_neighbors(cells)
            walk.append(current_cell)
            current_cell: Cell = random.choice(neighbors)

            # remove loops
            if current_cell in walk:
                loop_start = walk.index(current_cell)
                walk = walk[:loop_start]

        # walk complete, remove walls & add to maze
        previous_cell: Cell = None
        for cell in walk:
            unvisited_paths.remove(cell)
            cell.visited = True

            if previous_cell != None:
                wall_pos = get_middle(cell.pos, previous_cell.pos)
                canvas.path(wall_pos.x, wall_pos.y)
            previous_cell = cell

        wall_pos = get_middle(current_cell.pos, previous_cell.pos)
        canvas.path(wall_pos.x, wall_pos.y)
