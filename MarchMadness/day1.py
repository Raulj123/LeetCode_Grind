with open("1.in") as file:
    data = file.read().splitlines()
res = 0
for line in data:
    if len(line.split()) == 2:
        res += 1

print(res)
