crates = [
    ["D", "T", "R","B", "J","L", "W", "G"],
    ["S", "W", "C"],
    ["R", "Z", "T", "M"], 
    ["D", "T", "C", "H", "S", "P", "V"], 
    ["G", "P", "T", "L", "D", "Z"], 
    ["F", "B", "R", "Z", "J", "Q", "C", "D"], 
    ["S", "B", "D", "J", "M", "F", "T", "R"], 
    ["L", "H", "R", "B", "T", "V", "M"], 
    ["Q", "P", "D", "S", "V"]
]

moves = open("day5/input.txt", "r").read().split('\n')
def part1():
    for mv in range(len(moves)):
        start_stack = int(moves[mv].split()[3])-1 # find which stack to move from
        end_stack = int(moves[mv].split()[5])-1 # find which stack to move to
        move_amount = int(moves[mv].split()[1]) # find out how many crates to move
        moving_crates = crates[start_stack][-move_amount:] # slice start stack to get last(n) crates
        moving_crates.reverse() # reverse the order of the crates before re-stacking
        crates[start_stack] = crates[start_stack][:-move_amount] # delete crates from start stack
        crates[end_stack] = crates[end_stack] + moving_crates # move crates to new stack
    for stack in range(len(crates)):
        print(crates[stack][-1]) # Answer should be SHMSDGZVC

def part2():
    for mv in range(len(moves)):
        start_stack = int(moves[mv].split()[3])-1 # find which stack to move from
        end_stack = int(moves[mv].split()[5])-1 # find which stack to move to
        move_amount = int(moves[mv].split()[1]) # find out how many crates to move
        moving_crates = crates[start_stack][-move_amount:] # slice start stack to get last(n) crates
        crates[start_stack] = crates[start_stack][:-move_amount] # delete crates from start stack
        crates[end_stack] = crates[end_stack] + moving_crates # move crates to new stack
    for stack in range(len(crates)):
        print(crates[stack][-1]) # Answer should be VRZGHDFBQ

part2()