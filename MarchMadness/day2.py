grid = []

with open("2.in") as f:
    for line in f.readlines():
        left = line.split(' ')[0]
        grid.append([c for c in left])


hash = sum(row.count('#') for row in grid)

dots = sum(row.count('.') for row in grid)


room_height = len(grid)
room_width = len(grid[0])

print(f"room h : {room_height}")
print(f"room w: {room_width}")

placements = 0
crate_size = 15
    

for i in range(room_height-15):  
    for j in range(room_width-15):  
        if grid[i][j] == ".":
            if all(grid[x][y] == "." for x in range(i, i + 15) for y in range(j, j + 15)):
                placements +=1
            


print(f"place: {placements}")

print(f"{dots} m2")


