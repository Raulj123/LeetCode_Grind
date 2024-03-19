def isCross(path):
    dir = {
        "N": (0,1),
        "S": (0,-1),
        "E": (1,0),
        "W": (-1,0),
    }
    x, y = 0, 0 
    seen = {(x,y)}

    for c in path:
        dirx, diry = dir[c]
        x = x + dirx
        y = y + diry
        if (x,y) in seen:
            return True
        seen.add((x,y))
    return False


path = "NESWW"
a = isCross(path)
if a == True:
    print("Passed!")
else:
    print("Failed")
