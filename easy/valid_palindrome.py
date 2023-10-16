def isPalindrome(s):
    # 1) o(n) time and o(n) memory and using isalnum  
    #res = ""
    #for c in s:
    #    if c.isalnum():
    #       res += c.lower()
    #return res == res[::-1]
   
    # 2) o(n) time but 0(1) memory and not using isalnum   
   
    def alphanum(c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )

    l, r = 0, len(s) - 1
    while l < r: 
        while l < r and not alphanum(s[l]):
            l += 1 
        while l < r and not alphanum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True 


s = "A man, a plan, a canal: Panama"
result = isPalindrome(s)
print(f"result: {result}")
