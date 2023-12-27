import sys
import heapq

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
    ways_left = []
    # total, pos, came from, amount in a dir
    heapq.heappush(ways_left, (0, start, SOUTH, 0))
    ans = sys.maxsize
    best_at = {}
    while len(ways_left) > 0:
        t, cur, prev_d, straight_amt = heapq.heappop(ways_left)  

        if (cur,prev_d,straight_amt) not in best_at:
            best_at[(cur,prev_d,straight_amt)] = t
        else:
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

            if new_cur == end:
                if new_t < ans:
                    ans = new_t
                    print(ans)
                continue

            heapq.heappush(ways_left, (new_t, new_cur, d, new_straight_amt))

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
    ways_left = []
    # total, pos, came from, amount in a dir
    heapq.heappush(ways_left, (0, start, SOUTH, 0))
    ans = sys.maxsize
    best_at = {}
    while len(ways_left) > 0:
        t, cur, prev_d, straight_amt = heapq.heappop(ways_left)  

        if (cur,prev_d,straight_amt) not in best_at:
            best_at[(cur,prev_d,straight_amt)] = t
        else:
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

            if new_cur == end:
                if new_t < ans:
                    ans = new_t
                    print(ans)
                continue

            heapq.heappush(ways_left, (new_t, new_cur, d, new_straight_amt))

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

    ans1 = solve1(input_data_text)
    ans2 = solve2(input_data_text)

    print(f"Part 1: {ans1}")
    print(f"Part 2: {ans2}")


    
