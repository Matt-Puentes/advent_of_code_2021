sample_input = """2199943210
3987894921
9856789892
8767896789
9899965678"""

with (open("day9.txt", "r")) as f:
    sample_input = f.read()

hmap = list(list(int(c) for c in r) for r in sample_input.split())
low_points = []

xmax, ymax = len(hmap[0]), len(hmap)

get_neighbors = (lambda x,y: [(x + o[0] , y + o[1]) for o in ((-1,0),(1,0),(0,1),(0,-1)) if x+o[0] < xmax and y+o[1] < ymax and x+o[0] >= 0 and y+o[1] >= 0])

total_risk = 0
for y in range(len(hmap)):
	for x in range(len(hmap[y])):
		if hmap[y][x] != 9:
			low_point = True
			neighbors = get_neighbors(x,y)
			for n in neighbors:
				if hmap[y][x] >= hmap[n[1]][n[0]]:
					low_point = False
			if low_point:
				risk_level = 1 + hmap[y][x]
				total_risk += risk_level
				low_points.append((x,y,))
print("Part 1: ", total_risk)

# Floodfill from low points to get basins
basins = []
for l in low_points:
	c = 0
	basin = [x for x in get_neighbors(l[0], l[1]) if hmap[x[1]][x[0]] != 9]
	while c < len(basin):
		to_check = get_neighbors(*basin[c])
		for ntc in to_check:
			if hmap[ntc[1]][ntc[0]] != 9 and ntc not in basin:
				basin.append(ntc)
		c += 1
	basins.append(basin)

top_three = [len(x) for x in sorted(basins, key=len)[-3:]]
print("Part 2:", top_three[0] * top_three[1] * top_three[2])
