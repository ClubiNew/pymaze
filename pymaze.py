from algorithms import prims, dfs, wilsons, division
from util import prompt, canvas
import random

# get basic configuration options from the user
print("=== pymaze ===")
size_x = prompt.get_int("Maze width (cells)", 5, odd=True)
size_y = prompt.get_int("Maze height (cells)", 5, odd=True)
scale = prompt.get_int("Maze size (px/cell)", 1)
animated = prompt.get_decision("Animated")

canvas = canvas.Canvas(size_x, size_y, scale, animated)

if prompt.get_decision("Specify seed"):
    random.seed(input("Seed: "))

# algorithm select & run
print("\n=== algorithms ===")
algorithm_options = ["Prim's algorithm", "Randomized depth-first search", "Wilson's algorithm", "Recursive division"]
selected_algorithm = prompt.get_selection(algorithm_options, "Select algorithm")

if (selected_algorithm == 0):
    prims.generate(canvas, size_x, size_y)
elif (selected_algorithm == 1):
    dfs.generate(canvas, size_x, size_y)
elif (selected_algorithm == 2):
    wilsons.generate(canvas, size_x, size_y)
elif (selected_algorithm == 3):
    division.generate(canvas, size_x, size_y)

# output resulting maze
print("\n=== output ===")
if prompt.get_decision("Show preview"):
    canvas.preview()

if prompt.get_decision("Save"):
    file_name = input("File name: ")
    if not animated:
        canvas.save(file_name)
    else:
        duration = prompt.get_int("Duration (s)", 2)
        fps = prompt.get_int("FPS (#)", 1)
        canvas.save_animated(file_name, fps, duration)
