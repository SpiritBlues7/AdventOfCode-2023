def solve1(input_data):
    data = input_data.split("\n")

    return ""


def solve2(input_data):
    data = input_data.split("\n")

    return ""


if __name__ == "__main__":
    print("Program Start")
    use_sample = False

    use_sample = True

    if use_sample:
        input_data_file = open("sampleXX.txt", "r")
    else:
        input_data_file = open("inputXX.txt", "r")

    input_data_text = input_data_file.read()
    input_data_file.close()

    ans1 = solve1(input_data_text)
    ans2 = solve2(input_data_text)

    print(f"Part 1: {ans1}")
    print(f"Part 2: {ans2}")