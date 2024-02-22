filename = "file1.txt"

with open(filename) as file:
    data = file.read().splitlines()
t = 0
for line in data:
    length = len(line)
    size = length // 2
    first = line[:size]
    sec = line[size:]
    for char in first:
        if char in sec:
            type_ = char
    
    if 'a' <= type_ <= 'z':
        t += ord(type_) - ord('a') + 1
    elif 'A' <= type_ <= 'Z':
        t += ord(type_) - ord('A') + 27

print(t)
t2 = 0
i = 0
while i < len(data):
    for char in data[i]:
        if char in data[i+1] and char in data[i+2]:
            if 'a' <= char <= 'z':
                t2 += ord(char) - ord('a') + 1
            elif 'A' <= char <= 'Z':
                t2 += ord(char) - ord('A') + 27
            break
    i += 3
print(f"pt2: {t2}")

