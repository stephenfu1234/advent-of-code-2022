import time

def read_file(filename):
    return open(filename).read()

def solve(filename):
    start_time = int(time.time() * 1000)

    # for line in read_file(filename).splitlines():
    #     dir, dist = line.split()
    raw_input = read_file(filename)

    total_monkeys = raw_input.count('Monkey')

    # each monkey will be represented as value in each of the lists
    # [] for _ in range(total_monkeys)
    items = []
    operation = []
    test = []
    true_operation = []
    false_operation = []
    inspections = [0] * total_monkeys

    op = {'+': lambda x, y: x + y,
          '*': lambda x, y: x * y}
    
    # parse data
    # read into a list of lists, split by doublew new line then by new line using list comprension
    data = [i.split('\n') for i in raw_input.split('\n\n')]
    
    for monkey in range(0, total_monkeys):        
        # get the list of items, convert to int and add list to items.  items[0] = monkey 0, items[1] = monkey 1
        items.append(list(map(int, data[monkey][1].split(': ')[1].split(', '))))
        # operation.append(data[monkey][2].split(' = ')[1].split(' '))

        # try convert the last item to a digit unless it is 'old' string
        ops = data[monkey][2].split(' = ')[1].split(' ')
        if ops[-1].isdigit():
            ops[-1] = int(ops[-1])
        # we can remove the first old string e.g. old * 19
        operation.append(ops[1:])        
        
        test.append(int(data[monkey][3].split('by ')[1]))
        true_operation.append(int(data[monkey][4].split('monkey ')[1]))
        false_operation.append(int(data[monkey][5].split('monkey ')[1]))
        
    # iterate each round
    for round in range(0, 20):
        # for each monkey
        for monkey in range(0, total_monkeys):            
            # for each of their items
            for item in items[monkey]:                
                current_worry = item
                # apply operation
                if isinstance(operation[monkey][1], int):
                    # operation[0] is +,-,*,/ use the lambda table to apply
                    current_worry = op[operation[monkey][0]](current_worry, operation[monkey][1])
                else:
                    current_worry = op[operation[monkey][0]](current_worry, current_worry)
                    
                # apply floor (round down) division by 3
                current_worry = current_worry // 3

                # check if worry level is divisible by test
                if current_worry % test[monkey] == 0:
                    # then add to items of the monkey based on true 
                    items[true_operation[monkey]].append(current_worry)
                else:
                    # if false then pass to different monkey
                    items[false_operation[monkey]].append(current_worry)
                
                # count how many times the monkey has performed an inspection
                inspections[monkey] += 1
            
            # now that all the items have been processed for the current monkey, reset their list of items
            items[monkey] = []              

    print(inspections)
    
    # multiple top 2 largest values
    inspections.sort(reverse=True)
    print(inspections[0] * inspections[1])
    
    end_time = int(time.time() * 1000)
    print(f'Time taken for {filename} (ms): {end_time - start_time}')

solve('test.txt')
solve('input.txt')