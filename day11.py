import time
sample_input="""5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

with (open("day11.txt", "r")) as f:
    sample_input = f.read()

oct_grid = [[int(c) for c in row] for row in sample_input.split("\n")]
flashed = 0
for step in range(0, 1000):
    # Raise energy level, pre-populate list of octopuses with energy > 9
    to_flash = []
    for row in range(len(oct_grid)):
        for col in range(len(oct_grid[row])):
            oct_grid[row][col] += 1
            if oct_grid[row][col] > 9:
                to_flash.append((row,col))

    # Flash octopuses with energy > 9
    while len(to_flash) > 0:
        # print("To flash: ", to_flash)
        r,c = to_flash.pop()
        oct_grid[r][c] = -1
        offsets = [(r,c) for r in range(-1,2) for c in range(-1,2) if not r == c == 0]
        neighbors = [(r + ro, c + co) for ro, co in offsets if 0 <= r + ro < len(oct_grid) and 0 <= c + co < len(oct_grid[r])]
        # print(len(offsets), offsets)
        # print(r,c, neighbors)
        # print("")
        for n in neighbors:
            nr, nc = n[0], n[1]
            if oct_grid[nr][nc] != -1:
                # print(n, " ", oct_grid[nr][nc], " + 1 =", oct_grid[nr][nc]+1)
                oct_grid[nr][nc] += 1
            if oct_grid[nr][nc] > 9 and n not in to_flash:
                # print(n, " ", oct_grid[nr][nc], " > 9")
                to_flash.append(n)

    all_flashed = True
    for row in range(len(oct_grid)):
        for col in range(len(oct_grid[row])):
            if oct_grid[row][col] == -1:
                oct_grid[row][col] = 0
                if step < 100:
                    flashed += 1
            else:
                all_flashed = False

    if all_flashed:
        print(f"pt2: {step + 1}")
        break

    # if step > 0:
    #     print("\u001b[12A")
    # print("After step ",step + 1)
    # for line in oct_grid:
    #     for o in line:
    #         if o == 0:
    #             print('\033[94m', end="")
    #         print("{0: 2d}".format(o), end="")
    #         if o == 0:
    #             print('\033[0m', end="")
    #     print("")
    # time.sleep(.01)


print(f"pt1: {flashed}")