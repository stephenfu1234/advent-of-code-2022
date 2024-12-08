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
    scores = { 'AX': 1 + 3, # rock vs rock = 1 for rock + 3 for draw
               'BX': 1 + 0, # paper vs rock = 1 for rock + 0 for loss
               'CX': 1 + 6, # scissors vs rock = 1 for rock + 6 for win
               'AY': 2 + 6, # rock vs paper = 2 for paper + 6 for win
               'BY': 2 + 3, # paper vs paper = 2 for paper + 3 for draw
               'CY': 2 + 0, # scissors vs paper = 2 for paper + 0 for loss
               'AZ': 3 + 0, # rock vs scissors = 3 for scissors + 0 for loss
               'BZ': 3 + 6, # paper vs scissors = 3 for scissors + 6 for win
               'CZ': 3 + 3, # scissors vs scissors = 3 for scissors + 3 for draw
              }
    
    # get the score for opponent move vs your move
    return scores[round_moves[0] + round_moves[1]]

solve('test.txt')
solve('input.txt')