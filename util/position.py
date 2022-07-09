from typing_extensions import Self

class Pos():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def get_adjacent(self, size_x: int, size_y: int) -> list[Self]:
        adjacent = []

        for direction in [-2, 2]:
            adjacent_x = Pos(self.x + direction, self.y)
            if adjacent_x.within(size_x, size_y):
                adjacent.append(adjacent_x)

            adjacent_y = Pos(self.x, self.y + direction)
            if adjacent_y.within(size_x, size_y):
                adjacent.append(adjacent_y)

        return adjacent

    def within(self, size_x: int, size_y: int) -> bool:
        # add/subtract one to exclude outer walls
        return self.x > 0 and self.x < size_x - 1 and self.y > 0 and self.y < size_y - 1

def get_middle(pos_a: Pos, pos_b: Pos) -> Pos:
    x_direction = (pos_b.x - pos_a.x) // 2
    y_direction = (pos_b.y - pos_a.y) // 2
    return Pos(pos_a.x + x_direction, pos_a.y + y_direction)
