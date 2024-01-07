# input - no need to read it in today
time = [49, 87, 78, 95]
distance = [356, 1378, 1502, 1882]

# result is a multiplication, hence initialize it with 1
result = 1

for i  in range(0,len(time)):
    win = 0
    for t in range(0,time[i]):
        passing_distance = (time[i] - t) * t
        if passing_distance > distance[i]:
            win += 1
    result *= win

print(F'{result=}')
