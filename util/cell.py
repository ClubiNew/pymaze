from enum import Enum
from util.grid import Pos

class CellType(Enum):
    WALL = 0
    PATH = 1

class Cell:
    def __init__(self, pos: Pos, type: CellType):
        self.pos = pos
        self.type = type
        self.visited = False

    # return positions of neighboring cells within the grid
    def get_neighbors(self, size_x: int, size_y: int) -> list[Pos]:
        neighbors = []

        for direction in [-2, 2]:
            x_neighbor = Pos(self.pos.x + direction, self.pos.y)
            if x_neighbor.within(size_x, size_y):
                neighbors.append(x_neighbor)

            y_neighbor = Pos(self.pos.x, self.pos.y + direction)
            if y_neighbor.within(size_x, size_y):
                neighbors.append(y_neighbor)

        return neighbors
