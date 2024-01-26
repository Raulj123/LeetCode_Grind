filename = "file1.txt"

with open(filename) as file:
    data = file.readlines()

sum_ = 0 
cal = []
print(f"data: {data}")
for item in data:
    if item != "\n":
        sum_ += int(item)
    else:
        cal.append(sum_)
        sum_ = 0
cal.sort(reverse=True)
print(f"pt1: {cal[0]}")
print(f"pt2: {cal[:3]}")
