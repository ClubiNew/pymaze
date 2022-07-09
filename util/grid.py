import random

class Pos():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def within(self, size_x: int, size_y: int) -> bool:
        # add/subtract one to exclude outer walls
        return self.x > 0 and self.x < size_x - 1 and self.y > 0 and self.y < size_y - 1

def random_path_pos(size_x: int, size_y: int) -> Pos:
    # pick only odd numbers (path positions)
    x = random.randint(0, size_x // 2 - 1) * 2 + 1
    y = random.randint(0, size_y // 2 - 1) * 2 + 1
    return Pos(x, y)

def get_middle(pos_a: Pos, pos_b: Pos) -> Pos:
    x_direction = (pos_b.x - pos_a.x) // 2
    y_direction = (pos_b.y - pos_a.y) // 2
    return Pos(pos_a.x + x_direction, pos_a.y + y_direction)
