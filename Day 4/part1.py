import time

def read_file(filename):
    return open(filename).read()

def solve(filename):
    start_time = int(time.time() * 1000)

    raw_input = read_file(filename)

    # read into a list of lists, split by new line and then by comma and then by - using list comprension
    data = [[j.split('-') for j in i.split(',')] for i in raw_input.split('\n')]

    # calculate pairs which have enclosed range
    total = list(map(is_enclosed, data))
    # print(total)

    # sum the list to calculate total enclosed pairs
    print(sum(total))
    
    end_time = int(time.time() * 1000)
    print(f'Time taken for {filename} (ms): {end_time - start_time}')

def is_enclosed(pair):
    # e.g. pair = [['2', '8'], ['3', '7']]
    # 4-26,27-70
    # if 2 <= 3 and 8 >= 7 means fully enclosed

    # get individual items and convert to int
    item_1 = list(map(int, pair[0]))
    item_2 = list(map(int, pair[1]))

    if item_1[0] <= item_2[0] and item_1[1] >= item_2[1]:
        return 1

    if item_2[0] <= item_1[0] and item_2[1] >= item_1[1]:
        return 1
    
    return 0

solve('test.txt')
solve('input.txt')