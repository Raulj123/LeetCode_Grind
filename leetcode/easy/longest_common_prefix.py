def longestCommonPrefix(strs:list[str]) -> str:
    #We compare only the first and last words in the sorted list because if those words share a common prefix, then we can be sure that the rest of the words also share that prefix, due to the sorting.
    prefix = ""
    strs_sorted = sorted(strs)
    first = strs[0]
    last = strs[-1]

    for i in range(min(len(first),len(last))):
        if first[i] != last[i]:
            return prefix
        prefix += first[i]
    return prefix







strs = ["doby", "do", "doze", "ding"]
print("checking for longest prefix..")
result = longestCommonPrefix(strs)
print("Prefix: ", result)

