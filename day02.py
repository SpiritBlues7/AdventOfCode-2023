def solve1(input_data):
    games = input_data.split("\n")
    total = 0
    for game in games:
        game_info, other = game.split(":")
        _, game_id = game_info.split(" ")
        draws = other.split(";")
        success = True
        amounts = {
            "blue": 0,
            "red": 0,
            "green": 0
        }
        for draw in draws:
            items = draw.split(",")
            for item in items:
                item_num, item_col  = item.strip().split(" ")
                if amounts[item_col] < int(item_num):
                    amounts[item_col] = int(item_num)
            
        if success:
            if (amounts["red"] > 12 or 
                amounts["green"] > 13 or 
                amounts["blue"] > 14): 
                success = False

        if success:
            total += int(game_id)

    return total


def solve2(input_data):
    games = input_data.split("\n")
    total = 0
    for game in games:
        game_info, other = game.split(":")
        _, game_id = game_info.split(" ")
        draws = other.split(";")
        success = True
        amounts = {
            "blue": 0,
            "red": 0,
            "green": 0
        }
        for draw in draws:
            items = draw.split(",")
            for item in items:
                item_num, item_col  = item.strip().split(" ")
                if amounts[item_col] < int(item_num):
                    amounts[item_col] = int(item_num)

        total += amounts["red"] * amounts["green"] * amounts["blue"]

    return total

if __name__ == "__main__":
    print("Program Start")
    use_sample = False

    #use_sample = True

    if use_sample:
        input_data_file = open("sample02.txt", "r")
    else:
        input_data_file = open("input02.txt", "r")

    input_data_text = input_data_file.read()
    input_data_file.close()

    ans1 = solve1(input_data_text)
    ans2 = solve2(input_data_text)

    print(f"Part 1: {ans1}")
    print(f"Part 2: {ans2}")