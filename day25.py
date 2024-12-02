import time
sample_input = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""

with (open("day25.txt", "r")) as f:
    sample_input = f.read()

height = len(sample_input.split("\n"))
width = len(sample_input.split("\n")[0])

def print_grid(grid, step):
    i = 0

    if step > 0:
        print(f"\u001b[{height + 5}A")
    print(f"After {step} Steps")

    print("_" * (width + 2))
    for y in range(0, height):
        print("|", end="")
        for x in range(0, width):
            c = grid[y,x]
            if c is None:
                print(" ", end="")
            elif c.east:
                i += 1
                print('\033[93m', end="")
                print(">", end="")
                print('\033[0m', end="")
            else:
                i += 1
                print('\033[94m', end="")
                print("v", end="")
                print('\033[0m', end="")
        print("|")
    print("‾" * (width + 2))
    print(i, "cucumbers")
    #time.sleep(.01)


class cucumber:
    def __init__(self, facing_east, pos):
        self.east = facing_east
        self.pos = pos
        self.new_pos = None

    def check_move(self, grid):
        if self.east:
            if self.pos[0] + 1 >= width:
                check_pos = (0, self.pos[1])
            else:
                check_pos = (self.pos[0] + 1, self.pos[1])                
        else:
            if self.pos[1] + 1 >= height:
                check_pos = (self.pos[0], 0)
            else:
                check_pos = (self.pos[0], self.pos[1] + 1)
        # print(check_pos, height, width)
        if grid[check_pos[1], check_pos[0]] is None:
            # print(self.pos, "->", check_pos)
            self.new_pos = check_pos
            return True

        return False

    def move_if_valid(self, grid):
        if self.new_pos is not None:
            grid[self.pos[1], self.pos[0]] = None
            grid[self.new_pos[1], self.new_pos[0]] = self
            self.pos = self.new_pos
            self.new_pos = None
        return grid



east_facing = []
south_facing = []
grid = {}
for y,l in enumerate(sample_input.split("\n")):
    for x,c in enumerate(l):
        cuc = None
        if c == ">":
            cuc = cucumber(False, (y,x))
            south_facing.append(cuc)
        if c == "v":
            cuc = cucumber(True, (y,x))
            east_facing.append(cuc)

        grid[y,x] = cuc

print("Init Grid:")
print_grid(grid, 0)

step = 0
cucumbers_moving = True
while cucumbers_moving:
    cucumbers_moving = False
    step += 1
    for c in south_facing:
        moved = c.check_move(grid)
        cucumbers_moving = cucumbers_moving or moved
    for c in south_facing:
        grid = c.move_if_valid(grid)

    for c in east_facing:
        moved = c.check_move(grid)
        cucumbers_moving = cucumbers_moving or moved
    for c in east_facing:
        grid = c.move_if_valid(grid)

#    print_grid(grid, step)
print_grid(grid, 0)
print(f"Cucumbers stop moving after {step} steps")


