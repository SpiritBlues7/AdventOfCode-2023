import multiprocessing

def check_if_satisfies_text(combo, required):
    springs = combo.split(".")
    i = 0
    for spring in springs:
        if spring == "":
            continue
        if i >= len(required):
            return False
        if len(spring) != required[i]:
            return False
        i += 1
    if i != len(required):
        return False
    return True

def solve1(input_data):
    data = input_data.split("\n")
    t = 0
    for line in data:
        springs, required_raw = line.split(" ")
        required = [int(v) for v in required_raw.split(",")]
        spring_length = len(springs)
        combos = [""]
        st = 0

        for i in range(spring_length):
            new_combos = []
            while len(combos) > 0:
                cur_combo = combos.pop()
                if springs[i] == "?":
                    new_combos.append(cur_combo + "#")
                    new_combos.append(cur_combo + ".")
                else:
                    new_combos.append(cur_combo + springs[i])
            combos = new_combos

        for combo in combos:
            if check_if_satisfies_text(combo, required):
                st += 1
                
        t += st

    return t

def solve_single_line(inputs):
    input_data = inputs[0]
    j = inputs[1]
    data = input_data.split("\n")

    line = data[j]
    springs, required_raw = line.split(" ")
    required = [int(v) for v in required_raw.split(",")]

    springs = springs + "?" + springs + "?" + springs + "?" + springs + "?" + springs
    required = required + required + required + required + required

    # Dictionary format (string_index,required_index,current_run) = max_combos
    combos_at_index = {}

    # Initialise end values
    for n in range(max(required)+1):
        for k in range(len(required)+1):
            combos_at_index[(len(springs),k,n)] = 0
    combos_at_index[(len(springs),len(required),0)] = 1
    combos_at_index[(len(springs),len(required)-1,required[-1])] = 1

    # Loop through keys backwards and populate, i is spring index, k is required index, n is current run
    for i in range(len(springs)-1,-1,-1):
        for k in range(len(required),-1,-1):
            # if we reached the end of the required numbers then only deal with n = 0
            if k >= len(required):
                st = 0
                if springs[i] == "?" or springs[i] == ".":
                    combos_at_index[(i,k,0)] = combos_at_index[(i+1,k,0)]
                else:
                    combos_at_index[(i,k,0)] = 0
                continue
            for n in range(required[k]+1):
                assert (i,k,n) not in combos_at_index

                st = 0
                if i + 1 <= len(springs):
                    # found a new spring
                    if (springs[i] == "?" or springs[i] == "#") and k < len(required):
                        if n + 1 <= required[k]:
                            st += combos_at_index[(i+1,k,n+1)]
                    # found an empty square
                    if springs[i] == "?" or springs[i] == ".":
                        if n == 0:
                            st += combos_at_index[(i+1,k,n)]
                        elif n == required[k]:
                            if k + 1 <= len(required):
                                st += combos_at_index[(i+1,k+1,0)]
                combos_at_index[(i,k,n)] = st

    return combos_at_index[(0,0,0)]

def solve2(input_data):
    global input_value
    input_value = input_data
    data = input_data.split("\n")

    cpu_count = multiprocessing.cpu_count()
    input_params_list = [(input_data, i) for i in range(len(data))]
    t = 0

    pool = multiprocessing.Pool(cpu_count)
    results = pool.map(solve_single_line, input_params_list)
    
    pool.close()
    pool.join()
    return sum(results)


if __name__ == "__main__":
    print("Program Start")
    use_sample = False

    #use_sample = True

    if use_sample:
        input_data_file = open("sample12.txt", "r")
    else:
        input_data_file = open("input12.txt", "r")

    input_data_text = input_data_file.read()

    input_data_file.close()

    ans1 = solve1(input_data_text)
    ans2 = solve2(input_data_text)

    print(f"Part 1: {ans1}")
    print(f"Part 2: {ans2}")