# p1 logic: cycle the path(LLRR) infinitely get the current node and the path
# if current path is R then true and send a 1. Stop the loop when it ZZZ.

# p2 logic: Get a list of nodes that end with A. Send each of them to p2 fun.
# while current node doesn't end with 'Z' find the current iteration of path.
# Get the node corresponding to the step and increase path. Once you get a list of all those find the LCM.

from itertools import cycle
import math
filename = "file8.txt"

with open(filename) as file:
    data = file.read()

path, instructions = data.split("\n\n")
instructions = [place.split(" = ") for place in instructions.splitlines()]
instructions = {a: b[1:-1].split(", ") for a,b in instructions}
current = "AAA"

# for i, direction in enumerate(cycle(path)):
#     # if dir == R then true aka 1 else 0, left dir
#     current = instructions[current][direction == "R"]
#     if current == "ZZZ":
#         print(f"p1: {i + 1}")
#         break

def p2(node):
    count = 0
    while(node[-1] != "Z"):
        step = path[count % len(path)]
        node = instructions[node][step == "R"]
        count += 1
    return count

nodesA = [key for key in instructions.keys() if key[-1] == "A"] 
counts = [p2(node) for node in nodesA]
a = math.lcm(*counts)
print(f"pt: {a}")