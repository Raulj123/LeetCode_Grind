from datetime import datetime, timezone, timedelta

with open('5.in',encoding = "utf-8") as f:
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
            sus_baka = entries[name]


            sus = datetime.utcfromtimestamp(sus_baka[0]).strftime('%Y-%m-%dT%H:%SZ')
            sus = sus.split("T")[0]
            print(f"SUS time: {sus}")
        else:
            entries[name] = (time, building)
            exits.discard(name)  # Remove from exits if re-entering without exiting
    elif action == "<-":
        if name in entries:
            entries.pop(name)
            exits.add(name)
        else:
            print(f"Exit without entry for {name} detected at {time} in building {building}")

sus_p = set()
e = 0

for log in logs_sorted:
    time = log[0]
    name = log[1]
    action = log[2]
    
    time= datetime.utcfromtimestamp(time).strftime('%Y-%m-%dT%H:%SZ')
    time = time.split("T")[0]
    # this isnt getting the right time i give up 
    
    if time == sus:
        if action == '->':
            sus_p.add(name)
            e += 1





print(len(sus_p) * (e))
