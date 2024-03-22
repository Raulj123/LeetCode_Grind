from datetime import (
    datetime as DateTime,
    date as Date,
    timezone as Timezone,
    timedelta as TimeDelta,
)

with open('5.in') as f:
    data = f.read().splitlines()

logs = []
map = {}
entries = {}


for line in data:
    time = line.split(":")
    log = time[1].split()
    logs.append([int(time[0]),log[0],log[1], log[2]])

logs_sorted = sorted(logs,key=lambda x: x[0])


exits = set()  # Set to store exit events

for log in logs_sorted:
    time, name, action, building = log
    if action == "->":
        if name in entries:
            print(entries[name])
        else:
            entries[name] = (time, building)
            exits.discard(name)  # Remove from exits if re-entering without exiting
    elif action == "<-":
        if name in entries:
            entries.pop(name)
            exits.add(name)
        else:
            print(f"Exit without entry for {name} detected at {time} in building {building}")

# Check for entries without corresponding exits at the end
for name, (entry_time, building) in entries.items():
    print(f"No exit for {name} detected at {entry_time} in building {building}")

