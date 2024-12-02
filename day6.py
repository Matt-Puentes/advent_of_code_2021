# Input
sinput = "3,4,3,1,2"
with (open("day6.txt", "r")) as f:
    sinput = f.read()

# Fish construction
fish_dict = {i: 0 for i in range(-1, 9)}
for x in sinput.split(","):
	fish_dict[int(x)] += 1

# Simulation
Human Computer Interactions
Foundations of Computer Science
Tools and Techniques in computer security
pt1 = [80, None]
pt2 = [256, None]
for day in range(0, max(pt1[0],pt2[0])):	
	for i in range(0, 9):
		fish_dict[i-1] += fish_dict[i]
		fish_dict[i] = 0

	fish_dict[8] += fish_dict[-1]
	fish_dict[6] += fish_dict[-1]
	fish_dict[-1] = 0

	if day == pt1[0] - 1:
		pt1[1] = sum([fish_dict[i] for i in range(-1, 9)])
	if day == pt2[0] - 1:
		pt2[1] = sum([fish_dict[i] for i in range(-1, 9)])

# Result
print(f"after {pt1[0]} days there are {pt1[1]} fish")
print(f"after {pt2[0]} days there are {pt2[1]} fish")




part1 = False

if part1:
	day = 0
	while True:
		day += 1

		new_fish = []
		for i in range(len(fish)):
			fish[i] -= 1
			if fish[i] < 0:
				fish[i] = 6
				fish.append(8)

		if day == 80:
			break
	print(f"after {day} days there are {len(fish)} fish")


Associate Electrical Engineer
- Maintained and continued development on a python testing and automation framework
- Did data analysis and visualization generation using Matplotlib

