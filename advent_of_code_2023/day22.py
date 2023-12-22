from collections import deque

filename = "file22.txt"

with open(filename) as file:
    data = file.read().splitlines()

bricks = [list(map(int, line.replace("~",",").split(","))) for line in data]
bricks.sort(key=lambda brick: brick[2])

def overlap(brick, check):
    return max(brick[0], check[0]) <= min(brick[3], check[3]) and max(brick[1], check[1]) <= min(brick[4], check[4])


for i, brick in enumerate(bricks):
    max_z = 1
    for check in bricks[:i]:
        if overlap(brick, check):
            max_z = max(max_z, check[5] + 1)
    brick[5] -= brick[2] - max_z
    brick[2] = max_z
bricks.sort(key=lambda brick: brick[2])

k_sup_v = {i: set() for i in range(len(bricks))}
v_sup_k = {i: set() for i in range(len(bricks))}

for j, upper in enumerate(bricks):
    for i, lower in enumerate(bricks[:j]):
        if overlap(lower,upper) and upper[2] == lower[5] + 1:
            k_sup_v[i].add(j)
            v_sup_k[j].add(i)
t = 0

for i in range(len(bricks)):
    q = deque(j for j in k_sup_v[i] if len(v_sup_k[j]) ==1)
    falling = set(q)
    falling.add(i)
    while q:
        j = q.popleft()
        for k in k_sup_v[j] - falling:
            if v_sup_k[k] <= falling:
                q.append(k)
                falling.add(k)
    t += len(falling) - 1
    # if all(len(v_sup_k[j]) >= 2 for j in k_sup_v[i]):
    #     t += 1
print(t)
