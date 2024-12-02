sample_input = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

with (open("day13.txt", "r")) as f:
    sample_input = f.read()

dots, instructions = [x.split("\n") for x in sample_input.split("\n\n")]
dots = {(int(x),int(y)) for x,y in ((q.split(",") for q in dots))}
row_max = max(d[1] for d in dots) + 1
col_max = max(d[0] for d in dots) + 1

instructions = [(x[11], int(x[13:])) for x in instructions]
# instructions = [(col_max, int(x[13:])) if x[11] == 'y' else (int(x[13:]), row_max) for x in instructions]

grid = [["." for x in range(col_max)] for y in range(row_max)]


# fold = instructions[0]
# for row in range(min(row_max, fold[1])):
#     for col in range(min(col_max, fold[0])):
#         x, y = col,row

#         # print(y, fold[1])
#         if (x,y) in dots and y < fold[1] and x < fold[0]:
#             # print("yes", y, fold[1])
#             grid[row][col] = "*"
#         if (x, fold[1] + (fold[1] - y)) in dots and y < fold[1] and x < fold[0]:
#             grid[row][col] = "*"


for fold in instructions:
    ax, pos = fold
    to_remove = []
    to_add = []
    for dot in dots:
        if ax == 'y':
            if dot[1] == pos:
                to_remove.append(dot)
            elif dot[1] > pos:
                to_remove.append(dot)
                to_add.append((dot[0], pos - (dot[1] - pos)))
        else:
            if dot[0] == pos:
                to_remove.append(dot)
            elif dot[0] > pos:
                to_remove.append(dot)
                to_add.append((pos - (dot[0] - pos), dot[1]))
    for d in to_remove:
        dots.remove(d)
    for d in to_add:
        dots.add(d)

print(dots)
debug = True
count = 0
try:
    smallest_y_cut = min(pos for ax, pos in instructions if ax == 'y')
except ValueError:
    smallest_y_cut = len(grid)
try:
    smallest_x_cut = min(pos for ax, pos in instructions if ax == 'x')
except ValueError:
    smallest_x_cut = len(grid[0])

for row in range(smallest_y_cut):
    for col in range(smallest_x_cut):
        if (col, row) in dots:
            count += 1
            if debug:
                print("\033[94m*\033[0m", end="")
        else:
            if debug:
                print(".", end="")

    if debug:
        print()

print("count: ", len(dots))