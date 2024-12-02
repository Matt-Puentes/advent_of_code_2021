"""
Template:     NNCB
After step 1: NCNBCHB
After step 2: NBCCNBBBCBHCB
After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
"""

"""
After the first step of this process, the polymer becomes NCNBCHB.

Here are the results of a few steps using the above rules:

Template:     NNCB
After step 1: NCNBCHB
After step 2: NBCCNBBBCBHCB
After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB

This polymer grows quickly. After step 5, it has length 97; After step 10, it has length 3073. After step 10, B occurs 1749 times, C occurs 298 times, H occurs 161 times, and N occurs 865 times; taking the quantity of the most common element (B, 1749) and subtracting the quantity of the least common element (H, 161) produces 1749 - 161 = 1588.

Apply 10 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?
"""
from collections import Counter
from collections import defaultdict

sample_input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""



with (open("day14.txt", "r")) as f:
    sample_input = f.read()

template, rulestr = sample_input.split("\n\n")

rules = [x.split(" -> ") for x in rulestr.split("\n")]
rules = {q[0]: (q[0][0] + q[1],  q[1] + q[0][1]) for q in [x.split(" -> ") for x in rulestr.split("\n")]}
print(rules)

count = {k: 0 for k in rules}
for x in [k+template[j+1] for j,k in enumerate(template) if j < len(template) - 1]:
    count[x] += 1

for step in range(1,41):
    new_count = {k: 0 for k in rules}
    for k,v in count.items():
        new_count[rules[k][0]] += v
        new_count[rules[k][1]] += v
    count = new_count

final_count = defaultdict(int)
for k,v in count.items():
    print(k,v)
    final_count[k[0]] += v
final_count[template[-1]] += 1

most_common = sorted(final_count.items(), key=lambda x: x[1])[-1]
least_common = sorted(final_count.items(), key=lambda x: x[1])[0]
print(f"After {step} steps")
print(final_count)
print(most_common, least_common)
print(most_common[1] - least_common[1])

