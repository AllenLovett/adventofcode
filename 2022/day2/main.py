# Rock, Paper, Scissors
## Opponent move:
# A (1) Rock | B (2) Paper | C (3) Scissors
## Your Move:
# X (1) Rock | Y (2) Paper | Z (3) Scissors
##Scoring:
# Win - 6 | Draw - 3 | Lose - 0 points

game_moves = ["AYXZ","BZYX", "CXZY"] # Moves - <opponent><winning move><drawing move><losing move>
strategy_moves = ["Z", "Y", "X"] # Win, Draw, Lose
move_score = {"X": 1, "Y": 2, "Z": 3}
score = []

games = open("inputs.txt", "r").read().split('\n')
def part1(): # Given the inputs, calculate the scoring of each round based on the opening move and our required response
    for round in range(len(games)):
        for move in game_moves:
            if move.startswith(games[round].split()[0]): # Find the right set of moves based on opening move
                if games[round][2] == move[1]: # If our move matches the "winning" move, we win
                    round_score = move_score[games[round][2]] + 6
                    score.append(round_score)
                elif games[round][2] == move[2]: # If our move matches the "Drawing" move, we draw
                    round_score = move_score[games[round][2]] + 3
                    score.append(round_score)
                else: # Otherwise we lose
                    round_score = move_score[games[round][2]]
                    score.append(round_score)
# part1() # Result should be: 13924
def part2(): # Given the inputs, calculate the scoring when we play to the directed outcomes
    for round in range(len(games)):
        for move in game_moves:
            if move.startswith(games[round].split()[0]): # Find the right set of moves based on opening move
                if strategy_moves.index(games[round].split()[1]) == 0: # We need to win
                    # In order to win we need to find the winning play against the opening move
                    round_score = move_score[move[1]] + 6
                    score.append(round_score)
                elif strategy_moves.index(games[round].split()[1]) == 1: # We need to draw
                    round_score = move_score[move[2]] + 3
                    score.append(round_score)
                elif strategy_moves.index(games[round].split()[1]) == 2: # We need to lose
                    round_score = move_score[move[3]]
                    score.append(round_score)

part2() # Result should be 13448
print(f"Total strategy score: {sum(score)}")
