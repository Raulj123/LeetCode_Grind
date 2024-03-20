from collections import deque

def get(foods,name, wish):
    v = set()
    q= deque()
    c = 0
    imake = 0 
    q.append(name)
    v.add(name)
    wish = name
    while q:
        name = q.popleft()
        

        if name not in foods:
            continue

        for n in foods[name]:
            n = n.strip()
            if n not in v:
                q.append(n)
                v.add(n)
                c += 1


    
    for item in v:

        if item in wish:
            continue
        elif item in foods:
            c -= 1
    print(f"retu {c}")
    return c



with open("3.in") as file:
    data = file.read().splitlines()

foods = {}

for ing in data[2:]:
    name, ingredi = ing.split("=")
    need = ingredi.split("+")

    foods[name.strip()] = need

wish = data[0].split(":")
wish = wish[1].split(",")
wish = [n.strip() for n in wish]
print(f"wish: {wish}")
res = 0
for name in wish:
    res += get(foods, name, wish)
    print(res)

print(res)
