def solve1(input_data):
    data = input_data.split("\n")
    grid = {}
    global_number_coords = []
    symbols = set()
    for y, _ in enumerate(data):
        num_found = False
        num_coords = []
        num = ""
        for x, _ in enumerate(data[y]):
            grid[(x,y)] = data[y][x]
            if data[y][x].isdigit():
                num_found = True
                num += data[y][x]
                num_coords.append((x,y))
            else:
                if data[y][x] != '.':
                   symbols.add(data[y][x]) 
                if num_found:
                    global_number_coords.append((int(num), num_coords))
                num_found = False
                num = ""
                num_coords = []
        if num_found:
            global_number_coords.append((int(num), num_coords))
            num_found = False
            num = ""
            num_coords = []

    t = 0
    for num, coords in global_number_coords:
        symbol_found = False
        check_coords = []

        for x,y in coords:
            check_coords.append((x+1,y-1))
            check_coords.append((x+1,y))
            check_coords.append((x+1,y+1))
            check_coords.append((x,y-1))
            # check_coords.append((x,y))
            check_coords.append((x,y+1))
            check_coords.append((x-1,y-1))
            check_coords.append((x-1,y))
            check_coords.append((x-1,y+1))
        for coord in check_coords:
            if coord in grid:
                if grid[coord] in symbols:
                    symbol_found = True
        if symbol_found:
            t += num

    return str(t)


def solve2(input_data):
    data = input_data.split("\n")
    grid = {}
    global_number_coords = []
    symbols = set()
    for y, _ in enumerate(data):
        num_found = False
        num_coords = []
        num = ""
        for x, _ in enumerate(data[y]):
            grid[(x,y)] = data[y][x]
            if data[y][x].isdigit():
                num_found = True
                num += data[y][x]
                num_coords.append((x,y))
            else:
                if data[y][x] != '.':
                   symbols.add(data[y][x]) 
                if num_found:
                    global_number_coords.append((int(num), num_coords))
                num_found = False
                num = ""
                num_coords = []
        if num_found:
            global_number_coords.append((int(num), num_coords))
            num_found = False
            num = ""
            num_coords = []


    global_symbol_numbers = set()
    for num, coords in global_number_coords:
        symbol_found = False
        check_coords = []

        for x,y in coords:
            check_coords.append((x+1,y-1))
            check_coords.append((x+1,y))
            check_coords.append((x+1,y+1))
            check_coords.append((x,y-1))
            # check_coords.append((x,y))
            check_coords.append((x,y+1))
            check_coords.append((x-1,y-1))
            check_coords.append((x-1,y))
            check_coords.append((x-1,y+1))
        for coord in check_coords:
            if coord in grid:
                if grid[coord] == '*':
                    symbol_found = True
                    global_symbol_numbers.add((num, coord, False))
    
    t = 0
    global_symbol_numbers = list(global_symbol_numbers)
    for i, _ in enumerate(global_symbol_numbers):
        for j, _ in enumerate(global_symbol_numbers):
            if i == j:
                continue
            num1, coords1, found1 = global_symbol_numbers[i]
            num2, coords2, found2 = global_symbol_numbers[j]
            if coords1 == coords2 and not found1 and not found2:
                global_symbol_numbers[i] = (num1, coords1, True)
                global_symbol_numbers[j] = (num2, coords2, True)
                t += num1*num2

    return str(t)



if __name__ == "__main__":
    print("Program Start")
    use_sample = False

    #use_sample = True

    if use_sample:
        input_data_file = open("sample03.txt", "r")
    else:
        input_data_file = open("input03.txt", "r")

    input_data_text = input_data_file.read()
    input_data_file.close()

    ans1 = solve1(input_data_text)
    ans2 = solve2(input_data_text)

    print(f"Part 1: {ans1}")
    print(f"Part 2: {ans2}")