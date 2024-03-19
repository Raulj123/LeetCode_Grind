filename = "file14.txt"

with open(filename) as file:
    transpose = tuple(file.read().splitlines())
total = 0
def cycle():
    global transpose 
    for _ in range(4):
        transpose = tuple("".join(row) for row in list(zip(*transpose)))
        transpose = tuple("#".join("".join(sorted(list(group), reverse=True)) for group in col.split("#"))for col in transpose)
        # transpose = ["".join(row) for row in list(zip(*transpose))]
        transpose = tuple(row[::-1] for row in transpose)

seen = {transpose}
array = [transpose]
iter = 0

while True:
    iter += 1
    cycle()
    if transpose in seen:
        break
    seen.add(transpose)
    array.append(transpose)
first = array.index(transpose)
transpose = array[(1000000000 - first) % (iter - first) + first]

print(sum(col.count("O") * (len(transpose) - c) for c, col in enumerate(transpose)))

     
