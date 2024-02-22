
def isValid(s:str) -> bool:
    stack = []
    # loop thru s 
    # if a parethesis({[ then push to stack 
    # else check if then other end is in stack then pop 
    for char in s:
        if char == "(" or char == '{' or char == "[":
            stack.append(char)
        else:
            if not stack:
                return False
            elif char == ")" and stack[-1] == "(":
                stack.pop()
            elif char == "}" and stack[-1] == "{":
                stack.pop()
            elif char == "]" and stack[-1] == "[":
                stack.pop()
            else:
                return False

    return True

def isValid2(s:str) -> bool:
    
    mappings = {")": "(", "}": "{", "]": "["}
    stack = []
    #for each char in s, if char is a key in maps, if stack is empty or last element placed in stack doesnt match the value from the map[key] then false
    # else then its not a closing ( then append to stack 
    for char in s:
        if char in mappings:
            if not stack or stack[-1] != mappings[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    # not stack means if its empty then -> true else -> false
    return not stack 
             


s = "()[]{}"
print("Checking if valid..",s)
result = isValid(s)
result2 = isValid2(s)
print("w just the stack:", result)
print("w the map:", result2)
