sample_input = """target area: x=20..30, y=-10..-5"""

with (open("day17.txt", "r")) as f:
    sample_input = f.read()

goal = tuple(tuple(int(z) for z in y[2:].split('..')) for y in sample_input[13:].split(', '))

class Probe():
    def __init__(self, vel, pos = (0,0)):
        self.pos = pos
        self.vel = vel
        self.init_vel = vel
        self.sign = lambda x: 1 if x > 0 else -1 if x < 0 else 0

    def update(self):
        self.pos = (self.pos[0] + self.vel[0], self.pos[1] + self.vel[1])
        self.vel = (self.vel[0] - self.sign(self.vel[0]), self.vel[1] - 1)

highest_probe = (goal[1][1], None)
velocities = []
for x,y in [(x,y) for x in range(1, goal[0][1]+1) for y in  range(abs(goal[1][0])+1, goal[1][0]-1, -1)]:
    probe = Probe((x,y))
    highest_point = goal[1][1]
    while True:
        if probe.pos[0] > goal[0][1]: break
        if probe.pos[1] < goal[1][0]: break
        if probe.pos[1] > highest_point: highest_point = probe.pos[1]

        if goal[0][0] <= probe.pos[0] <= goal[0][1] and goal[1][0] <= probe.pos[1] <= goal[1][1]:
            velocities.append(probe.init_vel)
            if highest_point > highest_probe[0]:
                print(f"Goal reached by {probe.init_vel}")
                print(f"highest_point: {highest_point}")
                highest_probe = highest_point, probe
            break

        probe.update()

print(f"Highest probe: {highest_probe[1].init_vel}, at {highest_probe[0]}")
print(f"There were {len(velocities)} valid velocities")
