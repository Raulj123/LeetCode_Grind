import re

with open("in.txt") as file:
    data = file.read().splitlines()
c = 0
for row in data:
    for m in re.findall(r"mul\(\d{1,3},\d{1,3}\)", row):
        print(m)
        x,y = map(int, m[4:-1].split(","))
        c += x*y

print(c)
