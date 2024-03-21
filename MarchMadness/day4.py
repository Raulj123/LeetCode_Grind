from math import acos, floor, sin, hypot
import itertools

with open("4.in") as f:
    data = f.read().splitlines()

grid = []
intersections = []

for line in data:
    res = line.split()
    x = res[3]
    y = res[4]
    reach = res[-1]
    x = int(x.split('=')[1].strip(','))
    y = int(y.split('=')[1].strip(','))
    reach = int(reach.split('=')[1].strip('ft'))
    grid.append((x,y,reach))

#print(f"This is grid: {grid}")

def inter(d, R1, R2):
    Pi = 3.14;

    if (d <= (R1 - R2) and R1 >= R2) :
        ans = floor(Pi * R2 * R2);
 
    elif (d <= (R2 - R1) and R2 >= R1) :
        ans = floor(Pi * R1 * R1);
 
    else :
        alpha = acos(((R1 * R1) + (d * d) - (R2 * R2)) / (2 * R1 * d)) * 2;
        beta = acos(((R2 * R2) + (d * d) - (R1 * R1)) / (2 * R2 * d)) * 2;
         
        a1 = (0.5 * beta * R2 * R2 ) - (0.5 * R2 * R2 * sin(beta));
        a2 = (0.5 * alpha * R1 * R1) - (0.5 * R1 * R1 * sin(alpha));
        ans = floor(a1 + a2);

    return ans


def canCover(x1,y1,r1,x2,y2,r2):
    dis = hypot(x2-x1,y2-y1)
    total_reach = r1 + r2
    if dis < total_reach:
        findIn = inter(dis, r1,r2)
        intersections.append(findIn)
        return True
    else:
        return False


v = 0 

for pairs in itertools.combinations(grid,2):
    p1,p2 = pairs
    if canCover(p1[0],p1[1],p1[2],p2[0],p2[1],p2[2]):
        v += 1

print(f"Total pairs of router is : {v}")
print(f"Max Inter is: {max(intersections)}")

