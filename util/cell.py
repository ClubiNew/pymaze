import random
from enum import Enum
from typing_extensions import Self
from util.position import Pos

class CellType(Enum):
    WALL = 0
    PATH = 1

class Cell:
    def __init__(self, pos: Pos, type: CellType = None):
        self.pos = pos
        self.type = type
        self.visited = False

    def get_neighbors(self, cells: list[Self]) -> list[Self]:
        adjacent_positions = self.pos.get_adjacent(len(cells), len(cells[0]))

        neighbors = []
        for pos in adjacent_positions:
            neighbors.append(cells[pos.x][pos.y])

        return neighbors

    def get_visited_neighbors(self, cells: list[Self]) -> list[Self]:
        neighbors = self.get_neighbors(cells)
        return list(filter(lambda cell : cell.visited, neighbors))

    def get_unvisited_neighbors(self, cells: list[Self]) -> list[Self]:
        neighbors = self.get_neighbors(cells)
        return list(filter(lambda cell : not cell.visited, neighbors))

def random_path(cells: list[list[Cell]]) -> Cell:
    # paths are only on odd positions
    x = random.randint(0, len(cells) // 2 - 1) * 2 + 1
    y = random.randint(0, len(cells[0]) // 2 - 1) * 2 + 1
    return cells[x][y]
