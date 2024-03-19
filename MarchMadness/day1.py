with open("1.in") as file:
    data = file.read().splitlines()
res = 0
res2 = 0
for line in data:
    res2 += 1
    if len(line.split()) == 2:
        res += 1

print(res + res2)
