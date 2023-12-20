from math import lcm

def solve1(input_data):
    instructs, data = input_data.split("\n\n")
    instructs = instructs.replace('R', '1').replace('L', '0')
    instructs = [int(a) for a in instructs]
    # (L,R)
    routes = {}
    for l in data.split("\n"):
        k, vals = l.split(" = ")
        vl, vr = vals.replace(")", "").replace("(", "").split(", ")
        routes[k] = (vl, vr)
    
    cur = "AAA"
    i = 0
    c = 0
    while cur != "ZZZ":
        c += 1
        cur = routes[cur][instructs[i]]
        i += 1
        if i == len(instructs):
            i = 0
        
    return c

def solve2(input_data):
    instructs, data = input_data.split("\n\n")
    instructs = instructs.replace('R', '1').replace('L', '0')
    instructs = [int(a) for a in instructs]
    # (L,R)
    routes = {}
    starting_nodes = []
    for l in data.split("\n"):
        k, vals = l.split(" = ")
        if k.endswith("A"):
            starting_nodes.append(k)
        vl, vr = vals.replace(")", "").replace("(", "").split(", ")
        routes[k] = (vl, vr)
    
    current_nodes = starting_nodes.copy()
    i = 0
    c = 0
    increments = []
    while True:
        
        if i == len(instructs):
            i = 0

        next_nodes = []
        for j, v in enumerate(current_nodes):
            if current_nodes[j].endswith("Z"):
                increments.append(c)
            else:
                next_nodes.append(routes[current_nodes[j]][instructs[i]])
        current_nodes = next_nodes.copy()
        c += 1     
        if len(increments) == len(starting_nodes):
            break
        i += 1
    t = lcm(*increments)

    return t

if __name__ == "__main__":
    print("Program Start")
    use_sample = False

    #use_sample = True

    if use_sample:
        input_data_file = open("sample08.txt", "r")
    else:
        input_data_file = open("input08.txt", "r")

    input_data_text = input_data_file.read()
    input_data_file.close()

    ans1 = solve1(input_data_text)
    ans2 = solve2(input_data_text)

    print(f"Part 1: {ans1}")
    print(f"Part 2: {ans2}")