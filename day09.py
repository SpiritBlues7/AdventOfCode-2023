import sys

def solve1(input_data):
    history = input_data.split("\n")
    t = 0
    for h in history:
        h = [int(v) for v in h.split(" ")]

        current_h = h.copy()
        last_values = []
        while True:
            if all(x == 0 for x in current_h):
                break
            last_values.append(current_h[-1])
            
            new_h = []
            prev_v = sys.maxsize
            for v in current_h:
                if prev_v == sys.maxsize:
                    prev_v = v
                    continue
                new_h.append(v - prev_v)
                prev_v = v
            current_h = new_h.copy()
        t += sum(last_values)


    return t

def solve2(input_data):
    history = input_data.split("\n")
    t = 0
    for h in history:
        h = [int(v) for v in h.split(" ")]

        current_h = h.copy()
        first_values = []
        while True:
            if all(x == 0 for x in current_h):
                break
            first_values.append(current_h[0])
            
            new_h = []
            prev_v = sys.maxsize
            for v in current_h:
                if prev_v == sys.maxsize:
                    prev_v = v
                    continue
                new_h.append(v - prev_v)
                prev_v = v
            current_h = new_h.copy()

        history_t = 0
        for a in first_values[::-1]:
            history_t = a - history_t
        t += history_t


    return t

if __name__ == "__main__":
    print("Program Start")
    use_sample = False

    #use_sample = True

    if use_sample:
        input_data_file = open("sample09.txt", "r")
    else:
        input_data_file = open("input09.txt", "r")

    input_data_text = input_data_file.read()
    input_data_file.close()

    ans1 = solve1(input_data_text)
    ans2 = solve2(input_data_text)

    print(f"Part 1: {ans1}")
    print(f"Part 2: {ans2}")