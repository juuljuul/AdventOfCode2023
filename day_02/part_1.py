input = open("input", "r")

# initializtaion
result = 0

n_red = 12
n_green = 13
n_blue = 14

# calculate result
for line in input:
    id, games = line.split(":")
    true_id = id.split()[1]
    list_of_games = games.split(";")
    count_round = True
    for game in list_of_games:
        list_of_cubes = game.split(",")
        for cube in list_of_cubes:
            n, colour = cube.split()
            if colour == "red":
                if (int(n) > n_red):
                    count_round = False
            if colour == "green":
                if (int(n) > n_green):
                    count_round = False
            if colour == "blue":
                if (int(n) > n_blue):
                    count_round = False
    if count_round:
        result += int(true_id)

#print result
print(result)

input.close()