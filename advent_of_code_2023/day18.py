filename = "file18.txt"

with open(filename) as file:
    data = file.read().splitlines()

points = [(0,0)]

dirs = {
    "U": (-1,0),
    "D": (1,0),
    "R": (0,1),
    "L": (0,-1),
}
b = 0
for line in data:
    d, n, blah = line.split()
    blah = blah[2:-1] 
    dr, dc = dirs["RDLU"[int(blah[-1])]]
    n = int(blah[:-1], 16)
    # dr, dc = dirs[d]
    # n = int(n)
    b += n 
    r, c = points[-1]
    points.append((r + dr * n, c + dc * n))

area = abs(sum(points[i][0] * (points[(i + 1) % len(points)][1] - points[i - 1][1])for i in range(len(points)))) // 2 
i = area - (b // 2) + 1
print(i + b)
