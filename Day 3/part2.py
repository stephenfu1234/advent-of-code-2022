import time

def read_file(filename):
    return open(filename).read()

def solve(filename):
    start_time = int(time.time() * 1000)

    raw_input = read_file(filename)

    # read into a list of lists, split by new line and then each letter
    data = [i for i in raw_input.split('\n') if i]
    
    # group each rucksack into groups of 3
    rucksack_groups = [data[i:i + 3] for i in range(0, len(data), 3)]

    # find common items in each rucksack and get the priority
    common_items_priority = list(map(get_common_items, rucksack_groups))

    # get sum of all priorities
    print(sum(common_items_priority))

    end_time = int(time.time() * 1000)
    print(f'Time taken for {filename} (ms): {end_time - start_time}')

def get_common_items(rucksack_group):
    # use set theory to get common elements
    common_items = set(rucksack_group[0]) & set(rucksack_group[1]) & set(rucksack_group[2])

    # get priority of each common item and return total
    return sum(list(map(get_priority, common_items)))

def get_priority(item):
    # a=1 through to z=26
    # A=27 through to Z=52
    if(item.islower()):
        return ord(item) - 96
    return ord(item) - 38

solve('test.txt')
solve('input.txt')