from math import inf

# Build input
sample_input = "16,1,2,0,4,2,7,1,2,14"

with (open("day7.txt", "r")) as f:
    sample_input = f.read()
crabs = [int(x) for x in sample_input.split(",")]
pt1 = min([sum(abs(crab-pos) for crab in crabs) for pos in range(min(crabs), max(crabs))])
pt2 = min([sum((abs(crab-pos)*(abs(crab-pos)+1))//2 for crab in crabs) for pos in range(min(crabs), max(crabs))])
print("part1: ", pt1)
print("part2: ", pt2)

# Set to True to solve for part 1
part1 = False

# Calculate cost
min_fuel = (None, inf)
for pos in range(min(crabs), max(crabs)):
    fuel = 0
    for crab in crabs:
        d = abs(crab-pos)
        if part1:
            fuel += d
        else: # part2
            fuel += (d*(d+1))/2 # equiv. to 1 + 2 + ... + n
    if fuel < min_fuel[1]:
        min_fuel = pos, fuel


print(f"it takes {int(min_fuel[1])} fuel for the crabs to move to position {int(min_fuel[0])}")


