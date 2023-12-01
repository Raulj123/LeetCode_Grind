filename = "file1.txt"
spelled = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open(filename, "r") as file:
    total = 0
    s = ""
    for line in file:
        for index, word in enumerate(spelled):
            while word in line:
                i = line.index(word)
                # get whats before the spelled num, replace with int, get whats after
                line = line[: i + 1] + str(index + 1) + line[i + 2 :]
        for c in line:
            if c >= "0" and c <= "9":
                s += c
                break
        for c in line[::-1]:
            if c >= "0" and c <= "9":
                s += c
                break
        total += int(s)
        s = ""

print(total)

