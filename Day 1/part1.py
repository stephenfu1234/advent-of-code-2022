import time

def read_file(filename):
    return open(filename).read()

def solve(filename):
    start_time = int(time.time() * 1000)

    raw_input = read_file(filename)

    # read into a list of lists, split by double new line and cast as int  
    # each sub list is an elf's own inventory
    data = [list(map(int,i.split('\n'))) for i in raw_input.split('\n\n') if i]
    
    # sum each list to get the total of each elf
    sum_data = list(map(lambda x: sum(x), data))

    # then find the max carried
    print(max(sum_data))

    end_time = int(time.time() * 1000)
    print(f'Time taken for {filename} (ms): {end_time - start_time}')

solve('test.txt')
solve('input.txt')