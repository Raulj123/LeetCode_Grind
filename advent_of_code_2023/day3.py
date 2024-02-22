filename = "file3.txt"

with open(filename) as line:
    data = line.read()
    lines = data.split("\n")

n = len(lines)
m = len(lines[0])
gears = [[[] for _ in range(n)] for _ in range(m)]

def isSym(i, j, num):
    if not (0 <= i < n and 0 <= j < m):
        return False
    if lines[i][j] == "*":
        gears[i][j].append(num)
    return lines[i][j] != "." and not lines[i][j].isdigit()

part_nums_sum = 0
gear_ratio_sum = 0

for i, line in enumerate(lines):
    start = 0
    j = 0
    while j < m:
        num = ""
        start = j
        gear_ratio = 0
        while j < m and line[j].isdigit():
            num += line[j]
            j += 1
        
        if num == "":
            j += 1
            continue
        
        num = int(num)

        if isSym(i, start - 1, num) or isSym(i, j, num):
            part_nums_sum += num
            continue
        
        for k in range(start - 1, j + 1):
            if isSym(i - 1, k, num) or isSym(i + 1, k, num):
                part_nums_sum += num
                break

for i in range(n):
    for j in range(m):
        nums = gears[i][j]
        if lines[i][j] == "*" and len(nums) == 2:
            gear_ratio_sum += nums[0] * nums[1]

print(f"gears: {gear_ratio_sum}")
print(f"parts: {part_nums_sum}")
