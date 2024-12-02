sample_input = """on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13
off x=9..11,y=9..11,z=9..11
on x=10..10,y=10..10,z=10..10"""

# with (open("day22.txt", "r")) as f:
#     sample_input = f.read()


cubes = [[x.split(' ')[0] == 'on'] + [tuple(int(z) for z in y[2:].split("..")) for y in x.split(' ')[1].split(',')] for x in sample_input.split('\n')]
cubes = [(c[0], (c[1][0], c[1][1] + 1), (c[2][0], c[2][1] + 1), (c[3][0], c[3][1] + 1)) for c in cubes]

# cube intersection
# aaabbb intersection

placed_cubes = []
count = 0
for c1 in cubes:
    vol = (c1[1][1] - c1[1][0]) * (c1[2][1] - c1[2][0]) * (c1[3][1] - c1[3][0])
    print("\nCube ", c1)
    print('vol', vol)
    overlap = 0
    for c2 in placed_cubes:
        print('c2 ', c2)
        x_over = max(min(c1[1][1], c2[1][1]) - max(c1[1][0], c2[1][0]),0)
        y_over = max(min(c1[2][1], c2[2][1]) - max(c1[2][0], c2[2][0]),0)
        z_over = max(min(c1[3][1], c2[3][1]) - max(c1[3][0], c2[3][0]),0)
        print('overlap: ', x_over, y_over, z_over)
        overlap += x_over * y_over * z_over
        print("total overlap so far", overlap)

    print("vol, overlap, diff", vol, overlap, vol-overlap)
    if c1[0]:
        count += vol - overlap
    else:
        count -= vol - overlap
    print("new count", count)

    placed_cubes.append(c1)
