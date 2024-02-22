def generateParenthesis(n):
    res = []
    stack = []

    def recursiveFunc(openN, closedN):
        if openN == closedN == n:
            print("joining on", openN, closedN)
            res.append("".join(stack))
            return
        
        if openN < n:
            stack.append("(")
            print("adding (", openN, closedN)
            recursiveFunc(openN + 1, closedN)
            stack.pop() 
            print("popping on:", openN, closedN)
            print(stack)

        if closedN < openN:
            stack.append(")")
            print("adding )", openN, closedN)
            recursiveFunc(openN, closedN + 1)
            stack.pop()
            print("popping on:", openN, closedN)


    recursiveFunc(0,0)
    return res


n = 2 
result = generateParenthesis(n)
print(f"results: {result}")
