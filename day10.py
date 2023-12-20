import sys
NORTH = (-1,0)
EAST = (0,1)
SOUTH = (1,0)
WEST = (0,-1)
DIRS = [NORTH, EAST, SOUTH, WEST]
PIPE_TO_COORDS = {
    "|":((NORTH),(SOUTH)),
    "-":((EAST),(WEST)),
    "L":((NORTH),(EAST)),
    "J":((NORTH),(WEST)),
    "7":((SOUTH),(WEST)),
    "F":((SOUTH),(EAST))
}
POSSIBLE_S_PIPES = ["|", "-", "L", "J", "7", "F"]

def rotate_east(direction):
    if direction == NORTH:
        return EAST
    if direction == EAST:
        return SOUTH
    if direction == SOUTH:
        return WEST
    if direction == WEST:
        return NORTH
    assert False

def rotate_west(direction):
    if direction == NORTH:
        return WEST
    if direction == EAST:
        return NORTH
    if direction == SOUTH:
        return EAST
    if direction == WEST:
        return SOUTH
    assert False

def get_neighbour_coords(coords, pipe_type):
    neighbours = []
    neighbour_1_r = coords[0] + PIPE_TO_COORDS[pipe_type][0][0]
    neighbour_1_c = coords[1] + PIPE_TO_COORDS[pipe_type][0][1]
    neighbour_2_r = coords[0] + PIPE_TO_COORDS[pipe_type][1][0]
    neighbour_2_c = coords[1] + PIPE_TO_COORDS[pipe_type][1][1]
    if coord_is_valid((neighbour_1_r, neighbour_1_c)):  
        neighbours.append((neighbour_1_r, neighbour_1_c))
    if coord_is_valid((neighbour_2_r, neighbour_2_c)):  
        neighbours.append((neighbour_2_r, neighbour_2_c))

    return neighbours

def coord_is_valid(coord):
    if (coord[0] < max_r and coord[1] < max_c and
        coord[0] >= 0 and coord[1] >= 0):
        return True
    return False

def get_inside_area(max_path, max_visited, rotate_function):
    counted = set()
    for coord, facing in max_path:
        walk_dir = rotate_function(facing)
        cur_coord = coord
        first_run = True
        reached_edge = False
        while cur_coord not in max_visited or first_run:
            first_run = False
            cur_coord = (cur_coord[0] + walk_dir[0], cur_coord[1] + walk_dir[1])

            if not coord_is_valid(cur_coord):
                reached_edge = True
                break

            if cur_coord not in max_visited and cur_coord not in counted:
                counted.add(cur_coord)
                    
        if reached_edge:
            counted = set()
            break
    return counted

def solve1(input_data):
    G = {}
    start_pos = (-1,-1)
    global max_r
    global max_c 
    max_r = len(input_data.split("\n"))
    for r, line in enumerate(input_data.split("\n")):
        max_c = len(line)
        for c, v in enumerate(line):
            G[(r,c)] = v
            if v == "S":
                start_pos = (r,c)
    
    end = (-1,-1)
    max_loop_length = 0
    for possible_S in POSSIBLE_S_PIPES:
        visited = set()

        neighbours = get_neighbour_coords(start_pos, possible_S)
        if len(neighbours) < 2:
            continue

        if end == (-1,-1):
            end = neighbours[1]
        
        previous = start_pos
        current = neighbours[0]

        while current != start_pos:
            visited.add(current)
            old_current = current

            if G[current] == ".":
                break
            neighbours = get_neighbour_coords(current, G[current])
            if len(neighbours) < 2:
                break

            if previous == neighbours[0]:
                current = neighbours[1]
            elif previous == neighbours[1]:
                current = neighbours[0]
            else:
                break
            previous = old_current

        if current == start_pos:
            max_loop_length = max(max_loop_length, len(visited) + 1)

    return max_loop_length/2

def solve2(input_data):
    G = {}
    start_pos = (-1,-1)
    global max_r
    global max_c 
    max_r = len(input_data.split("\n"))
    
    for r, line in enumerate(input_data.split("\n")):
        max_c = len(line)
        for c, v in enumerate(line):
            G[(r,c)] = v
            if v == "S":
                start_pos = (r,c)
    
    
    end = (-1,-1)
    max_loop_length = 0
    max_visited = set()
    max_path = []
    
    for possible_S in POSSIBLE_S_PIPES:
        visited = set()
        path = []
        neighbours = get_neighbour_coords(start_pos, possible_S)
        if len(neighbours) < 2:
            continue

        if end == (-1,-1):
            end = neighbours[1]
        
        previous = start_pos
        current = neighbours[0]

        facing = (current[0] - previous[0], current[1] - previous[1])
        old_facing = facing
        path.append((start_pos, facing))
        path.append((current, facing))

        while current != start_pos:
            visited.add(current)
            old_current = current

            if G[current] == ".":
                break
            neighbours = get_neighbour_coords(current, G[current])
            if len(neighbours) < 2:
                break

            if previous == neighbours[0]:
                current = neighbours[1]
            elif previous == neighbours[1]:
                current = neighbours[0]
            else:
                break
            previous = old_current
            facing = (current[0] - previous[0], current[1] - previous[1])
            if old_facing != facing:
                path.append((old_current, facing))
            assert facing in DIRS
            path.append((current, facing))

        if current == start_pos:
            max_loop_length = max(max_loop_length, len(visited) + 1)
            max_visited = visited.copy()
            max_path = path.copy()

    max_visited.add(start_pos)

    area_to_right = get_inside_area(max_path, max_visited, rotate_east)
    area_to_left = get_inside_area(max_path, max_visited, rotate_west)

    return max(len(area_to_right), len(area_to_left))

if __name__ == "__main__":
    print("Program Start")
    use_sample = False

    #use_sample = True

    if use_sample:
        input_data_file = open("sample10.txt", "r")
    else:
        input_data_file = open("input10.txt", "r")

    input_data_text = input_data_file.read()
    input_data_file.close()

    ans1 = solve1(input_data_text)
    ans2 = solve2(input_data_text)

    print(f"Part 1: {ans1}")
    print(f"Part 2: {ans2}")