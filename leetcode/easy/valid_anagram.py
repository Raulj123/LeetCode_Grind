def isAnagram(s:str, t:str) -> bool:
    hashs, hasht = {}, {}
    for i in range(len(s)):
        hashs[s[i]] = 1 + hashs.get(s[i],0)
        hasht[t[i]] = 1 + hasht.get(t[i],0)

    for c in hashs:
        if hashs[c] != hasht[c]:
            return False
        
    return True 


s,t = "anagram","nagaram"
result = isAnagram(s,t)
print("result", result)


#time -> o(n)
#space -> o(1)? since alpha. is a fixed num and independent of the input size n