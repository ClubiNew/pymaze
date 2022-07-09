import os
import random
from PIL import Image
from algorithms import prims
from util import prompt

# get basic configuration options from the user
print("=== pymaze ===")
SIZE_X = prompt.get_int("Maze width (cells)", 3, odd=True)
SIZE_Y = prompt.get_int("Maze height (cells)", 3, odd=True)
SCALE = prompt.get_int("Maze size (px/cell)", 1)

if prompt.get_decision("Specify seed"):
    random.seed(input("Seed: "))

# algorithm select & run
print("\n=== algorithms ===")
img = Image.new('1', (SIZE_X, SIZE_Y))

algorithm_options = ["Prim's algorithm"]
selected_algorithm = prompt.get_selection(algorithm_options, "Select algorithm")

if (selected_algorithm == 0):
    prims.generate(img, SIZE_X, SIZE_Y)

# output resulting maze
print("\n=== output ===")
final_image = img.resize((SIZE_X * SCALE, SIZE_Y * SCALE))

if prompt.get_decision("Show preview"):
    final_image.show()

if prompt.get_decision("Save"):
    if not os.path.isdir("out"):
        os.makedirs("out")

    file_name = input("File name: ")
    final_image.save(f"out/{file_name}.png")
