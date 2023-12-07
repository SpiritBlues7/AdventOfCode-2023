def check_pair(val):
    for c in val:
        if val.count(c) == 2:
            return True
    return False

def check_two_pair(val):
    pair_count = 0
    for c in val:
        if val.count(c) == 2:
            pair_count += 1
    return pair_count == 4

def check_trip(val):
    for c in val:
        if val.count(c) == 3:
            return True
    return False

def check_quad(val):
    for c in val:
        if val.count(c) == 4:
            return True
    return False

def check_quint(val):
    for c in val:
        if val.count(c) == 5:
            return True
    return False

def check_full(val):
    return check_trip(val) and check_pair(val) 

def convert_to_nums(val, joker_is_zero=False):
    vals = []
    for c in val:
        if c.isdigit():
            vals.append(int(c))
        if c == "T":
            vals.append(10)
        if c == "J":
            if joker_is_zero:
                vals.append(0)
            else:
                vals.append(11)
        if c == "Q":
            vals.append(12)
        if c == "K":
            vals.append(13)
        if c == "A":
            vals.append(14)
    return vals

def solve1(input_data):
    data = input_data.split("\n")
    values = []
    for line in data:
        hand, bid = line.split(" ")
        hand_nums = convert_to_nums(hand)
        val = 0
        if check_quint(hand_nums):
            val = 6
        elif check_quad(hand_nums):
            val = 5
        elif check_full(hand_nums):
            val = 4
        elif check_trip(hand_nums):
            val = 3
        elif check_two_pair(hand_nums):
            val = 2
        elif check_pair(hand_nums):
            val = 1
        else:
            val = 0
        values.append((val, hand_nums, int(bid)))

    values.sort()
    c = 1
    t = 0
    for _, _, bid in values:
        t += bid * c
        c += 1
        
    return str(t)


def solve2(input_data):
    data = input_data.split("\n")
    values = []
    for line in data:
        hand, bid = line.split(" ")
        hand_nums = convert_to_nums(hand, True)
        joker_count = hand_nums.count(0)
        val = 0
        if check_quint(hand_nums):
            val = 6
        elif check_quad(hand_nums):
            val = 5
            if joker_count == 1:
                val = 6
            if joker_count == 4:
                val = 6
        elif check_full(hand_nums):
            val = 4
            if joker_count > 1:
                val = 6
        elif check_trip(hand_nums):
            val = 3
            if joker_count == 1:
                val = 5
            if joker_count == 3:
                val = 5
        elif check_two_pair(hand_nums):
            val = 2
            if joker_count == 1:
                val = 4
            elif joker_count == 2:
                val = 5
        elif check_pair(hand_nums):
            val = 1
            if joker_count == 1:
                val = 3
            elif joker_count == 2:
                val = 3
        else:
            if joker_count == 1:
               val = 1
        values.append((val, hand_nums, int(bid)))

    values.sort()
    c = 1
    t = 0
    for _, _, bid in values:
        t += bid * c
        c += 1
        
    return str(t)

if __name__ == "__main__":
    print("Program Start")
    use_sample = False

    #use_sample = True

    if use_sample:
        input_data_file = open("sample07.txt", "r")
    else:
        input_data_file = open("input07.txt", "r")

    input_data_text = input_data_file.read()
    input_data_file.close()

    ans1 = solve1(input_data_text)
    ans2 = solve2(input_data_text)

    print(f"Part 1: {ans1}")
    print(f"Part 2: {ans2}")