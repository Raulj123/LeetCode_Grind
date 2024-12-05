with open("in.txt") as file:
  data = file.read().splitlines()

print(f"Here is the data: {data}")
dir = [(-1,0),(-1,1), (0,1), (1,1), (1,0), (1,-1),(0,-1), (-1,-1)]
# go up -> dig to right -> left .. etc in clockwise
count = 0
for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c] != "X":
            continue
        for dr, dc in dir:
            if not(0 <= r + 3 * dr < len(data) and 0 <= c + 3 * dc < len(data[0])): continue
            if data[r + dr][c + dc] == 'M' and data[r + 2 * dr][c + 2 * dc] == 'A' and data[r + 3 * dr][c + 3 * dc] == 'S':
                count += 1
                print("match")
print(count)





