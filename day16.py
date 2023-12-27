from queue import deque

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
DIRECTIONS = [NORTH,EAST,SOUTH,WEST]

D_NORTH = (-1,0)
D_EAST = (0,1)
D_SOUTH = (1,0)
D_WEST = (0,-1)

INCREMENT = {
    NORTH: D_NORTH,
    EAST: D_EAST,
    SOUTH: D_SOUTH,
    WEST: D_WEST,
}
MAPPINGS = {
    "\\": {
        NORTH: [WEST],
        EAST: [SOUTH],
        SOUTH: [EAST],
        WEST: [NORTH],
        },
    "/": {
        NORTH: [EAST],
        EAST: [NORTH],
        SOUTH: [WEST],
        WEST: [SOUTH],
        },
    "-": {
        NORTH: [EAST, WEST],
        EAST: [EAST],
        SOUTH: [EAST, WEST],
        WEST: [WEST],
        },
    "|": {
        NORTH: [NORTH],
        EAST: [NORTH, SOUTH],
        SOUTH: [SOUTH],
        WEST: [NORTH, SOUTH],
        },
    ".": {
        NORTH: [NORTH],
        EAST: [EAST],
        SOUTH: [SOUTH],
        WEST: [WEST],
        },
}

def print_energised(G, energised):
    for r in range(r_max):
        for c in range(c_max):
            if (r,c) in energised:
                print("#", end="")
            else:
                print(G[(r,c)], end="")
        print()
    print()

def run_beams(G, start, cur_d):
    energised = set()
    old_length = 0
    count_at_old = 0
    change = True
    beams = deque()
    beams.append((start,cur_d))
    seen = set()
    while len(beams) > 0:
        cur, cur_d = beams.popleft()
        if cur[0] < 0 or cur[0] == r_max or cur[1] < 0 or cur[1] == c_max:
            continue
        if (cur, cur_d) in seen:
            continue
        energised.add(cur)
        seen.add((cur, cur_d))
        new_ds = MAPPINGS[G[cur]][cur_d]
        for new_d in new_ds:
            new_cur = (cur[0] + INCREMENT[new_d][0], cur[1] + INCREMENT[new_d][1])
            beams.append((new_cur,new_d))
        if len(energised) == old_length:
            count_at_old += 1
            # print(count_at_old)
            if count_at_old >= 20:
                break
        else:
            count_at_old = 0
        # print_energised(G, energised)
        old_length = len(energised)
    return len(energised)

def solve1(input_data):
    data = input_data.split("\n")
    global r_max
    global c_max
    r_max = len(data)
    c_max = len(data[0])
    G = {}
    for r in range(r_max):
        for c in range(c_max):
            G[(r,c)] = data[r][c]
    
    start = (0,0)
    cur_d = EAST
    
    return run_beams(G, start, cur_d)

def solve2(input_data):
    data = input_data.split("\n")
    global r_max
    global c_max
    r_max = len(data)
    c_max = len(data[0])
    G = {}
    for r in range(r_max):
        for c in range(c_max):
            G[(r,c)] = data[r][c]
    
    start = (0,0)
    cur_d = EAST
    max_energy = 0
    startings = []
    for r in range(r_max):
        startings.append(((r,0),EAST))
        startings.append(((r,c_max-1),WEST))
    for c in range(c_max):
        startings.append(((0,c),SOUTH))
        startings.append(((r_max-1,c),NORTH))
    
    count = 0
    total_needed = r_max*2 + c_max*2
    for start, start_d in startings:
        energy_amount = run_beams(G, start, start_d)
        max_energy = max(max_energy, energy_amount)
        count += 1
        print(count, "out of", total_needed)
        

    return max_energy

if __name__ == "__main__":
    print("Program Start")
    use_sample = False

    #use_sample = True

    if use_sample:
        input_data_file = open("sample16.txt", "r")
    else:
        input_data_file = open("input16.txt", "r")

    input_data_text = input_data_file.read()

    input_data_file.close()

    ans1 = solve1(input_data_text)
    ans2 = solve2(input_data_text)

    print(f"Part 1: {ans1}")
    print(f"Part 2: {ans2}")