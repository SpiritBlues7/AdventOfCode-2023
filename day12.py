import multiprocessing
from collections import deque 

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

def solve_2_lines(inputs):
    input_data = inputs[0]
    j = inputs[1]
    data = input_data.split("\n")

    line = data[j]
    springs, required_raw = line.split(" ")
    required = [int(v) for v in required_raw.split(",")]

    springs = springs + "?" + springs + "?" + springs + "?" + springs + "?" + springs
    required = required + required + required + required + required

    combos = deque()
    combos.append((0,0,0))
    st = 0

    while len(combos) > 0:
        (current_amount, spring_index, required_index) = combos.pop()

        if spring_index == len(springs):
            if required_index == len(required) and current_amount == 0:
                st += 1
            elif required_index == len(required) - 1 and current_amount == required[required_index]:
                st += 1
            continue

        if required_index == len(required) and current_amount == 0 and springs[spring_index] != "#":
            combos.append((current_amount, spring_index + 1, required_index))
            continue

        if springs[spring_index] == "?":
            # this is a new spring
            if current_amount + 1 <= required[required_index]:
                combos.append((current_amount + 1, spring_index + 1, required_index))
            # was coming from a empty and this is an empty
            if current_amount == 0:
                combos.append((current_amount, spring_index + 1, required_index))
            # was coming from a spring and this is an empty 
            if current_amount == required[required_index]:
                combos.append((0, spring_index + 1, required_index + 1))
        
        elif springs[spring_index] == "#":
            if current_amount + 1 <= required[required_index]:
                combos.append((current_amount + 1, spring_index + 1, required_index))
        else:
            # was coming from a empty
            if current_amount == 0:
                combos.append((current_amount, spring_index + 1, required_index))
            # was coming from a spring
            if current_amount == required[required_index]:
                combos.append((0, spring_index + 1, required_index + 1))
        # print(combos)

    print(j, st)
    return st

def solve2(input_data):
    global input_value
    input_value = input_data
    data = input_data.split("\n")
    # solve_2_lines((input_data, 1))
    cpu_count = multiprocessing.cpu_count()
    input_params_list = [(input_data, i) for i in range(len(data))]
    t = 0

    pool = multiprocessing.Pool(cpu_count)
    results = pool.map(solve_2_lines, input_params_list)
    
    pool.close()
    pool.join()
    print(sum(results))



    # for i in range(len(data)):
    #     threads.append(Process(target=solve_2_lines, args=(input_data,i,ans)))
    
    # for thread in threads:
    #     thread.start()

    # for thread in threads:
    #     thread.join()

    # a = ans.get()
    # t += a
    # while a > 0:
    #     a = ans.get()
    #     print("TOTAL:", t)
    #     t += a
    



    # for line in data:
    #     springs, required_raw = line.split(" ")
    #     required = [int(v) for v in required_raw.split(",")]

    #     springs = springs + "?" + springs + "?" + springs + "?" + springs + "?" + springs
    #     required = required + required + required + required + required
    #     springs_initial = springs.count("#")
    #     required_count = sum(required)
    #     max_allowed = required_count - springs_initial
    #     spring_length = len(springs)
    #     combos = [([0],False)]
    #     st = 0

    #     for i in range(spring_length):
    #         new_combos = []

    #         # print(i)
    #         while len(combos) > 0:
    #             (cur_combo, on_run) = combos.pop()
    #             springs_current = sum(cur_combo)
    #             springs_upcoming = springs[i:].count("#")
    #             springs_total_so_far = springs_current + springs_upcoming
    #             # print(springs_current)
    #             if springs[i] == "?":
    #                 if on_run:
    #                     temp_combo_add = cur_combo.copy()
    #                     temp_combo_add[-1] = temp_combo_add[-1]+1
    #                     if (springs_total_so_far < required_count 
    #                         and check_if_satisfies_list(temp_combo_add, required, True)):
    #                         new_combos.append((temp_combo_add, True))
    #                     temp_combo_same = cur_combo.copy()
    #                     new_combos.append((temp_combo_same, False))
                        
    #                 else:
    #                     temp_combo_add2 = cur_combo.copy()
    #                     temp_combo_add2.append(1)
    #                     if (springs_total_so_far < required_count 
    #                         and check_if_satisfies_list(temp_combo_add2, required, True)):
    #                         new_combos.append((temp_combo_add2, True))
    #                     temp_combo_same2 = cur_combo.copy()
    #                     new_combos.append((temp_combo_same2, False))
    #             elif springs[i] == "#":
    #                 temp_combo_add7 = cur_combo.copy()
    #                 if on_run:
    #                     temp_combo_add7[-1] = temp_combo_add7[-1]+1
    #                     if (springs_total_so_far <= required_count
    #                         and check_if_satisfies_list(temp_combo_add7, required, True)):
    #                         new_combos.append((temp_combo_add7, True))

    #                 else:
    #                     temp_combo_add7.append(1)
    #                     if check_if_satisfies_list(temp_combo_add7, required, True):
    #                         new_combos.append((temp_combo_add7, True))
    #             else:
    #                 temp_combo_same4 = cur_combo.copy()
    #                 new_combos.append((temp_combo_same4, False))
    #             # print(new_combos)
    #         combos = new_combos

    #     # print(len(combos))
    #     for combo, run in combos:
    #         if check_if_satisfies_list(combo, required):
    #             st += 1
                
    #             # print(combo, required)
    #     print(st)     
    #     t += st

    # return t


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