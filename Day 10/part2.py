import time

def read_file(filename):
    return open(filename).read()

def solve(filename):
    start_time = int(time.time() * 1000)

    register = 1
    cycle = 1
    records = []
    cycle_interval = 20
    cycle_record = []

    for line in read_file(filename).splitlines():
        # print('cycle', cycle, 'register', register)
        cycle_record.append((cycle, register))
        if line == 'noop':
            cycle += 1

            if cycle % cycle_interval == 0:
                # print('noop appending', register)
                records.append(register)
        else:
            _, val = line.split()
            # will we pass a cycle threshold on either the first or second cycle
            # if so, save current register in records before we increment
            if (cycle+1) % cycle_interval == 0:
                # print('addx appending', register, val)
                records.append(register)

            # cycle += 1
            # print('cycle', cycle+1, 'register', register)
            cycle_record.append((cycle+1, register))

            if (cycle+2) % cycle_interval == 0:
                # print('addx appending', register, val)
                records.append(register + int(val)) 

            
            cycle += 2
            register += int(val)

    # print(cycle)
    # print(register)
    # print(cycle_record)

    start = 0
    end = len(cycle_record)
    step = 40
    counter = 0
    for i in range(start, end, step):
        x = i
        records = cycle_record[x:x+step]
        # print(records)
        line = ''
        for cycle_idx, val in records:
            char_idx = cycle_idx - (counter * 40)
            # print((cycle_idx%40), cycle_idx)
            # print(char_idx, val)
            if val - 1 <= (char_idx-1) and val + 1 >= (char_idx-1):
                line += '#'
            else:
                line += '.'
        counter += 1
        print(line)
    
    end_time = int(time.time() * 1000)
    print(f'Time taken for {filename} (ms): {end_time - start_time}')

    # for cycle, val in cycle_record:
    #     print(cycle, val)

# solve('test.txt')
# solve('test2.txt')
solve('input.txt')