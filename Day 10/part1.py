import time

def read_file(filename):
    return open(filename).read()

def solve(filename):
    start_time = int(time.time() * 1000)

    register = 1
    cycle = 1
    records = []
    cycle_interval = 20

    for line in read_file(filename).splitlines():
        # print('cycle', cycle, 'register', register)
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

            if (cycle+2) % cycle_interval == 0:
                # print('addx appending', register, val)
                records.append(register + int(val)) 

            cycle += 2
            register += int(val)

    print(cycle)
    print(register)
    print(records[0::2])
    strengths = []
    for idx, val in enumerate(records[0::2]):
        cycle_idx = ((idx+1)*(cycle_interval*2))-20
        strengths.append(cycle_idx * val)
    print(sum(strengths))
    end_time = int(time.time() * 1000)
    print(f'Time taken for {filename} (ms): {end_time - start_time}')

# solve('test.txt')
# solve('test2.txt')
solve('input.txt')