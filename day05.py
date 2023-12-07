import sys

def solve1(input_data):
    data = input_data.split("\n\n")
    seeds = data[0].split(":")[1].split(" ")
    lowest = sys.maxsize
    for seed in seeds[1:]:
        cur_val = int(seed)
        for dat in data[1:]:
            g = dat.split("\n")[1:]
            for line in g:
                dest, source, amount = line.split(" ")
                if cur_val >= int(source) and cur_val <= int(source) + int(amount):
                    cur_val = int(dest) + (int(cur_val) - int(source))
                    break
        lowest = min(lowest, int(cur_val))

    return lowest

def solve2(input_data):
    data = input_data.split("\n\n")
    seeds = data[0].split(":")[1].split(" ")
    seeds = seeds[1:]
    current_ranges = set()
    total_seeds = []
    for i in range(0, len(seeds)-1,2):
        current_ranges.add((seeds[i],seeds[i+1]))
    lowest = sys.maxsize

    for dat in data[1:]:
        next_range = set()
        while len(current_ranges) > 0:
            (cur_start, cur_amount) = current_ranges.pop()
            cur_start = int(cur_start)
            cur_amount = int(cur_amount)
            if cur_amount == 0:
                continue
            cur_end = cur_start + cur_amount

            g = dat.split("\n")[1:]
            found_ranges = []
            changed = False
            for line in g:
                dest, source, amount = line.split(" ")
                dest = int(dest)
                source = int(source)
                amount = int(amount)
                source_end = source + amount
                start_found = -1
                end_found = -1
                if (cur_start <= source and cur_end >= source_end):
                    start_found = source
                    end_found = source_end
                    current_ranges.add((cur_start, max(source - cur_start - 1, 0)))
                    current_ranges.add((source_end + 1, max(cur_end - source_end - 1, 0)))
                if (cur_start >= source and cur_end <= source_end):
                    start_found = cur_start
                    end_found = cur_end
                if (cur_start <= source and cur_end > source and cur_end <= source_end):
                    start_found = source
                    end_found = cur_end
                    current_ranges.add((cur_start, max(source - cur_start - 1, 0)))
                if (cur_start >= source and cur_start < source_end and cur_end >= source_end):
                    start_found = cur_start
                    end_found = source_end
                    current_ranges.add((source_end + 1, max(cur_end - source_end - 1, 0)))
                if (start_found != -1):
                    next_range.add((dest + (start_found - source), 
                        end_found - start_found))
                    changed = True
            if not changed:
                next_range.add((cur_start,cur_amount))

                
        current_ranges = next_range
    
    for ran in current_ranges:
        lowest = min(lowest, ran[0])


    return lowest


if __name__ == "__main__":
    print("Program Start")
    use_sample = False

    #use_sample = True

    if use_sample:
        input_data_file = open("sample05.txt", "r")
    else:
        input_data_file = open("input05.txt", "r")



    input_data_text = input_data_file.read()
    input_data_file.close()

    ans1 = solve1(input_data_text)
    ans2 = solve2(input_data_text)

    print(f"Part 1: {str(ans1)}")
    print(f"Part 2: {str(ans2)}")