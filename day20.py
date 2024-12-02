sample_input = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###"""

with (open("day20.txt", "r")) as f:
    sample_input = f.read()


algo, image = sample_input.split("\n\n")
image = image.split("\n")

pixels = set()

for row in range(len(image)):
	for col in range(len(image[row])):
		if image[row][col] == '#':
			pixels.add((row,col))

for row in range(-5, 11):
	for col in range(-5, 11):
		print('#' if (row,col) in pixels else '.', end="")
	print("")
print("="*15)

step = 0
while step < 2:
	step += 1
	rmin, cmin = min(y[0] for y in pixels) - 1, min(y[1] for y in pixels) - 1
	rmax, cmax = max(y[0] for y in pixels) + 2, max(y[1] for y in pixels) + 2
	new_pixels = set()
	for row in range(rmin, rmax):
		for col in range(cmin, cmax):
			neighbors = [(row+x,col+y) for x in range(-1,2) for y in range(-1,2)]
			binary = ""
			for n in neighbors:
				binary += '1' if n in pixels else '0'
			index = int(binary,2)
			# if row < 0 and col < 0:
			# 	print(pixels)
			# 	print(neighbors)
			# 	print(row, col, binary, index)
			if algo[index] == '#':
				new_pixels.add((row, col))
	pixels = new_pixels


for row in range(-5, 11):
	for col in range(-5, 11):
		print('#' if (row,col) in pixels else '.', end="")
	print("")
print("="*15)


print(f"after {step} steps there are {len(pixels)} pixels")