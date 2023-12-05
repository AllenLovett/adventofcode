import re
import os
import sys
f = open(os.path.join(sys.path[0],"input.txt"), "r")

results = f.read().split("\n")

limits = {"red": 12, "blue": 14, "green": 13}
possible_games = []

def part1():
    for games in results:
        game = {}
        game["id"] = games.split(':')[0].split(' ')[1]
        game_possible = True
        
        for picks in games.split(':')[1].split(';'):
            for pick in picks.split(','):
                pick = pick.strip()
                if int(pick.split(' ')[0]) > limits[pick.split(' ')[1]]:
                    game_possible = False
        if game_possible:
            possible_games.append(int(game["id"]))
    print(sum(possible_games))

part1()
