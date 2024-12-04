import os
import sys
import re

f = open(os.path.join(sys.path[0],"input.txt"), "r")

# parse input file into 2 lists for comparison
input = f.read().split("\n")

list_left = []
list_right = []

for entry in input:
    list_left.append(int(entry.split("   ")[0]))
    list_right.append(int(entry.split("   ")[1]))

    # arrange both lists in numerical order to find the most aligned pairs
    sorted_left = sorted(list_left)
    sorted_right = sorted(list_right)
    
def part1():
    
    scores = []
    for idx in range(len(list_left)):
        # get same line entry from each list and sort them biggest to smallest
        pair = sorted([sorted_left[idx], sorted_right[idx]], reverse=True)
        # subtract large from small to get the difference
        pair_score = pair[0] - pair[1]
        # keep the running total across all pairs
        scores.append(pair_score)
        
    print(sum(scores))

def part2():
    similarity_scores = []

    # For each entry in the left lise
    # multiply value by number of matching entries in right list
    for entry in sorted_left:
        similarity_scores.append(entry * sorted_right.count(entry))
    
    print(sum(similarity_scores))


part1()
part2()