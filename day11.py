def get_shortest_distance(galaxy1, galaxy2, distance_inc):
    start_r = -1
    total_r = 0

    if galaxy1[0] < galaxy2[0]:
        start_r = galaxy1[0]
    else:
        start_r = galaxy2[0]
    r_diff = abs(galaxy1[0] - galaxy2[0])
    total_r = r_diff
    for r in range(r_diff):
        if start_r + r in rows_doubled:
            total_r += distance_inc - 1

    start_c = -1
    total_c = 0
    if galaxy1[1] < galaxy2[1]:
        start_c = galaxy1[1]
    else:
        start_c = galaxy2[1]
    c_diff = abs(galaxy1[1] - galaxy2[1])
    total_c = c_diff
    for r in range(c_diff):
        if start_c + r in cols_doubled:
            total_c += distance_inc - 1
    
    return total_r + total_c

def solve1(input_data):
    G = {}
    galaxies = []
    global max_r
    global max_c

    max_r = len(input_data.split("\n"))
    for r, line in enumerate(input_data.split("\n")):
        max_c = len(line)
        for c, v in enumerate(line):
            G[(r,c)] = v
            if v == "#":
                galaxies.append((r,c))

    global rows_doubled 
    rows_doubled = set()
    for r in range(max_r):
        r_galaxy_found = False
        for c in range(max_c):
            if G[(r,c)] == "#":
                r_galaxy_found = True
        if not r_galaxy_found:
            rows_doubled.add(r)

    global cols_doubled 
    cols_doubled = set()
    for c in range(max_c):
        c_galaxy_found = False
        for r in range(max_r):
            if G[(r,c)] == "#":
                c_galaxy_found = True
        if not c_galaxy_found:
            cols_doubled.add(c)

    t = 0
    while len(galaxies) > 0:
        cur_galaxy = galaxies.pop()
        for other_galaxy in galaxies:
            shortest = get_shortest_distance(cur_galaxy, other_galaxy, 2)
            t += shortest

    return t


def solve2(input_data):
    G = {}
    galaxies = []
    global max_r
    global max_c

    max_r = len(input_data.split("\n"))
    for r, line in enumerate(input_data.split("\n")):
        max_c = len(line)
        for c, v in enumerate(line):
            G[(r,c)] = v
            if v == "#":
                galaxies.append((r,c))

    global rows_doubled 
    rows_doubled = set()
    for r in range(max_r):
        r_galaxy_found = False
        for c in range(max_c):
            if G[(r,c)] == "#":
                r_galaxy_found = True
        if not r_galaxy_found:
            rows_doubled.add(r)

    global cols_doubled 
    cols_doubled = set()
    for c in range(max_c):
        c_galaxy_found = False
        for r in range(max_r):
            if G[(r,c)] == "#":
                c_galaxy_found = True
        if not c_galaxy_found:
            cols_doubled.add(c)

    t = 0
    while len(galaxies) > 0:
        cur_galaxy = galaxies.pop()
        for other_galaxy in galaxies:
            shortest = get_shortest_distance(cur_galaxy, other_galaxy, 1000000)
            t += shortest

    return t


if __name__ == "__main__":
    print("Program Start")
    use_sample = False

    #use_sample = True

    if use_sample:
        input_data_file = open("sample11.txt", "r")
    else:
        input_data_file = open("input11.txt", "r")

    input_data_text = input_data_file.read()
    input_data_file.close()

    ans1 = solve1(input_data_text)
    ans2 = solve2(input_data_text)

    print(f"Part 1: {ans1}")
    print(f"Part 2: {ans2}")