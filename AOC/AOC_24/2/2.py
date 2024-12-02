safe = 0

with open("in.txt") as file:
    data = file.read().splitlines()

reports = []


for line in data:
    report = list(map(int, line.split()))
    reports.append(report)

for report in reports:
    diff = [x - y for x, y in zip(report, report[1:])]
    if all(1 <= n <= 3 for n in diff) or all(-1 >= n >= -3 for n in diff):
        safe += 1

print(safe)

