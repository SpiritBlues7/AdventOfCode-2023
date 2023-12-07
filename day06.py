import sys

def solve1(input_data):
    input_data = input_data.replace("  ", " ")
    input_data = input_data.replace("  ", " ")
    input_data = input_data.replace("  ", " ")
    times_raw, distance_raw = input_data.split("\n")
    times = times_raw.split(":")[1].strip().split(" ")
    distances = distance_raw.split(":")[1].strip().split(" ")

    ans = 1
    for i, _ in enumerate(times):
        count = 0
        for j in range(int(times[i])+1):
            result = j*(int(times[i])-j)
            if result > int(distances[i]):
                count += 1
        ans *= count
        
    return ans

def solve2(input_data):
    input_data = input_data.replace(" ", "")
    times_raw, distance_raw = input_data.split("\n")
    time = int(times_raw.split(":")[1].strip())
    distance = int(distance_raw.split(":")[1].strip())

    ans = 0
    for i in range(time+1):
        result = i*(time-i)
        if result > distance:
            ans = time - i - i + 1
            break
        
    return ans


if __name__ == "__main__":
    print("Program Start")
    use_sample = False

    #use_sample = True

    if use_sample:
        input_data_file = open("sample06.txt", "r")
    else:
        input_data_file = open("input06.txt", "r")

    input_data_text = input_data_file.read()
    input_data_file.close()

    ans1 = solve1(input_data_text)
    ans2 = solve2(input_data_text)

    print(f"Part 1: {str(ans1)}")
    print(f"Part 2: {str(ans2)}")