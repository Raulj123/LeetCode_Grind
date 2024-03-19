filename = "file15.txt"

with open(filename) as file:
    data = file.read().split(",")



def hash(value):
    ans = 0 
    for c in value:
        ans += ord(c)
        ans *= 17
        ans %= 256
    return ans
    #     total = 0
    #     curr = 0
    #     for num in lis:
    #         curr = num
    #         total += curr
    #         mul = total * 17 
    #         div = mul % 256
    #         total = div
    #     ans += total
    # print(ans)
        


values = [[ord(c) for c in string] for string in data]
# hash(values)

boxes = [[] for _ in range(256)]
focal_len = {}

for instruction in data:
    if "-" in instruction:
        label = instruction[:-1]
        ind = hash(label)
        if label in boxes[ind]:
            boxes[ind].remove(label)
    else:
        label, length = instruction.split("=")
        length = int(length)
        ind = hash(label)
        if label not in boxes[ind]:
            boxes[ind].append(label)
        focal_len[label] = length
total = 0

for box_num, box in enumerate(boxes, 1):
    for lens_slot, label in enumerate(box,1):
        total += box_num * lens_slot * focal_len[label]
print(f"p2: {total}")