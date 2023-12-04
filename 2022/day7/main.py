console = open("day7/input.txt", "r").read().split('$') # break input into commands & responses
def part1():
    commands = [line.strip().split('\n') for line in console] # ['command', 'reponse(0)', 'reponse(1)', 'response(n)']
    # print(commands)
    filesystem = []
    directory = []
    commands.pop(0) # bad input from split
    for cmd in range(len(commands)):
        if commands[cmd][0].split()[0] == "cd": 
            if commands[cmd][0].split()[1] != "..": # moving down into another dir
                filesystem.append(commands[cmd][0].split()[1])
        if commands[cmd][0].split()[0] == "ls":
            filesystem[filesystem.index(commands[cmd-1][0].split()[1])] = [commands[cmd-1][0].split()[1],commands[cmd][1:]]
            

    

part1()