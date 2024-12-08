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

    total_visible_trees = (data.shape[0] * 2) + (data.shape[1] * 2) - 4
    for row_idx in range(start_row_index, end_row_index+1):
        for col_idx in range(start_col_index, end_col_index+1):
            # print(data[row_idx][col_idx])
            # for each interior tree, check N, E, S, W if all tress are smaller
            
            current_tree = data[row_idx, col_idx]
            # print(row_idx, col_idx, current_tree)
            # north
            # print('checking north', data[:row_idx, col_idx]) 
            if max(data[:row_idx, col_idx]) < current_tree:
                # print('north is clear')
                total_visible_trees += 1
                continue

            # east
            # print('checking east', data[row_idx, col_idx+1:]) 
            if max(data[row_idx, col_idx+1:]) < current_tree:
                # print('east is clear')
                total_visible_trees += 1
                continue

            # south
            # print('checking south', data[row_idx+1:, col_idx]) 
            if max(data[row_idx+1:, col_idx]) < current_tree:
                # print('south is clear')
                total_visible_trees += 1
                continue

            # west
            # print('checking west', data[row_idx, :col_idx]) 
            if max(data[row_idx, :col_idx]) < current_tree:
                # print('west is clear')
                total_visible_trees += 1
                continue
    
    print(total_visible_trees)

    end_time = int(time.time() * 1000)
    print(f'Time taken for {filename} (ms): {end_time - start_time}')

solve('test.txt')
solve('input.txt')