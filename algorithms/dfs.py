import random
from util.canvas import Canvas
from util.cell import *
from util.position import *

def generate(canvas: Canvas, size_x: int, size_y: int):
    # create cells grid
    cells: list[list[Cell]] = []

    for x in range(size_x):
        cells.append([])
        for y in range(size_y):
            cells[x].append(Cell(Pos(x, y)))

    # pick random starting cell
    start_cell: Cell = random_path(cells)
    start_cell.visited = True

    # iterative implementation
    stack = [start_cell]

    while len(stack) != 0:
        cell = stack.pop()
        unvisited_neighbors = cell.get_unvisited_neighbors(cells)
        if len(unvisited_neighbors) != 0:
            neighbor: Cell = random.choice(unvisited_neighbors)
            neighbor.visited = True

            wall_pos = get_middle(cell.pos, neighbor.pos)
            canvas.path(wall_pos.x, wall_pos.y)

            stack.append(cell)
            stack.append(neighbor)
