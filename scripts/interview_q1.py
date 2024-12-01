from collections import Counter
test = "Hello world"

def count_max_char(test):
    map1 = {}
    for char in test:
        if char in map1:
            map1[char] += 1
        else:
            map1[char] = 1
        
    maxKey = max(map1, key=map1.get)
    print(f"{maxKey}:{map1[maxKey]}")
   
def better(test):
    freq = Counter(test)
    key = max(freq, key=freq.get)
    print(f"{key}:{freq[key]}")


count_max_char(test)
better(test)
