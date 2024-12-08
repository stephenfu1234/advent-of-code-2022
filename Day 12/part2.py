import time
from heapq import heapify, heappop, heappush

def read_file(filename):
    return open(filename).read()

def solve(filename):
    start_time = int(time.time() * 1000)

    # for line in read_file(filename).splitlines():
    #     dir, dist = line.split()
    raw_input = read_file(filename)

    # read into a list of lists, split by new line and then by space using list comprension
    data = [list(i) for i in raw_input.split('\n')] #if i == to apply filtering

    # this is a shortest path puzzle, we could brute force all the options but that could be useless in part 2
    # so lets try Dikstra's algorithm as this will help find the shortest route between two points in a network
    # Dijkstra's algorithm finds the shortest path from one vertex to all other vertices.
    # It does so by repeatedly selecting the nearest unvisited vertex and calculating the distance to all the unvisited neighbouring vertices.
    
    # for part 1 this is a effectively a directed weighted graph where all weights are 1
    # the restriction on only being able to move to a step that is max 1 height taller determines the network i.e. nodes (vertices) and its edges

    # to represent the graph we can have a dictionary where each key is a given node (location)
    # the values for a key are another dict where the key is the neighbour node and value is the distance
    maze_with_border = add_border_to_maze(data)

    #print(network_graph.graph)
    #print('\n')
        
    # for part 2 we need also know the elevation for a given coordinate as we need to find the cloest elevation 'a' to the end 'E'
    # so lets just modify our location key to include the elevation letter and then search for the shortest distance from E

    # Find all the valid starting locations (key that contains 'a')
    # then for each find the one with with smallest steps
    valid_start_locations = get_valid_starting_locations(maze_with_border)
    # print(valid_start_locations)

    target_location = get_location_of_value('E', maze_with_border)
    possible_distances = []

    # setup a new graph
    network_graph = setup_graph(maze_with_border)
    
    # for each possible starting location
    for valid_start_location in valid_start_locations:
        # calculate the shortest distance from the start location
        distances = network_graph.shortest_distances(valid_start_location)

        # then store the distance to the target location 'E'
        possible_distances.append(distances[target_location])
        # print('start location', valid_start_location, 'target location', target_location, 'distance', distances[target_location])

    print(min(possible_distances))

    end_time = int(time.time() * 1000)
    print(f'Time taken for {filename} (ms): {end_time - start_time}')

def add_border_to_maze(maze):
    # add left and right border
    for row in maze:
        row.insert(0, '#')
        row.append('#')

    # add top border
    maze.insert(0, len(maze[0]) * ['#']) 
    # add bottom border
    maze.append(maze[0])
    return maze

def setup_graph(maze):
    graph = Graph()
    
    for row in range(0, len(maze)):
        for col in range(0, len(maze[0])):
            if maze[row][col] == '#':
                # not a valid location so skip
                continue;
              
            # check heighbours and if we can access then create graph edge for node
            # coordinates for N S E W
            directions = [[row-1, col], [row+1, col], [row, col+1], [row, col-1]]
            # use tuple unpacking            
            for neighbour_row, neighbour_col in directions:
                # we can move to the neighbour if its lower elevation or greater elevation of max 1
                current_elevation = get_elevation(maze[row][col])
                neighbour_elevation = get_elevation(maze[neighbour_row][neighbour_col])
                if current_elevation + 1 >= neighbour_elevation:
                    current_location_key = get_location_key(row, col)
                    neighbour_location_key = get_location_key(neighbour_row, neighbour_col)

                    # we can move from current location to neighbour location at a cost of 1 step
                    graph.add_edge(current_location_key, neighbour_location_key, 1)
            # print('\n')
    return graph

def get_location_key(row, col):
    return str(row) + '_' + str(col)

def get_location_of_value(value, maze):
    for row in range(0, len(maze)):
        for col in range(0, len(maze[0])):
            if maze[row][col] == value:
                return get_location_key(row, col)

def get_valid_starting_locations(maze):
    locations = []
    for row in range(0, len(maze)):
        for col in range(0, len(maze[0])):
            if maze[row][col] == 'a' or maze[row][col] == 'S':
                locations.append(get_location_key(row, col))

    return locations

def get_elevation(code):
    # starting elevation is a
    if code == 'S':
        return ord('a')
    
    if code == 'E':
        # same elevation as z
        return ord('z')
    
    if code == '#':
        # if its the border then make the border elevation too high so we cant move there
        return ord('~')
    
    return ord(code)

class Graph:
    def __init__(self, graph: dict = {}):
        self.graph = graph

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:  # Check if the node is already added
            self.graph[node1] = {}  # If not, create the node
        self.graph[node1][node2] = weight  # Else, add a connection to its neighbour

    def shortest_distances(self, source: str):
        # Initialize the values of all nodes with infinity
        distances = {node: float("inf") for node in self.graph}
        distances[source] = 0  # Set the source value to 0

        # Initialize a priority queue
        pq = [(0, source)]
        heapify(pq)

        # Create a set to hold visited nodes
        visited = set()

        while pq:  # While the priority queue isn't empty
            current_distance, current_node = heappop(pq)
            if current_node in visited:
                continue 

            visited.add(current_node)

            if current_node not in self.graph:
                continue
            
            for neighbour, weight in self.graph[current_node].items():
                if neighbour not in distances:
                    continue

                # Calculate the distance from current_node to the neighbour
                tentative_distance = current_distance + weight
                if tentative_distance < distances[neighbour]:
                    distances[neighbour] = tentative_distance
                    heappush(pq, (tentative_distance, neighbour))

        return distances
    
solve('test.txt')
solve('input.txt')