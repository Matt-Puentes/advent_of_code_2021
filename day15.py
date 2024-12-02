sample_input = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

with (open("day15.txt", "r")) as f:
    sample_input = f.read()

import time

grid = [[int(col) for col in row] for row in sample_input.split("\n")]


igs = len(grid), len(grid[0])

for i in range(1,5):
    for g in grid[-igs[0]:]:
        grid.append([gi+1 if gi < 9 else (gi + 1) % 9 for gi in g ])

for i in range(1,5):
    for i in range(len(grid)):
        grid[i] = grid[i] + [g+1 if g < 9 else (g + 1) % 9 for g in grid[i][-igs[1]:] ]

print("Grid generation finished")

from astar import find_path

def fdbf(a,b):
    if not (0 <= b[0] < len(grid) and 0 <= b[1] < len(grid[b[0]])):
        return 1000000000
    return grid[b[0]][b[1]]

result = list(find_path(
    start = (0,0),
    goal = (len(grid) - 1, len(grid[0]) - 1),
    neighbors_fnct = lambda n: [(n[0]+o[0],n[1]+o[1]) for o in [(1,0),(-1,0),(0,-1),(0,1)]],
    reversePath=False,
    heuristic_cost_estimate_fnct = lambda a, b: 0,
    distance_between_fnct = fdbf,
    is_goal_reached_fnct = lambda a, b: a == b
))
print("Lowest Risk path has risk of", sum(grid[r[0]][r[1]] for r in result) - grid[result[0][0]][result[0][1]])

def print_grid(delete=True, path=[]):
    time.sleep(.05)
    if delete:
        print(f"\u001b[{len(grid) + 2}A")
    # print(f"step {s}")
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # if node.pos == (row, col):
                # print('\033[92m', end="")
            if (row, col) in path:
                print('\033[93m', end="")
            # elif (row, col) in open_list:
            #     print('\033[94m', end="")
            # elif (row, col) in closed_list:
            #     print('\033[96m', end="")
            print(grid[row][col], end="")
            print('\033[0m', end="")
        print("")
