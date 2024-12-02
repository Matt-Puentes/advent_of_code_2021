sample_input = """[1,1]
[2,2]
[3,3]
[4,4]"""
sample_input = """[[[[9,8],1],2],3]
4"""
# sample_input = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
# [[[5,[2,8]],4],[5,[[9,9],0]]]
# [6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
# [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
# [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
# [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
# [[[[5,4],[7,7]],8],[[8,3],8]]
# [[9,3],[[9,9],[6,[4,9]]]]
# [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
# [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]""" # [[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]] 4140

# with (open("day18.txt", "r")) as f:
#     sample_input = f.read()

numbers = [eval(l) for l in sample_input.split()]

class Node:
    def __init__(self, parent):
        self.parent = parent
        self.l = None
        self.r = None
        if parent is None:
            self.depth = 0
        else:
            self.depth = self.parent.depth

    def __str__(self):
        return f"({str(self.l)},{str(self.r)})"


def build_graph(num_list, parent):
    node = Node(parent)
    node.l = build_graph(num_list[0], node) if isinstance(num_list[0], list) else num_list[0]
    node.r = build_graph(num_list[1], node) if isinstance(num_list[1], list) else num_list[1]
    return node

first_number = numbers.pop(0)
root = build_graph(first_number, None)

while len(numbers) > 0:
    new_number = build_graph(numbers.pop(0), None)
    root = Node

# num = [numbers.pop(0), None]

# while len(numbers) > 0:
#     # Addition
#     num[1] = numbers.pop(0)

#     # explode, return 0 if none
#     def explode(snum, i, to_explode=None):
#         print(f"at {snum} {to_explode}")
#         if isinstance(snum[0], list):
#             ret = explode(snum[0], i + [0])
#             snum[0] = ret
#         if isinstance(snum[1], list):
#             ret = explode(snum[1], i + [0])
#             snum[1] = ret

#         if len(i) >= 4 and to_explode is None:
#             print(f"exploding {snum} at {i}")
#             snum = 0
#             to_explode = snum, i
#             any_exp = True
#         return snum

#     def add_to_neighbor(val, index, to_right):
#         pass


#     ret = explode(num, [])
#     print(ret)


    # Split, return 0 if none,
    # continue





# magnitude of pair
# 3 * magnitude of left + 2 * magnitude of right
# lone numbers are their own magnitude
# [[1,2],[[3,4],5]] becomes 143.
# [[[[0,7],4],[[7,8],[6,0]]],[8,1]] becomes 1384.
# [[[[1,1],[2,2]],[3,3]],[4,4]] becomes 445.
# [[[[3,0],[5,3]],[4,4]],[5,5]] becomes 791.
# [[[[5,0],[7,4]],[5,5]],[6,6]] becomes 1137.
# [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]] becomes 3488.

# To explode a pair, the pair's left value is added to the first regular number to the left of the 
# exploding pair (if any), and the pair's right value is added to the first regular number to the right 
# of the exploding pair (if any). Exploding pairs will always consist of two regular numbers. Then, 
# the entire exploding pair is replaced with the regular number 0.

# To split a regular number, replace it with a pair; the left element of the pair should be the regular number 
# divided by two and rounded down, while the right element of the pair should be the regular number divided by 
# two and rounded up. For example, 10 becomes [5,5], 11 becomes [5,6], 12 becomes [6,6], and so on.