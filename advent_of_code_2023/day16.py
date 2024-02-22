from collections import deque

filename = "file16.txt"

with open(filename) as file:
    data = file.read().splitlines()

"""starting point r,c,dr,dc dr, dc -> (1,0) means going down (0,1) going right"""

def cal(r,c,dr,dc):
    start = [(r,c,dr,dc)]
    seen = set()
    q = deque(start)

    while q:
        r, c, dr, dc = q.popleft()
        r += dr
        c += dc

        if r < 0 or r >= len(data) or c < 0 or c >= len(data[0]):
            continue 

        char = data[r][c]

        if char == "." or (char == "-" and dc != 0) or (char  == "|" and dr != 0):
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr ,dc))
        elif char == "/":
            """(0,1) -> (-1,0),  (1,0) -> (0,-1)  (-1,0) -> (0, 1)"""
            dr, dc = -dc, -dr
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr ,dc))
        elif char == "\\":
            dr, dc = dc, dr
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr ,dc))
        else:
            for dr, dc in [(1,0), (-1,0)] if char == "|" else [(0,1), (0,-1)]:
                if (r, c, dr, dc) not in seen:
                    seen.add((r, c, dr, dc))
                    q.append((r, c, dr ,dc))
            
    coords = {(r,c) for (r,c, _, _) in seen}
    return (len(coords))
max_val = 0

for r in range(len(data)):
    max_val = max(max_val, cal(r, -1, 0, 1))
    max_val = max(max_val, cal(r, len(data[0]), 0, -1))

for c in range(len(data)):
    max_val = max(max_val, cal(-1,c,1,0))
    max_val = max(max_val, cal(len(data),c,1,0))

print(max_val)