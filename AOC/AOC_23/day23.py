# p1 logic: Use edge contraction to get pts that have 3 or more degrees. These will have more then one option to take.
# Pts in between these points will have a length of n. Make sense? They will only have one path to take aka the only path untill it reaches above pts ^.points
filename = "file23.txt"

with open(filename) as file:
    grid = file.read().splitlines()

start = (0, grid[0].index("."))
end = (len(grid) - 1, grid[len(grid) - 1].index("."))
points = [start, end]

for r, row in enumerate(grid):
    for c, char in enumerate(row):
        neighbors = 0
        if char == "#":
            continue
        for nr, nc in [(r - 1, c), (r + 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != "#":
                neighbors += 1
        if neighbors >= 3:
            points.append((r,c))

graph = {pt: {} for pt in points}
print(f"points: {points}")
dir = {
    "^": [(-1,0)],
    "v": [(1,0)],
    ">": [(0,1)],
    "<": [(0,-1)],
    ".": [(0,-1),(0,1),(1,0),(-1,0)],
}

for sr, sc in points:
    stack = [(0,sr,sc)]
    seen = {(sr,sc)}

    while stack:
        n, r, c = stack.pop()

        if n != 0 and (r,c) in points:
            """So its a point of interest"""
            graph[(sr, sc)][(r,c)] = n
            continue 
        for dr, dc in [(0,-1),(0,1),(1,0),(-1,0)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != "#" and (nr,nc) not in seen:
                stack.append((n + 1, nr, nc))
                seen.add((nr,nc))
print(f"graph: {graph}")

seen = set()

def dfs(pt):
    if pt == end:
        return 0
    m = -float("inf")

    seen.add(pt)
    for node in graph[pt]:
        if node not in seen:
            m = max(m, dfs(node) + graph[pt][node])
    seen.remove(pt)
    return m
print(dfs(start))
