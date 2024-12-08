import time

def read_file(filename):
    return open(filename).read()

def solve(filename):
    start_time = int(time.time() * 1000)

    raw_input = read_file(filename)

    # use range for sliding window through the string
    window_size = 4
    for i in range(len(raw_input)):
        # for each window given by raw_input[i:i+window_size]
        # get the next 4 characters, then turn into a set and if the length is window_size then it won't contain duplicates
        if len(set(raw_input[i:i+window_size])) == window_size:
            # end position will be start range plus window_size
            print(i + window_size)
            break
    
    end_time = int(time.time() * 1000)
    print(f'Time taken for {filename} (ms): {end_time - start_time}')

solve('test.txt')
solve('input.txt')