import time
import numpy as np

def read_file(filename):
    return open(filename).read()

def solve(filename):
    start_time = int(time.time() * 1000)

    raw_input = read_file(filename)

    # read into numpy 2d matrix, rows as \n, cols as individual numbers
    data = np.array([list(i) for i in raw_input.split('\n')]).astype(int)
    
    # print(data)
    
    # for each internal tree (number) check direction wise if any value is equal or larger
    start_row_index = 1
    end_row_index = data.shape[0] - 2
    start_col_index = 1
    end_col_index = data.shape[1] - 2

    scenic_scores = []
    total_visible_trees = (data.shape[0] * 2) + (data.shape[1] * 2) - 4
    for row_idx in range(start_row_index, end_row_index+1):
        for col_idx in range(start_col_index, end_col_index+1):
            # print(data[row_idx][col_idx])
            # for each interior tree, check N, E, S, W if all tress are smaller
            
            current_tree = data[row_idx, col_idx]
            # north - get first tree going north that is same or larger than current tree, set default to total trees incase there is no equal/taller tree            
            # for looking north we need to reverse the data
            scenic_score_north = next((x+1 for x, val in enumerate(np.flip(data[:row_idx, col_idx])) if val >= current_tree), len(data[:row_idx, col_idx])) 
            
            # east
            scenic_score_east = next((x+1 for x, val in enumerate(data[row_idx, col_idx+1:]) if val >= current_tree), len(data[row_idx, col_idx+1:])) 
            
            # south
            scenic_score_south = next((x+1 for x, val in enumerate(data[row_idx+1:, col_idx]) if val >= current_tree), len(data[row_idx+1:, col_idx])) 

            # west
            # for looking west we need to reverse the data
            scenic_score_west = next((x+1 for x, val in enumerate(np.flip(data[row_idx, :col_idx])) if val >= current_tree), len(data[row_idx, :col_idx])) 
            scenic_scores.append(scenic_score_north * scenic_score_east * scenic_score_south * scenic_score_west)
    
    print(max(scenic_scores))

    end_time = int(time.time() * 1000)
    print(f'Time taken for {filename} (ms): {end_time - start_time}')

solve('test.txt')
solve('input.txt')