import random
from util.cell import *
from util.position import *
from util.canvas import Canvas

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

    # simplified prim's
    neighbors: list[Cell] = start_cell.get_neighbors(cells)

    while len(neighbors) != 0:
        cell = random.choice(neighbors)
        neighbors.remove(cell)

        if not cell.visited:
            cell.visited = True

            neighbors += cell.get_unvisited_neighbors(cells)

            visited_neighbors = cell.get_visited_neighbors(cells)
            selected_neighbor: Cell = random.choice(visited_neighbors)

            wall_pos = get_middle(cell.pos, selected_neighbor.pos)
            canvas.path(wall_pos.x, wall_pos.y)
