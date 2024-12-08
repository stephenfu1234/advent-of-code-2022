import time

def read_file(filename):
    return open(filename).read()

def solve(filename):
    start_time = int(time.time() * 1000)

    raw_input = read_file(filename)

    sections = raw_input.split('\n\n')
    stacks = parse_setup(sections[0].split('\n'))
    moves = list(map(parse_move, sections[1:][0].split('\n')))

    for move in moves:
        stacks = move_crates(stacks, move[0], move[1], move[2])
    
    # get the last letter from each of the stacks and concatenate
    print(''.join([stack[-1] for stack in stacks]))

    end_time = int(time.time() * 1000)
    print(f'Time taken for {filename} (ms): {end_time - start_time}')

def parse_setup(setup):
    # reverse the setup so that its easier to parse top to bottom instead of bottom to top
    setup.reverse()
    
    # get first line of the setup, split to get the numbers and then take the last
    total_stacks = int(setup[0].split()[-1])
    
    stacks = []
    for stack_num in range(1, total_stacks+1):
        stack = []
        # for each row (exclude the first row which are the stack numbers)
        for row in setup[1:]:            
            # the index is calculated by the stack number-1 * the gap and then add one for the opening bracket
            # e.g [Z] [M] [P]
            idx = ((stack_num - 1) * 4) + 1
            if row[idx] != ' ':
                stack.append(row[idx])
        stacks.append(stack)
    
    return stacks
     

def parse_move(move):
    tokens = move.split(' ')
    return [int(tokens[1]), int(tokens[3]), int(tokens[5])]

def move_crates(stacks, num_crates, from_stack, to_stack):    
    # remove 1 from stack number for zero based indexing    
    # take num_crates off the from stack
    crates = stacks[from_stack-1][-num_crates:]    

    # no need to reverse the crates for part 2 as the crates are moved in order

    stacks[from_stack-1] = stacks[from_stack-1][:-num_crates]
    
    # add removed crates to the to stack    
    stacks[to_stack-1].extend(crates)

    return stacks

solve('test.txt')
solve('input.txt')