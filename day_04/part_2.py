input = open("input", "r")

# initialization
result = 0
n_cards = 211 # total number of scratchcards
list = [1] * n_cards # initialize list of scratchcards: one each in the beginning
index = 0 # count the index in the list

# calculate result
for line in input:
    _, cards = line.split(":") # discard "card n:"
    winning_numbers, my_numbers = cards.split("|") # distinguish winning numbers and my numbers
    list_of_my_numbers = my_numbers.split()
    list_of_winning_numbers = winning_numbers.split()
    counter = 0 # count matching numbers
    for number in list_of_my_numbers:
        if number in list_of_winning_numbers:
            counter += 1
    add = 1 # variable to add to the index
    while counter > 0:
        list[index + add] += list[index] # add as many scratchcards on the next position(s) as there are in this index
        add += 1 # go to next index
        counter -= 1
    index += 1 # go to next index

#print result
result = sum(list)
print(result)

input.close()