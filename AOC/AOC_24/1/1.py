listA  = []
listB  = []
dis = 0
sim = 0

with open("in.txt") as file:
    data = file.read().splitlines()

for pair in data:
    a,b = pair.split()
    listA.append(int(a))
    listB.append(int(b))

listA.sort()
listB.sort()

for a, b in zip(listA, listB):
    dis += abs(a - b)

for a in listA:
    sim += (a * listB.count(a))

print(f"pt1: {dis} \n pt2: {sim}")