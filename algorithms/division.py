import random
from util.canvas import Canvas
from util.cell import *
from util.position import *

def divide(canvas: Canvas, top_left: Pos, bottom_right: Pos):
    space = bottom_right - top_left + Pos(1, 1)

    x_walls = space.x // 2
    y_walls = space.y // 2

    if (x_walls == 0 and y_walls == 0):
        return

    new_path: Pos = None

    if space.x >= space.y:
        wall = random.randint(0, x_walls - 1) * 2 + 1
        gap = random.randint(0, y_walls) * 2
        new_path = top_left + Pos(wall, gap)

        #recurse
        divide(canvas, top_left, Pos(new_path.x - 1, bottom_right.y))
        divide(canvas, Pos(new_path.x + 1, top_left.y), bottom_right)
    else:
        wall = random.randint(0, y_walls - 1) * 2 + 1
        gap = random.randint(0, x_walls) * 2
        new_path = top_left + Pos(gap, wall)

        #recurse
        divide(canvas, top_left, Pos(bottom_right.x, new_path.y - 1))
        divide(canvas, Pos(top_left.x, new_path.y + 1), bottom_right)

    # remove gap
    canvas.path(new_path.x, new_path.y)

def generate(canvas: Canvas, size_x: int, size_y: int):
    # start recursive division
    top_left = Pos(1, 1)
    bottom_right = Pos(size_x, size_y) - Pos(2, 2)
    divide(canvas, top_left, bottom_right)
