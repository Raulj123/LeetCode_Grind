def romanToInt(s: str) -> int:
    number = 0
    map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    #comparing 2 numbers if a less than subtract frm number else add to number. 
    for i in range(len(s)-1 ):
        if map[s[i]] < map[s[i+1]]:
            number -= map[s[i]]
        else:
            number += map[s[i]]
    return number + map[s[-1]]




s = "MCMXCIV"
print("Converting ", s, "to int")
result = romanToInt(s)
print("Result: ", result)