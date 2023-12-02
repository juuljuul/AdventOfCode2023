input = open("input", "r")

# initialization
result = 0
alpha_numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

# calculate result
for line in input:
    i = 0
    list_of_ints = []
    for i, char in enumerate(line):
        if char.isdigit():
            list_of_ints.append(int(char))
        else:
            for key in alpha_numbers:
                if line[i:].find(key) == 0:
                    list_of_ints.append(int( alpha_numbers[key]))
    
    result += list_of_ints[0] * 10 + list_of_ints[-1]

print(result)

input.close()