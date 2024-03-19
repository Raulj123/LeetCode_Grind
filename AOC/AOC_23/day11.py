# p1 logic: Get empty rows and cols and put them in a list of indices where they are located.
# Get the points and put them in a list of tuples where (r,c) are the indices they are at.
# Loop the points then loop again starting at 0 up to but not including i (so you can get the next points).points
# Then loop again in range of the min and max of the two poinys and if the current row index is in empty rows + 2. 
# Hard part was getting the empty cols and iterating the points.

# p2: 2 -> 10000000


filename = "file11.txt"

with open(filename) as file:
    data = file.read().splitlines()

expanded = []
cols = len(data[0])
empty_rows = [i for i, row in enumerate(data) if all(char == "." for char in row)]
empty_cols = [i for i, col in enumerate(zip(*data)) if all(char == "." for char in col)]
points = [(i,j) for i, row in enumerate(data) for j, char in enumerate(row) if char == "#" ]
t = 0
scale = 1000000
for i, (r1, c1) in enumerate(points):
    for (r2, c2) in points[:i]:
        for r in range(min(r1,r2), max(r1, r2)):
            t += scale if r in empty_rows else 1
        for c in range(min(c1, c2), max(c1,c2)):
            t += scale if c in empty_cols else 1
print(f"p1: {t}")