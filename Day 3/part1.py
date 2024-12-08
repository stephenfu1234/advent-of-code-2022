import time

def read_file(filename):
    return open(filename).read()

def solve(filename):
    start_time = int(time.time() * 1000)

    raw_input = read_file(filename)

    # read into a list of lists, split by new line and then each letter
    data = [i for i in raw_input.split('\n') if i]
    
    # convert each rucksack into a list of compartments
    rucksacks = list(map(get_compartments, data))
    
    # find common items in each rucksack and get the priority
    common_items_priority = list(map(get_common_items, rucksacks))

    # get sum of all priorities
    print(sum(common_items_priority))

    end_time = int(time.time() * 1000)
    print(f'Time taken for {filename} (ms): {end_time - start_time}')

def get_compartments(rucksack):
    compartment_1 = rucksack[len(rucksack)//2:]
    compartment_2 = rucksack[:len(rucksack)//2]
    return [compartment_1, compartment_2]

def get_common_items(rucksack):
    # use set theory to get common elements
    common_items = set(rucksack[0]) & set(rucksack[1])

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