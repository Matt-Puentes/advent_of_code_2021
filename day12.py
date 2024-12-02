import time
start = time.time()

sample_input = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

sample_input = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

sample_input = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

with (open("day12.txt", "r")) as f:
    sample_input = f.read()

edges = [x.split("-") for x in sample_input.split("\n")]

nodes = {n: set() for x in edges for n in x}
for e in edges:
    nodes[e[0]].add(e[1])
    nodes[e[1]].add(e[0])

paths1 = [[path[1], path[0]] if path[1] == "start" else [path[0], path[1]] for path in edges if "start" in path]
paths = [(p,False) for p in paths1]
finished_paths = 0
while len(paths) > 0:
    path, has_double = paths.pop()
    if "end" in path:
        finished_paths += 1
    else:
        for n in nodes[path[-1]]:
            if n == "start":
                pass
            elif n == "end":
                finished_paths += 1
            elif n.isupper():
                paths.append((path+[n], has_double))
            elif n.islower():
                if n not in path:
                    paths.append((path+[n], has_double))
                elif n in path and not has_double:
                    paths.append((path+[n], True))

print(f"there are {finished_paths} paths")

end = time.time()
print(f"processing took {end - start}s")

