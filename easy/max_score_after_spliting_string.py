def maxScore(s):
    max_score = 0

    for i in range(len(s) - 1):
        left_side = s[:i + 1]
        right_side = s[i + 1:]
        left_count = left_side.count("0")
        right_count = right_side.count("1")
        max_score = max(max_score, left_count + right_count)
    return max_score




s = "0000"
s = maxScore(s)
if s == 3:
    print("Passed: ", s)
else:
    print("Failed", s)
