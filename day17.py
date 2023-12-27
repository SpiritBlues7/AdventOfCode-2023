import sys

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

class Node:
    def __init__(self, current, prev_d, straight_amt, total, path):
        self.current = current
        self.prev_d = prev_d
        self.straight_amt = straight_amt
        self.total = total
        self.path = path

def print_path(G, path):
    for r in range(r_max):
        for c in range(c_max):
            if (r,c) in path:
                print("#", end="")
            else:
                print(G[(r,c)], end="")
        print()
    print()

def solve1(input_data):
    data = input_data.split("\n")
    global r_max
    global c_max
    r_max = len(data)
    c_max = len(data[0])
    G = {}
    for r in range(r_max):
        for c in range(c_max):
            G[(r,c)] = int(data[r][c])
    
    start = (0,0)
    end = (r_max - 1, c_max - 1)
    # pos, came from, val
    start_node = Node(start, SOUTH, 0, 0, [])
    ways_left = [start_node]
    ans = sys.maxsize
    min_node = None
    best_at = {}
    while len(ways_left) > 0:
        cur_node = ways_left.pop()
        cur = cur_node.current
        prev_d = cur_node.prev_d
        straight_amt = cur_node.straight_amt
        t = cur_node.total
        # path = cur_node.path

        
        if straight_amt == 1:
            if (cur,prev_d) not in best_at:
                best_at[(cur,prev_d)] = t
            else:
                if best_at[(cur,prev_d)] <= t:
                    continue
                else:
                    best_at[(cur,prev_d)] = t
        else:
            if (cur,prev_d) in best_at and best_at[(cur,prev_d)] <= t:
                continue
                
        for d in DIRECTIONS:
            new_cur = (cur[0] + INCREMENT[d][0], cur[1] + INCREMENT[d][1])
            new_straight_amt = straight_amt
            if new_cur[0] < 0 or new_cur[0] == r_max or new_cur[1] < 0 or new_cur[1] == c_max:
                continue
            new_t = t + G[new_cur]
            if d == DIRECTIONS[(prev_d + 2)%4]:
                continue
            if new_t > ans:
                continue
            if d == prev_d:
                new_straight_amt += 1
            else:
                new_straight_amt = 1
            if new_straight_amt > 3:
                continue
            #new_node = Node(new_cur, d, new_straight_amt, new_t, path.copy())
            new_node = Node(new_cur, d, new_straight_amt, new_t, [])
            new_node.path.append(new_cur)
            if new_cur == end:
                if new_t < ans:
                    ans = new_t
                    min_node = new_node
                    print(ans)
                continue

            ways_left.append(new_node)
            # print(ways_left)
    # print(min_node.path)
    # print_path(G, min_node.path)
    return ans

def solve2(input_data):
    data = input_data.split("\n")
    global r_max
    global c_max
    r_max = len(data)
    c_max = len(data[0])
    G = {}
    for r in range(r_max):
        for c in range(c_max):
            G[(r,c)] = int(data[r][c])
    
    start = (0,0)
    end = (r_max - 1, c_max - 1)
    # pos, came from, val
    start_node = Node(start, SOUTH, 0, 0, [])
    ways_left = [start_node]
    ans = 2000
    min_node = None
    best_at = {}
    while len(ways_left) > 0:
        cur_node = ways_left.pop()
        cur = cur_node.current
        prev_d = cur_node.prev_d
        straight_amt = cur_node.straight_amt
        t = cur_node.total
        # path = cur_node.path
        
        if straight_amt == 4:
            if (cur,prev_d) not in best_at:
                best_at[(cur,prev_d)] = t
            else:
                if best_at[(cur,prev_d)] <= t:
                    continue
                else:
                    best_at[(cur,prev_d)] = t
        else:
            if (cur,prev_d) in best_at and best_at[(cur,prev_d)] <= t:
                continue
                
        for d in DIRECTIONS:
            new_straight_amt = straight_amt
            move_amount = 1
            if d == prev_d:
                new_straight_amt += 1
            else:
                move_amount = 4
                new_straight_amt = 4
            if new_straight_amt > 10:
                continue
            new_cur = (cur[0] + (INCREMENT[d][0]*move_amount), 
                cur[1] + (INCREMENT[d][1]*move_amount))
            
            if new_cur[0] < 0 or new_cur[0] >= r_max or new_cur[1] < 0 or new_cur[1] >= c_max:
                continue
            if move_amount == 1:
                new_t = t + G[new_cur]
            else:
                temp_pos = cur
                new_t = t
                for k in range(move_amount):
                    temp_pos = (temp_pos[0] + (INCREMENT[d][0]), temp_pos[1] + (INCREMENT[d][1]))
                    new_t += G[temp_pos]
            if d == DIRECTIONS[(prev_d + 2)%4]:
                continue
            if new_t > ans:
                continue

            # new_node = Node(new_cur, d, new_straight_amt, new_t, path.copy())
            new_node = Node(new_cur, d, new_straight_amt, new_t, [])
            new_node.path.append(new_cur)
            if new_cur == end:
                if new_t < ans:
                    ans = new_t
                    min_node = new_node
                    print(ans)
                continue

            ways_left.append(new_node)
            # print(ways_left)
    # print(min_node.path)
    # print_path(G, min_node.path)
    return ans

if __name__ == "__main__":
    print("Program Start")
    use_sample = False

    #use_sample = True

    if use_sample:
        input_data_file = open("sample17.txt", "r")
    else:
        input_data_file = open("input17.txt", "r")

    input_data_text = input_data_file.read()

    input_data_file.close()

    # ans1 = solve1(input_data_text)
    ans2 = solve2(input_data_text)

    # print(f"Part 1: {ans1}")
    print(f"Part 2: {ans2}")


    
