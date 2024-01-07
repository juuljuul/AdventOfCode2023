input = open("input", "r")

# initialization
result = 0#
# first line of input is just copied here
instructions = "LRLRLLRRLLRRLRRLRRRLLRLRLRLRLRRLRRRLRLRRLRLLRRLLRLRRLRLRRLLRRRLRLRLRRRLRLLRRRLLLLLLRRRLRRLLLRRLRLRRLRRLRLRRLRRLLRRLRRRLRRRLLRLRLLLRRLLLRRLLRRLRLLRRRLRRRLRRRLRLRRLRRLLLRRRLRRLLRRLRRRLRLRLRRLRRLRRRLRRRLRLLLLRRRLRLRRRLRRRLLRLRRLRRLLRLLLRRLRLRRLRRRLRRRLRRRLLRRRLRLLRRRLRRRLRRRLRRRLRRLRRRLLRRLLRLRLRRRLRRRLRLRRRR"

navigation = {}
# read in remainder of the lines
for line in input:
    position, instruction = line.split("=")
    instruction = instruction.replace("(", "")
    instruction = instruction.replace(")", "")
    left, right = instruction.split(",")
    navigation[position.strip()] = [left.strip(), right.strip()]

position = "AAA"
instruction_index = 0

# go through instructions
while position != "ZZZ":
    result += 1
    if instruction_index == len(instructions):
        instruction_index = 0
    if instructions[instruction_index] == 'L':
        position = navigation[position][0]
    elif instructions[instruction_index] == 'R':
        position = navigation[position][1]
    else:
        print("something is weird...")
    instruction_index += 1

#print result
print(result)

input.close()
