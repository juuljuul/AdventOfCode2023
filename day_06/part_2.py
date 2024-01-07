# input
time = 49877895
distance = 356137815021882

# init solution
win = 0

for t in range(0,time):
    passing_distance = (time - t) * t
    if passing_distance > distance:
        win += 1

print(F'{win=}')
