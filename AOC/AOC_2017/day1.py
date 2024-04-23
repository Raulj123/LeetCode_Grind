import argparse

parser = argparse.ArgumentParser()
parser.add_argument('square', help="yes", type=int)
args = parser.parse_args()
print(args.square**2)
with open("1.in") as file:
    data = file.readline().strip()


data = list(data)
n = len(data)
sum = 0

for i in range(1,n):
    if data[i] == data[i - 1]:
        sum += int(data[i])

if data[0] == data[-1]:
    sum += int(data[0])

print(sum) 
