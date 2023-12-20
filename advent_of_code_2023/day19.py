filename = "file19.txt"

with open(filename) as file:
    block1, _ = file.read().split("\n\n")

workf = {}


for line in block1.splitlines():
    name, rest = line[:-1].split("{")
    rules = rest.split(",")
    workf[name] = ([], rules.pop())
    for rule in rules:
        comparison, target = rule.split(":")
        key = comparison[0]
        sign = comparison[1]
        n = int(comparison[2:])
        workf[name][0].append((key, sign, n, target))

def count(ranges, name="in"):
    if name == "R":
        return 0 
    if name == "A":
        product = 1
        for lo, hi in ranges.values():
            product *= hi - lo + 1
        return product
    
    rules, fallbck = workf[name]
    total = 0

    for key, sign, n, target in rules:
        lo, hi = ranges[key]
        if sign == "<":
            T = (lo, n - 1)
            F = (n, hi)
        else:
            T = (n + 1, hi)
            F = (lo, n)
        if T[0] <= T[1]:
            copy = dict(ranges)
            copy[key] = T
            total += count(copy, target)
        if F[0] <= F[1]:
            ranges = dict(ranges)
            ranges[key] = F
        else:
            break
    else:
        total += count(ranges, fallbck)
    return total

print(count({key: (1,4000) for key in "xmas"}))

# ops = {
#     ">": int.__gt__,
#     "<": int.__lt__,
# }

# def accept(item, name="in"):
#     if name == "R":
#         return False
#     if name == "A":
#         return True
#     rules, fallbck = workf[name]
#     for key, sign, n, target in rules:
#         if ops[sign](item[key],n):
#             return accept(item, target)
#     return accept(item, fallbck)


# total = 0 

# for line in block2.splitlines():
#     item = {}
#     for segment in line[1:-1].split(","):
#         char, n = segment.split("=")
#         item[char] = int(n)
#     if accept(item):
#         total += sum(item.values())

# print(total)