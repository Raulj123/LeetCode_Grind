# p1 logic: Flood fill, while the queue is not empty check char all 4 directions and if so add to seen.
# Basically adding all the points along the pipes. To find the farthest point is just the point that is half way across
# If we go in either dir from the halfway point it would be shorter to get thier on one side or the other. 

# p2 logic: Do a horizontal scan checking if it crosses pipes(Crossing if "I" crosses meaning -- | crossed once). Get what the value of S really is by using sets and intersections. Replace S with its true val.
# Replace those not in seen(not in the loop) with a '.'

from collections import deque

filename = "file10.txt"

with open(filename) as file:
    data = file.read().splitlines()

# Find index of S
for i, line in enumerate(data):
    if "S" in line:
        s_row, s_col = i, line.index("S")

seen = {(s_row, s_col)}
queue = deque([(s_row, s_col)])
possible_s = {"|", "-", "L", "J", "7", "F", "S"}

while queue:
    curr_row, curr_col = queue.popleft()
    char = data[curr_row][curr_col]

    "Checking if current char can go up and if the symbol above it can accept comming up"
    if curr_row > 0 and char in "S|LJ" and data[curr_row - 1][curr_col] in "|7F" and (curr_row - 1, curr_col) not in seen:
        seen.add((curr_row - 1, curr_col))
        queue.append((curr_row - 1, curr_col))
        if char == "S":
            possible_s &= {"|", "L", "J"}
    "Checking if we can go down"
    if curr_row < len(data) - 1 and char in "S|7F" and data[curr_row + 1][curr_col] in "|LJ" and (curr_row + 1, curr_col) not in seen:
        seen.add((curr_row + 1, curr_col))
        queue.append((curr_row + 1, curr_col))
        if char == "S":
            possible_s &= {"|", "7", "F"}
    "Checking if we can go left"
    if curr_col > 0 and char in "S-J7" and data[curr_row][curr_col - 1] in "-LF" and (curr_row, curr_col - 1) not in seen:
        seen.add((curr_row, curr_col - 1))
        queue.append((curr_row, curr_col - 1))
        if char == "S":
            possible_s &= {"-", "7", "J"}
    "Checking right"
    if curr_col < len(data[curr_row]) - 1 and char in "S-LF" and data[curr_row][curr_col + 1] in "-J7" and (curr_row, curr_col + 1) not in seen:
        seen.add((curr_row, curr_col + 1))
        queue.append((curr_row, curr_col + 1))
        if char == "S":

            possible_s &= {"-", "L", "F"}
            
    
print(f"p1: {len(seen) // 2}")
# assert len(possible_s) == 1
(S,) = possible_s
data = [row.replace("S", S) for row in data]
data = ["".join( char if (r, c) in seen else "." for c, char in enumerate(row)) for r, row in enumerate(data)]
outside_loop = set()

for r, row in enumerate(data):
    within = False
    up = None
    for c, char  in enumerate(row):
        if char == "|":
            assert up is None
            within = not within
        elif char == "-":
            assert up is not None 
        elif char in "LF":
            assert up is None
            up = char == "L"
        elif char in "7J":
            assert up is not None
            if char != ("J" if up else "7"):
                within = not within
            up = None
        elif char == ".":
            pass
        else:
            raise RuntimeError(f"error: {char}")
        if not within:
            outside_loop.add((r,c))

print(len(data) * len(data[0]) - len(outside_loop | seen))

