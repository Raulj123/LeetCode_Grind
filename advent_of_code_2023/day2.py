# Yes I know it's bad.

input = "file2.txt"
cubes = {"red": 12, "green": 13, "blue": 14}
game_ids_sum = 0
power_sets_sum = 0

with open(input, "r") as file:
    for line in file:
        counter = 0
        sets = line.split(";")
        game_id = int(sets[0].split(":")[0].split()[1])
        cube_counts = {"red": 0, "green": 0, "blue": 0}
        result = 1

        for set in sets:
            pairs = [pair.split() for pair in set.split(",")]
            temp = {"red": 0, "green": 0, "blue": 0}
            pairs[0] = pairs[0][-2:]
            # cube_counts = {"red": 0, "green": 0, "blue": 0}
           
            for count, color in pairs:
                temp[color] += int(count)
            
            for key in temp.keys():
                cube_counts[key] = max(cube_counts[key], temp[key])
            
        for val in cube_counts.values():
            result *= val
            
        power_sets_sum += result
            # yay = all(cube_counts[color] <= limit for color, limit in cubes.items())
#             if yay:   
#                 counter += 1
#                 if counter == len(sets):        
#                     game_ids_sum += game_id
# print(game_ids_sum)
print(f"Power set sum: {power_sets_sum}")

