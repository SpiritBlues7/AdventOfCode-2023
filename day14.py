def move_north(G:dict, inc):
    any_change = False
    first = True
    change = True
    while change or first:
        first = False
        change = False
        new_G = {}

        for r in range(max_r):
            for c in range(max_c):
                v = G[(r,c)]
                if (r,c) not in new_G:
                    new_G[(r,c)] = v
                if (r + inc[0] < 0 
                    or c + inc[1] < 0
                    or r + inc[0] == max_r
                    or c + inc[1] == max_c):
                    continue
                if v != "O":
                    continue
                if G[(r + inc[0],c + inc[1])] != ".": 
                    continue
                change = True
                any_change = True
                new_G[(r + inc[0],c + inc[1])] = "O"
                new_G[(r,c)] = "."
        G = new_G
    return new_G, any_change

def print_grid(G:dict):
    for r in range(max_r):
        for c in range(max_c):
            print(G[(r,c)], end="")
        print()

def count_weight(G:dict):
    t = 0
    for r in range(max_r):
        for c in range(max_c):
            if G[(r,c)] == "O":
                t += max_r - r
    return t

def solve1(input_data):
    data = input_data.split("\n")
    global max_r
    global max_c
    max_r = len(data)
    max_c = len(data[0])
    G = {}
    for r in range(max_r):
        for c in range(max_c):
            G[(r,c)] = data[r][c]
    

    G, change = move_north(G, (-1,0))

    # print_grid(G)

    return count_weight(G)


def solve2(input_data):
    data = input_data.split("\n")
    global max_r
    global max_c
    max_r = len(data)
    max_c = len(data[0])
    G = {}
    G_o = set()
    for r in range(max_r):
        for c in range(max_c):
            G[(r,c)] = data[r][c]
            if data[r][c] == "O":
                G_o.add((r,c))
    
    change = False
    first = True
    count = 0
    
    differences = {}
    counts_left = 1000000000
    interval_found = False
    while counts_left > 0:
        new_G_o = set()

        first = False
        G, change_n = move_north(G, (-1,0))
        G, change_w = move_north(G, (0,-1))
        G, change_s = move_north(G, (1,0))
        G, change_e = move_north(G, (0,1))

        for r in range(max_r):
            for c in range(max_c):
                if G[(r,c)] == "O":
                    new_G_o.add((r,c))
        cur_diff = list(G_o.difference(new_G_o))
        cur_diff.sort()
        cur_diff = tuple(cur_diff)
        print(count, cur_diff)
        if cur_diff not in differences:
            differences[cur_diff] = count
        else:
            if not interval_found:
                interval_found = True
                interval = count - differences[cur_diff]
                amount_to_mult = counts_left//interval
                counts_left = counts_left - (amount_to_mult * interval)
        G_o = new_G_o
        change = change_n and change_w and change_s and change_e
        count += 1
        counts_left -= 1
        
    # print_grid(G)

    return count_weight(G)

if __name__ == "__main__":
    print("Program Start")
    use_sample = False

    #use_sample = True

    if use_sample:
        input_data_file = open("sample14.txt", "r")
    else:
        input_data_file = open("input14.txt", "r")

    input_data_text = input_data_file.read()

    input_data_file.close()

    ans1 = solve1(input_data_text)
    ans2 = solve2(input_data_text)

    print(f"Part 1: {ans1}")
    print(f"Part 2: {ans2}")