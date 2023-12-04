input = open("input", "r")

# initialization
result = 0

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
    if counter > 0: # only add if there are any matching cards
        result += 2**(counter-1) # count a power of two

#print result
print(result)

input.close()