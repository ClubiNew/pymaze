from cmath import e
import random
from PIL import Image
from algorithms.prims import get_neighbors
from util.cell import *
from util.grid import *

def generate(img: Image, size_x: int, size_y: int):
    # create cells grid
    cells: list[Cell] = []

    for x in range(size_x):
        cells.append([])
        for y in range(size_y):
            cells[x].append(Cell(Pos(x, y)))
            # paths are at odd co-ordinates
            if x % 2 == 1 and y % 2 == 1:
                img.putpixel((x, y), 1)

    # pick random starting cell
    start_pos = random_path_pos(size_x, size_y)
    start_cell: Cell = cells[start_pos.x][start_pos.y]
    start_cell.visited = True

    # iterative implementation
    stack = [start_cell]

    while len(stack) != 0:
        cell = stack.pop()
        unvisited_neighbors = get_neighbors(cells, cell)[1]
        if len(unvisited_neighbors) != 0:
            neighbor = random.choice(unvisited_neighbors)
            neighbor.visited = True

            wall_pos = get_middle(cell.pos, neighbor.pos)
            img.putpixel((wall_pos.x, wall_pos.y), 1)

            stack.append(cell)
            stack.append(neighbor)
