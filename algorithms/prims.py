import random
from PIL import Image
from util.cell import *
from util.grid import *

def get_neighbors(cells: list[Cell], cell: Cell) -> tuple[list[Cell], list[Cell]]:
        neighbor_positions = cell.get_neighbors(len(cells), len(cells[0]))
        visited, unvisited = [], []

        for pos in neighbor_positions:
            neighbor = cells[pos.x][pos.y]
            if neighbor.visited:
                visited.append(neighbor)
            else:
                unvisited.append(neighbor)

        return (visited, unvisited)

def generate(img: Image, size_x: int, size_y: int):
    # create cells grid
    cells: list[Cell] = []

    for x in range(size_x):
        cells.append([])
        for y in range(size_y):
            cell_type = CellType.PATH if x % 2 == 1 and y % 2 == 1 else CellType.WALL
            cells[x].append(Cell(Pos(x, y), cell_type))

    # bootstrap algorithm
    start_pos = random_path_pos(size_x, size_y)
    start_cell: Cell = cells[start_pos.x][start_pos.y]
    start_cell.visited = True

    neighbors: list[Cell] = get_neighbors(cells, start_cell)[1]

    # main algorithm
    while len(neighbors) > 0:
        cell = random.choice(neighbors)
        neighbors.remove(cell)

        if not cell.visited:
            cell.visited = True

            cell_neighbors = get_neighbors(cells, cell)
            neighbors += cell_neighbors[1]

            vis_neighbor: Cell = random.choice(cell_neighbors[0])
            wall_pos = get_middle(cell.pos, vis_neighbor.pos)
            cells[wall_pos.x][wall_pos.y].type = CellType.PATH

    # draw path
    for x, row in enumerate(cells):
        for y, cell in enumerate(row):
            img.putpixel((x, y), cell.type.value)
