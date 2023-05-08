def lengthOfLastWord(s:str) -> int:
    split_words = s.split()
    last = split_words[-1]
    result = len(last)
    return result

word = "Hello World"
result = lengthOfLastWord(word)
print("Length of last word: ", result)