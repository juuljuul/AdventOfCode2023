input = open("input", "r")

# initialization
result = 0

# calculate result
for line in input:
    list_of_ints = []
    for char in line:
        if char.isdigit():
            list_of_ints.append(int(char))
    
    result += list_of_ints[0] * 10 + list_of_ints[-1]

#print result
print(result)

input.close()