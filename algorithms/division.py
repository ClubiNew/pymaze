import random
from PIL import Image
from util.cell import *
from util.position import *

def divide(img: Image, top_left: Pos, bottom_right: Pos):
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
        divide(img, top_left, Pos(new_path.x - 1, bottom_right.y))
        divide(img, Pos(new_path.x + 1, top_left.y), bottom_right)
    else:
        wall = random.randint(0, y_walls - 1) * 2 + 1
        gap = random.randint(0, x_walls) * 2
        new_path = top_left + Pos(gap, wall)

        #recurse
        divide(img, top_left, Pos(bottom_right.x, new_path.y - 1))
        divide(img, Pos(top_left.x, new_path.y + 1), bottom_right)

    # remove gap
    img.putpixel((new_path.x, new_path.y), 1)

def generate(img: Image, size_x: int, size_y: int):
    # paint path cells
    for x in range(1, size_x, 2):
        for y in range(1, size_y, 2):
            img.putpixel((x, y), 1)

    # start recursive division
    top_left = Pos(1, 1)
    bottom_right = Pos(size_x, size_y) - Pos(2, 2)
    divide(img, top_left, bottom_right)
