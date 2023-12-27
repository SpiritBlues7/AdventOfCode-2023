from queue import deque
import sys

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
DIRECTIONS = [NORTH,EAST,SOUTH,WEST]

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

SWAP_DIR_TO_ID = {
    "U": UP,
    "R": RIGHT,
    "D": DOWN,
    "L": LEFT,
}
SWAP_ID_TO_DIR = {
    UP: "U",
    RIGHT: "R",
    DOWN: "D",
    LEFT: "L",
}
D_NORTH = (-1,0)
D_EAST = (0,1)
D_SOUTH = (1,0)
D_WEST = (0,-1)

INCREMENT_UDLR = {
    UP: D_NORTH,
    RIGHT: D_EAST,
    DOWN: D_SOUTH,
    LEFT: D_WEST,
}

INCREMENT = {
    NORTH: D_NORTH,
    EAST: D_EAST,
    SOUTH: D_SOUTH,
    WEST: D_WEST,
}

def get_boundaries(G):
    global max_r
    global max_c
    global min_r
    global min_c
    max_r = 0
    max_c = 0
    min_r = 0
    min_c = 0
    for r,c in G:
        max_r = max(max_r, r+1)
        max_c = max(max_c, c+1)
        min_r = min(min_r, r-1)
        min_c = min(min_c, c-1)

def print_grid(G):
    for r in range(max_r):
        for c in range(max_c):
            if (r,c) in G:
                print("#", end="")
            else:
                print(".", end="")
        print()

def flood_fill(G):
    start = (min_r, min_c)
    current_list = deque()
    current_list.append(start)
    visited = set()
    
    while len(current_list) > 0:
        current = current_list.popleft()
        if current in visited:
            continue
        else:
            visited.add(current)
             
        for d in DIRECTIONS:
            new_cur = current  
            new_cur = (new_cur[0] + INCREMENT[d][0], new_cur[1] + INCREMENT[d][1])
            if new_cur in G:
                continue
            if (min_r)<=new_cur[0]<=(max_r) and (min_c)<=new_cur[1]<=(max_c):
                current_list.append(new_cur)
    
    total_r_area = (max_r) - (min_r) + 1
    total_c_area = (max_c) - (min_c) + 1
    total_area = abs(total_r_area) * abs(total_c_area)
    total_filled = total_area - len(visited)
    return total_filled 

def get_area(G,R,C):
    t = 0
    total_needed = len(G)
    i = 0
    for (r,c), ds in G.items():
        if i % 100000 == 0:
            print(i, "area calc out of", total_needed)

        for d in ds:
            walking_dir = (d + 1) % 4

            closest_edge = sys.maxsize
            if walking_dir == UP:
                for r2 in C[c]:
                    if r2 == r:
                        continue
                    if r2 < r:
                        closest_edge = min(closest_edge, r-r2-1)
            if walking_dir == DOWN:
                for r2 in C[c]:
                    if r2 == r:
                        continue
                    if r2 > r:
                        closest_edge = min(closest_edge, r2-r-1)
            if walking_dir == LEFT:
                for c2 in R[r]:
                    if c2 == c:
                        continue
                    if c2 < c:
                        closest_edge = min(closest_edge, c-c2-1)
            if walking_dir == RIGHT:
                for c2 in R[r]:
                    if c2 == c:
                        continue
                    if c2 > c:
                        closest_edge = min(closest_edge, c2-c-1)

            assert closest_edge != sys.maxsize
            t += closest_edge
            i += 1
    return t/4
            

def solve1(input_data):
    parts = input_data.split("\n")
    G = set()
    G.add((0,0))
    current = (0,0)
    for part in parts:
        d, v, color = part.split(" ")
        d = SWAP_DIR_TO_ID[d]
        v = int(v)
        
        for i in range(v):
            current = (current[0] + INCREMENT_UDLR[d][0], current[1] + INCREMENT_UDLR[d][1])
            G.add(current)
    
    get_boundaries(G)
    # print_grid(G)
    total_filled = flood_fill(G)
    return total_filled

def solve2(input_data):
    parts = input_data.split("\n")
    G = {}
    C = {}
    R = {}
    current = (0,0)
    perimeter = 0
    old_d = None
    parts_total = len(parts)
    count = 0
    for part in parts:
        print(count, "parts out of", parts_total)
        data = part.split(" ")[2][2:-1]
        d = int(data[-1],16)
        v = int(data[:-1],16)

        if old_d is not None and old_d != d:
            G[current].append(d)


        perimeter += v
        for i in range(v):
            current = (current[0] + INCREMENT_UDLR[d][0], current[1] + INCREMENT_UDLR[d][1])
            assert current not in G
            G[current] = [d]

            if current[0] not in R:
                R[current[0]] = [current[1]]
            else:
                R[current[0]].append(current[1])
            if current[1] not in C:
                C[current[1]] = [current[0]]
            else:
                C[current[1]].append(current[0])

        old_d = d
        count += 1

    get_boundaries(G)
    # print_grid(G)
    total_filled = get_area(G,R,C)
    print(perimeter)
    return total_filled + perimeter

if __name__ == "__main__":
    print("Program Start")
    use_sample = False

    #use_sample = True

    if use_sample:
        input_data_file = open("sample18.txt", "r")
    else:
        input_data_file = open("input18.txt", "r")

    input_data_text = input_data_file.read()

    input_data_file.close()

    ans1 = solve1(input_data_text)
    ans2 = solve2(input_data_text)

    print(f"Part 1: {ans1}")
    print(f"Part 2: {ans2}")


    
