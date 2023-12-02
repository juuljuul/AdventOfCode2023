input = open("input", "r")

# initializtaion
result = 0

# calculate result
for line in input:
    id, games = line.split(":")
    true_id = id.split()[1]
    list_of_games = games.split(";")
    n_red = 0
    n_green = 0
    n_blue = 0
    cubes = {"red": 0, "green": 0, "blue": 0}
    for game in list_of_games:
        list_of_cubes = game.split(",")
        for cube in list_of_cubes:
            n, colour = cube.split()
            if colour == "red":
                cubes["red"] = max(int(n), cubes["red"])
            if colour == "green":
                cubes["green"] = max(int(n), cubes["green"])
            if colour == "blue":
                cubes["blue"] = max(int(n), cubes["blue"])
    power = cubes["red"] * cubes["blue"] * cubes ["green"]
    result += power
    

#print result
print(result)

input.close()