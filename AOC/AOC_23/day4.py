from collections import defaultdict

filename = "file4.txt"

with open(filename) as line:
    data = line.read()
    lines = data.split("\n")

total_pts = 0
copies = defaultdict(int)

for i, line in enumerate(lines):
    copies[i] += 1
    nums = line[10:].split("|")
    win_nums = set(nums[0].split())
    options = set(nums[1].split())
    bingo = options.intersection(win_nums)

    if bingo:
        found = len(bingo)
        
        if found > 1:
            worth = 1
            for n in range(1,found):
                worth =  worth * 2
        else:
            worth = 1
        total_pts += worth

        for j in range(found):
            copies[i + 1 + j] += copies[i]
            
        
print(f"p1: {total_pts}")
print(f"pt: {sum(copies.values())}")
    

    
