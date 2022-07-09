# pymaze

pymaze is a python program for maze generation. Simply run `main.py` and select the maze size, resolution, seed and algorithm to use. Saved mazes will output to the `pymaze/out` directory.

# Supported Algorithms

pymaze currently has one algorithm to choose from. Each algorithm produces stylistically unique results.

## 1. Prim's Algorithm

Using a simplified and randomized version of [Prim's algorithm](https://en.wikipedia.org/wiki/Prim%27s_algorithm), you can generate a maze biased towards many short dead ends.

<details>
    <summary><b>Example Results</b></summary>
    <img src="examples/prims/99x33.png" alt="63x43 Prim's maze" />
    <img src="examples/prims/49x49.png" alt="49x49 Prim's maze" />
</details>

## 2. Randomized depth-first search

Using a randomized iterative depth-first search, you can generate a maze with many long corridors.

<details>
    <summary><b>Example Results</b></summary>
    <img src="examples/dfs/99x33.png" alt="99x33 DFS maze" />
    <img src="examples/dfs/49x49.png" alt="49x49 DFS maze" />
</details>

**_Note:_** All of the example mazes are generated with their extension-less file name (i.e. 99x33) as the seed, should you wish to re-create them.
