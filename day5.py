sample_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

with (open("day5.txt", "r")) as f:
    sample_input = f.read()



def main(sample_input):
	line_strs = sample_input.split("\n")
	lines = [tuple(tuple(int(n) for n in p.split(",")) for p in l.split(" -> ")) for l in line_strs]
	grid = [[0 for x in range(max([z[1] for y in lines for z in y])+1)] for y in range(max([z[0] for y in lines for z in y])+1)]

	for line in lines:
		dx = line[1][0] - line[0][0]
		dy = line[1][1] - line[0][1]
		if not (dx == 0 or dy == 0 or abs(dx) == abs(dy)):
			continue
		
		steps = abs(dx if dx is not 0 else dy) + 1
		dx = 0 if dx == 0 else -1 if dx < 0 else 1
		dy = 0 if dy == 0 else -1 if dy < 0 else 1
		
		for o in range(steps):
			try:
				grid[line[0][0] + dx*o][line[0][1]  + dy*o] += 1
			except:
				print("Step")
				print(line[0][0], dx*o, line[0][1], dy*o)
				print(line[0][0] + dx*o, line[0][1] + dy*o)
				print(len(grid), len(grid[0]))
				raise


	# for g in grid:
	# 	print(g)

	count = 0
	for r in grid:
		for g in r:
			if g >= 2:
				count+=1

	print(count)


if __name__ == "__main__":
	main(sample_input)
