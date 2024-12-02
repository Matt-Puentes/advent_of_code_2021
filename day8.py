# sample_input= "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
sample_input= """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

with (open("day8.txt", "r")) as f:
    sample_input = f.read()

lines = ((x.split(" ") for x in y.split(" | ")) for y in sample_input.split('\n'))

count = 0
outputs = []
for sig_pattern, output in lines:
    translate_dict = {x: None for x in 'abcdefg'}
    numbers = [None]*10

    unknown_numbers = {2: [],3: [],4: [],5: [],6: [], 7: []}
    for x in sig_pattern:
        unknown_numbers[len(x)].append(x)

    # Find 1/4/7/8
    for x in sig_pattern:
        if len(x) == 2:
            numbers[1] = x
            unknown_numbers[2] = []
        elif len(x) == 4:
            numbers[4] = x
            unknown_numbers[4] = []
        elif len(x) == 3:
            numbers[7] = x
            unknown_numbers[3] = []
        elif len(x) == 7:
            numbers[8] = x
            unknown_numbers[7] = []

    # 6, 9, and 0
    for n in unknown_numbers[6]:
        # use 7 to find 6
        for c in numbers[7]:
            if c not in n:
                numbers[6] = n
                unknown_numbers[6].remove(n)
                print(f"Found 6, 6 does not have {c}")

    # use 4 to find 0
    for n in unknown_numbers[6]:
        for c in numbers[4]:
            if c not in n:
                numbers[0] = n
                unknown_numbers[6].remove(n)
                print(f"Found 0, 0 does not have {c}")

    numbers[9] = unknown_numbers[6][0]
    unknown_numbers[6] = []
    print(f"Leftover 6-digit number is 9")

    for n in unknown_numbers[5]:
        if numbers[1][0] in n and numbers[1][1] in n:
                numbers[3] = n
                unknown_numbers[5].remove(n)
                print(f"Found 3, 3 has both ", numbers[1][0], "and", numbers[1][1])

    for n in unknown_numbers[5]:
        for c in n:
            if c not in numbers[6]:
                numbers[2] = n
                unknown_numbers[5].remove(n)
                print(f"Found 2, 2 doesnt fit in 6")

    numbers[5] = unknown_numbers[5][0]
    unknown_numbers[5] = []
    print(f"Leftover 5-digit number is 5")

    numbers = [sorted(x) for x in numbers]
    print(numbers)
    
    output = int("".join([str(numbers.index(sorted(num))) for num in output]))
    outputs.append(output)

print("outputs: ", outputs, "sum: ", sum(outputs))
