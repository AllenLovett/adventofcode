import re
import os
import sys
f = open(os.path.join(sys.path[0],"input.txt"), "r")

coordinates = f.read().split("\n")
totals = []

def part1():
    for entry in coordinates:
        totals.append(int(str(re.findall('\d', entry)[0])+str(re.findall('\d', entry)[-1])))
    print(sum(totals)) 

def part2():
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for entry in coordinates:
        nums = {}
        for word in words: # first look for any number words
                if len(re.findall(word, entry)) > 0:
                    for num in re.finditer(word, entry):
                        nums[num.start()] = (str(words.index(word)+1))
        for digit in re.finditer(r"\d", entry):
             nums[digit.start()] = entry[digit.start()]
        totals.append(int(sorted(nums.items())[0][1]+sorted(nums.items())[-1][1]))
    print(sum(totals))

part2()