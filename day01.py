def solve1(input_data):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for ch in alpha:
        input_data = input_data.replace(ch, "")
    input_data = input_data.splitlines()
    t = 0
    for line in input_data:
        num = int(line[0] + line[-1])
        t += num
    return t

def solve2(input_data):
    digits = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine"
        ]
    forward_parse = ""
    backward_parse = ""
    for i, ch in enumerate(input_data):
        forward_parse += ch
        backward_parse = input_data[len(input_data)-1-i] + backward_parse
        for j in range(0,9):
            forward_parse = forward_parse.replace(digits[j], str(j+1))
            backward_parse = backward_parse.replace(digits[j], str(j+1))
    forward_parse = forward_parse.splitlines()
    backward_parse = backward_parse.splitlines()
    combined_input_data = ""
    for i, _ in enumerate(forward_parse):
        combined_input_data += forward_parse[i] + backward_parse[i] + "\n"     
    return solve1(combined_input_data)
        
if __name__ == "__main__":
    print("Program Start")
    use_sample = False

    #use_sample = True

    if use_sample:
        input_data_file = open("sample01.txt", "r")
    else:
        input_data_file = open("input01.txt", "r")

    input_data_text = input_data_file.read()
    input_data_file.close()

    ans1 = solve1(input_data_text)
    ans2 = solve2(input_data_text)

    print(f"Part 1: {ans1}")
    print(f"Part 2: {ans2}")