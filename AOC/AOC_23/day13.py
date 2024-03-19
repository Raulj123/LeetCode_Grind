filename = "file13.txt"

with open(filename) as file:
    data = file.read().split("\n\n")

def findout(rows):
    for r in range(1, len(rows)):
        above = rows[:r][::-1]
        below = rows[r:]
        # above = above[:len(below)]
        # below = below[:len(above)]
        if sum(sum(0 if c == d else 1 for c, d in zip(x,y)) for x, y in zip(above, below)) == 1:
            return r
    return 0 

total = 0
for puzzle in data:
    rows = puzzle.split("\n")
    total += 100 * findout(rows)
    cols = list(zip(*rows))
    total += findout(cols)
print(total)
    

                