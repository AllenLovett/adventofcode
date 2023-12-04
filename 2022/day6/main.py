stream = open("day6/input.txt", "r").read()
char_index = 0
found = 0
def part1(): # Answer: 1142
    global char_index
    global found
    for char in range(len(stream)):
        marker_check = stream[char_index:char_index+4] # slice 4 characters
        char_index += 1
        if len(set(marker_check)) == 4 and found == 0: # set conversion will only include unique characters
            print(f"Found at: {char_index+3}")
            found = 1

def part2(): # Answer: 2803
    global char_index
    global found
    for char in range(len(stream)):
        marker_check = stream[char_index:char_index+14] # slice 4 characters
        char_index += 1
        if len(set(marker_check)) == 14 and found == 0: # set conversion will only include unique characters
            print(f"Found at: {char_index+13}")
            found = 1
part2()