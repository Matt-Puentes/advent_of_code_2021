sample_input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

with (open("day10.txt", "r")) as f:
    sample_input = f.read()

pt1_score = 0
pt2_scores = []
pt1_key = {')': 3, ']': 57, '}':1197, '>':25137}
pt2_key = {')': 1, ']': 2, '}':3, '>':4}

# Match left Brackets with their right side
bracket_map = {i: o for i, o in zip("([{<",")]}>")}

for line in sample_input.split("\n"):
    error_char = None

    # Iterate over line, keep track of open chunks with stack
    s = []
    for c in line:
        if c in bracket_map:
            s.append(bracket_map[c])
        else:
            if c == s[len(s)-1]:
                s.pop()
            else:
                error_char = c
                break

    # Check/Score line
    if error_char is not None: # Syntax Error
        pt1_score += pt1_key[error_char]
    elif len(s) > 0: # Line incomplete
        pt2_score = 0
        for s in [pt2_key[char] for char in reversed(s)]:
            pt2_score *= 5
            pt2_score += s
        pt2_scores.append(pt2_score)

print("pt1: ", pt1_score)
print("pt2: ", sorted(pt2_scores)[len(pt2_scores)//2])

