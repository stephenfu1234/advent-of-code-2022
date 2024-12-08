import time

def read_file(filename):
    return open(filename).read()

def solve(filename):
    start_time = int(time.time() * 1000)

    raw_input = read_file(filename)

    # read into a list of lists, split by new line and then by space
    data = [i.split(' ') for i in raw_input.split('\n') if i]

    # calculate the scores for each round
    round_scores = list(map(get_score, data))

    # output total score of all rounds
    print(sum(round_scores))

    end_time = int(time.time() * 1000)
    print(f'Time taken for {filename} (ms): {end_time - start_time}')

def get_score(round_moves):
    # now X, Y, Z represent the desired result so we need to derive the choice
    scores = { 'AX': 3 + 0, # rock and loss = 3 for scissors + 0 for loss
               'BX': 1 + 0, # paper and loss = 1 for rock + 0 for loss
               'CX': 2 + 0, # scissors and loss = 2 for paper + 0 for loss
               'AY': 1 + 3, # rock and draw = 1 for rock + 3 for draw
               'BY': 2 + 3, # paper and draw = 2 for paper + 3 for draw
               'CY': 3 + 3, # scissors and draw = 3 for scissors + 3 for draw
               'AZ': 2 + 6, # rock and win = 2 for paper + 6 for win
               'BZ': 3 + 6, # paper and win = 3 for scissors + 6 for win
               'CZ': 1 + 6, # scissors and win = 1 for rock + 6 for win
              }
    
    # get the score for opponent move vs your move
    return scores[round_moves[0] + round_moves[1]]

solve('test.txt')
solve('input.txt')