from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[str]:
    result = defaultdict(list)
    for s in strs:
      count = [0] * 26
      for c in s:
        count[ord(c) - ord("a")] += 1
      result[tuple(count)].append(s)
    return result.values()    
    


strs = ["eat","tea","tan","ate","nat","bat"]
result =  groupAnagrams(strs)
print("result:" ,result)

# time - > o(m * n * 26) -> o(m*n) where m is the num of strs and n is num of char per strs 
# space -> o(n) n is the number of strings in strs