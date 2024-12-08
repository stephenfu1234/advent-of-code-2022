import time

def read_file(filename):
    return open(filename).read()

def solve(filename):
    start_time = int(time.time() * 1000)

    tail_visited_locations = [(0,0)]
    current_head_location = (0,0)
    current_tail_location = (0,0)

    for line in read_file(filename).splitlines():
        dir, dist = line.split()
        
        # for each of the head steps
        for i in range(0, int(dist)):
            # convert direction into coordinate steps
            x_step, y_step = get_step_dir(dir)

            # move head
            current_head_location = (current_head_location[0] + x_step, current_head_location[1] + y_step)

            # move tail
            # if head and tail in same column or row then the head can follow in same direction
            if current_head_location[0] == current_tail_location[0] or current_head_location[1] == current_tail_location[1]:
                # only move if not adjacent
                if is_adjacent(current_head_location, current_tail_location) == False:
                    # if head and tail not touching each other then move the tail towards the head
                    current_tail_location = (current_tail_location[0] + x_step, current_tail_location[1] + y_step)

            # if in different column or row then the head should take a diagonal step towards the head if there is a gap between the two
            else:
                # only move if not adjacent
                if is_adjacent(current_head_location, current_tail_location) == False:
                    # if head and tail not touching each other then move the tail diagonally towards the head
                    # print(current_head_location, current_tail_location)

                    x_gap = current_head_location[0] - current_tail_location[0]
                    y_gap = current_head_location[1] - current_tail_location[1]

                    tail_x_step = x_gap if abs(x_gap) == 1 else x_gap/2
                    tail_y_step = y_gap if abs(y_gap) == 1 else y_gap/2

                    current_tail_location = (current_tail_location[0] + tail_x_step,
                                             current_tail_location[1] + tail_y_step)                

            # add location
            tail_visited_locations.append(current_tail_location)
            # print(current_tail_location)

    print(tail_visited_locations)
    unique_tail_locations = set(tail_visited_locations)
    print(len(unique_tail_locations))
    
    end_time = int(time.time() * 1000)
    print(f'Time taken for {filename} (ms): {end_time - start_time}')

def get_step_dir(dir):
    if dir == 'U':
        return 0, -1
    
    if dir == 'D':
        return 0, 1
    
    if dir == 'L':
        return -1, 0
    
    if dir == 'R':
        return 1, 0

def is_adjacent(current_head_location, current_tail_location):
    if abs(current_head_location[0] - current_tail_location[0]) <= 1 and abs(current_head_location[1] - current_tail_location[1]) <= 1:
        return True
    return False

solve('test.txt')
# solve('input.txt')