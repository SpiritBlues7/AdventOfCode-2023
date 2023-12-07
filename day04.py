def solve1(input_data):
    input_data = input_data.replace("  "," ")
    data = input_data.split("\n")
    t = 0
    for line in data:
        winning_nums, my_nums = line.split(": ")[1].split(" | ")
        winning_nums = winning_nums.split(" ")
        my_nums = my_nums.split(" ")
        st = 0
        for num in winning_nums:
            if num in my_nums:
                st *= 2
                st = max(st, 1)
        t += st

    return t

def solve2(input_data):
    input_data = input_data.replace("  "," ")
    data = input_data.split("\n")

    cards = []
    for line in data:
        winning_nums, my_nums = line.split(": ")[1].split(" | ")
        winning_nums = winning_nums.split(" ")
        my_nums = my_nums.split(" ")
        
        st = 0
        for num in winning_nums:
            if num in my_nums:
                st += 1
        cards.append(st)

    t = 0
    card_ids = [(i,1) for i in range(len(cards))]
    while len(card_ids) != 0:
        sorted(card_ids)

        card_num, amount_of_card_num = card_ids.pop(0)
        card_val = cards[card_num]
        t+=amount_of_card_num
        for i in range(card_val):
            next_card_num, next_amount_of_card_num = card_ids[i]
            card_ids[i] = (next_card_num, next_amount_of_card_num+amount_of_card_num)

    return t

if __name__ == "__main__":
    print("Program Start")
    use_sample = False

    #use_sample = True

    if use_sample:
        input_data_file = open("sample04.txt", "r")
    else:
        input_data_file = open("input04.txt", "r")

    input_data_text = input_data_file.read()
    input_data_file.close()

    ans1 = solve1(input_data_text)
    ans2 = solve2(input_data_text)

    print(f"Part 1: {ans1}")
    print(f"Part 2: {ans2}")