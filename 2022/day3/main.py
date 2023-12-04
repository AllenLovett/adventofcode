import string
backpacks = open("day3/input.txt", "r").read().split('\n')
abc = string.ascii_letters

def part1():
    priority = []
    for backpack in backpacks:
        for item in range(len(backpack)//2): # Check first half of string for compartment 1 items
            if backpack.find(backpack[item], len(backpack)//2, len(backpack)) != -1: # Find returns -1 if nothing is found, range set to second half of string
                priority.append(abc.index(backpack[item])+1) # score is determind by position in the array, plus 1 to account for zero indexing
                break # We only count the first instance of a match
    print(f"Total priority score for Backpacks: {sum(priority)}")
# part1() # Answer should be 7446

def part2():
    groups = []
    priority = []
    for group in range(0, len(backpacks), 3):  # Split input list into groups of 3
        groups.append(backpacks[group:group+3])
    # print(groups)
    for group in range(len(groups)): # Iterate over each group
        for item in range(len(groups[group][0])): # iterate over all objects in the first backpack for comparison
            if (groups[group][1].count(groups[group][0][item]) >= 1 and groups[group][2].count(groups[group][0][item]) >= 1): # count in backpacks 2 & 3 to determine a matched object
                priority.append(abc.index(groups[group][0][item])+1)# we found a common object, determine their score
                break # we only need to do this once per group
    print(f"Total priority score for Backpacks: {sum(priority)}")

part2() # Answer should be 2646