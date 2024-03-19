filename = "file1.txt"

with open(filename) as file:
    data = file.read().splitlines()

t = 0
for game in data:
    opp, you = game.split()
    # rock, paper, scissors, 0, 1, 2
    opp = ord(opp) - ord("A")
    # you = ord(you) - ord("X")
    # finding out if tie or win
    # if opp == you:
    #     t += 3
    # # the next move always beats the previous 
    # elif (you - opp) % 3 == 1:
    #     t += 6
    # t += you + 1

    if you == "X":
        t += (opp - 1) % 3 + 1
    elif you == "Z":
        t += 6 + (opp + 1) % 3 + 1
    else:
        t += 3 + opp + 1
    
print(t)

 # L, draw, W