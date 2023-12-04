assignments = open("day4/input.txt", "r").read().split('\n')
overlaps = 0
def part1():
    global overlaps
    for assignment in range(len(assignments)):
        assignment1 = assignments[assignment].split(',')[0]
        assignment2 = assignments[assignment].split(',')[1]
        if (int(assignment1.split('-')[0]) >= int(assignment2.split('-')[0])) and (int(assignment1.split('-')[1]) <= int(assignment2.split('-')[1])):
            overlaps +=1
        elif (int(assignment2.split('-')[0]) >= int(assignment1.split('-')[0])) and (int(assignment2.split('-')[1]) <= int(assignment1.split('-')[1])):
            overlaps +=1
    print(f"Detected {overlaps} overlaps") # Answer should be 534
def part2():
    global overlaps
    for assignment in range(len(assignments)):
        assignment1 = assignments[assignment].split(',')[0]
        assignment2 = assignments[assignment].split(',')[1]
        if (int(assignment1.split('-')[0]) >= int(assignment2.split('-')[0])) and (int(assignment1.split('-')[0]) <= int(assignment2.split('-')[1])):
            overlaps +=1
        elif (int(assignment2.split('-')[0]) >= int(assignment1.split('-')[0])) and (int(assignment2.split('-')[0]) <= int(assignment1.split('-')[1])):
            overlaps +=1
    print(f"Detected {overlaps} overlaps") # Answer should be 841

part2()