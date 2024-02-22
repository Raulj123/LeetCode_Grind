def blah(s):
    maxS = 0
    l = 0
    map = {}
    for r in range(len(s)):
        if s[r] not in map:
            maxS = max(maxS, r-l+1)
        else:
            if map[s[r]] < l:
                maxS = max(maxS, r-l+1)
            else:
                l = map[s[r]] + 1
        map[s[r]] = r
    return maxS



s = "abcabcbb"
res = blah(s)
print(f"result: {res}")
