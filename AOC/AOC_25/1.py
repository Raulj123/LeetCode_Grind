
def readFile():
    with open("1.txt") as file:
        data = file.read().splitlines()
    return data


def part1():
    data = readFile()
    curr = 50
    zero = 0

    for rotation in data:
        direction = rotation[0]
        points = int(rotation[1:])
        if direction == "L":
            points = - points    
        curr = (curr + points) % 100
        if curr == 0:
            zero += 1
    print("1:", zero)

# I looked part 2 up shit was confusing 
def part2():
    data = readFile()
    curr = 50
    zero = 0

    for rotation in data:
        direction = rotation[0]
        points = int(rotation[1:])
        if direction == "L":
            points = - points    
            turns, offset = divmod(points, -100)
            zero += turns
            if curr != 0 and curr + offset <= 0:
                zero += 1
        else:
            turns, offset = divmod(points,100)
            zero += turns
            if curr != 100 and curr + offset >=100:
                zero += 1

        curr = (points + curr) % 100
    print("2:", zero)


part1()
part2()