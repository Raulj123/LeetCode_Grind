filename = "file6.txt"

with open(filename) as line:
    data = line.read()
    lines = data.split("\n")

times = map(int,lines[0].split()[1:])
right_time = int(''.join(map(str, times)))
anw2 = 1
distance = map(int,lines[1].split()[1:])
right_dis = int(''.join(map(str, distance)))
races = list(zip(times, distance))
anw = 1

for time, dis in races:
    print(f"time {time} dis {dis}")
    anw *= sum((time - hold) * hold >= dis for hold in range(time))
print(anw)

anw2 *= sum((right_time - hold) * hold >= right_dis for hold in range(int(right_time)))
print(anw2)
