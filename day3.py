from functools import reduce
from os import nice

sample = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""

with (open("day3.txt", "r")) as f:
    x = f.read()
# x = sample

# part1 = True
# if part1:
#     res = (lambda x: int(x, 2) * int("".join("0" if d == "1" else "1" for d in x), 2))(
#         "".join(
#             tuple(
#                 "1" if l[0] > l[1] else "0"
#                 for l in reduce(
#                     lambda s, n: tuple(
#                         (s[i][0] + 1, s[i][1])
#                         if n[i] == "1"
#                         else (s[i][0], s[i][1] + 1)
#                         for i in range(len(s))
#                     ),
#                     [[q for q in c] for c in [y for y in x.split()]],
#                     (((0, 0),) * len(x.split()[0])),
#                 )
#             )
#         )
#     )
#     print(res)

# part2
results = {"ox": None, "co2": None}
for test in results.keys():
    numbers = x.split()
    total = ""
    for i in range(len(numbers[0])):
        counts = [0, 0]
        for n in numbers:
            counts[int(n[i])] += 1
        if test == "ox":
            returns = ["0", "1"]
        else:
            returns = ["1", "0"]
        numbers = tuple(
            filter(
                lambda l: l[i] == (returns[0] if counts[0] > counts[1] else returns[1]),
                numbers,
            )
        )
        if len(numbers) == 1:
            results[test] = numbers[0]
            break

print(int(results["ox"], 2) * int(results["co2"], 2))
