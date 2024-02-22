filename = "file5.txt"

with open(filename) as line:
    data = line.read()
    lines = data.split("\n\n")

seeds = list(map(int,[line for line in lines[0].split()[1:]]))
blocks = lines[1:]
range_seeds = []
for i in range(0, len(seeds), 2):
    range_seeds.append((seeds[i], seeds[i] + seeds[i+1]))


for block in blocks:
    ranges = []
   
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int,line.split())))

    new_new = []

    while len(range_seeds) > 0:
        start, end = range_seeds.pop()
        for des, source, range_len in ranges:
            overlap_start = max(start, source)
            overlap_end = min(end, source + range_len)
            if overlap_start < overlap_end:
                new_new.append((overlap_start - source + des, overlap_end - source + des))
                if overlap_start > start:
                    range_seeds.append((start, overlap_start))
                if end > overlap_end:
                    range_seeds.append((overlap_end, end))
                break
        else:
            new_new.append((start, end))
    range_seeds = new_new
print(min(range_seeds)) 

    # for seed in seeds:   for pt 1 
    #     for des, source, range_len in ranges:
    #         if seed in range(source, source + range_len):
    #             new_new.append(seed - source + des)
    #             break
    #     else:
    #         new_new.append(seed)

#    seeds = new_new
# print(min(seeds))
