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

def check_if_satisfies_list(combo, required, partial=False):
    i = 0
    for j, spring in enumerate(combo):
        if i >= len(required):
            return False
        if spring == 0:
            continue
        if partial and spring > required[i]:
            return False
        elif (not partial or j < len(combo) - 1) and spring != required[i]:
            return False
        i += 1
    if not partial and i != len(required):
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
                # print(combo, required)
                
        t += st

    return t


def solve2(input_data):
    data = input_data.split("\n")
    t = 0
    for line in data:
        springs, required_raw = line.split(" ")
        required = [int(v) for v in required_raw.split(",")]

        springs = springs + "?" + springs + "?" + springs + "?" + springs + "?" + springs
        required = required + required + required + required + required
        springs_initial = springs.count("#")
        required_count = sum(required)
        max_allowed = required_count - springs_initial
        spring_length = len(springs)
        combos = [([0],False)]
        st = 0

        for i in range(spring_length):
            new_combos = []

            # print(i)
            while len(combos) > 0:
                (cur_combo, on_run) = combos.pop()
                springs_current = sum(cur_combo)
                springs_upcoming = springs[i:].count("#")
                springs_total_so_far = springs_current + springs_upcoming
                # print(springs_current)
                if springs[i] == "?":
                    if on_run:
                        temp_combo_add = cur_combo.copy()
                        temp_combo_add[-1] = temp_combo_add[-1]+1
                        if (springs_total_so_far < required_count 
                            and check_if_satisfies_list(temp_combo_add, required, True)):
                            new_combos.append((temp_combo_add, True))
                        temp_combo_same = cur_combo.copy()
                        new_combos.append((temp_combo_same, False))
                        
                    else:
                        temp_combo_add2 = cur_combo.copy()
                        temp_combo_add2.append(1)
                        if (springs_total_so_far < required_count 
                            and check_if_satisfies_list(temp_combo_add2, required, True)):
                            new_combos.append((temp_combo_add2, True))
                        temp_combo_same2 = cur_combo.copy()
                        new_combos.append((temp_combo_same2, False))
                elif springs[i] == "#":
                    temp_combo_add7 = cur_combo.copy()
                    if on_run:
                        temp_combo_add7[-1] = temp_combo_add7[-1]+1
                        if (springs_total_so_far <= required_count
                            and check_if_satisfies_list(temp_combo_add7, required, True)):
                            new_combos.append((temp_combo_add7, True))

                    else:
                        temp_combo_add7.append(1)
                        if check_if_satisfies_list(temp_combo_add7, required, True):
                            new_combos.append((temp_combo_add7, True))
                else:
                    temp_combo_same4 = cur_combo.copy()
                    new_combos.append((temp_combo_same4, False))
                # print(new_combos)
            combos = new_combos

        # print(len(combos))
        for combo, run in combos:
            if check_if_satisfies_list(combo, required):
                st += 1
                
                # print(combo, required)
        print(st)     
        t += st

    return t


if __name__ == "__main__":
    print("Program Start")
    use_sample = False

    use_sample = True

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