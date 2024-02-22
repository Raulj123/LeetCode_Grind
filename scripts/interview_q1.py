test = "Hello world"

def count_max_char(test):
    map = {}
    max_num = 0
    key_max = ""
    res = ""
    for char in test:
        map[char] = 0

    for char in test:
        if char in map:
            map[char] += 1
    for char, times in map.items():
        if times > max_num:
            max_num = times
            key_max = char

    res = key_max + ":" + str(max_num)

    return res

print(count_max_char(test))

