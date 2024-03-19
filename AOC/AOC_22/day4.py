filename = "file1.txt"

with open(filename) as file:
    data = file.read().splitlines()


t = 0
t2 = 0
for line in data:
    a, b, c, d = map(int, line.replace(",","-").split("-"))
    # 1-5, 2-3, 2-5, 1-9
    if a <= c and b >= d or c <= a and d >= b:
        t += 1
    if set(range(a,b+1)) & set(range(c, d +1)):
        t2 += 1

print(t2)
print(t)
