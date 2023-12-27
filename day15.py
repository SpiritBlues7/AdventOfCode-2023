from queue import deque

def solve1(input_data):
    datas = input_data.split(",")
    t = 0
    for data in datas:
        t += hash_alg(data)

    return t

def hash_alg(data):
    st = 0
    for c in data:
        st += ord(c)
        st *= 17
        st = st % 256
    return st


def score(boxes):
    t = 0
    for b, q in boxes.items():
        print(b, q)
        for i, (label, focal) in enumerate(boxes[b]):
            st = (b+1) * (i+1) * focal
            t += st
    return t

def solve2(input_data):
    datas = input_data.split(",")
    t = 0
    boxes = {}
    for data in datas:
        char_split = ""
        remove = True
        if '=' in data:
            char_split = '='
            remove = False
        else:
            char_split = '-'
        label, focal = data.split(char_split)
        if focal != "":
            focal = int(focal)
        box = hash_alg(label)
        

        if not remove:
            if box not in boxes:
                boxes[box] = deque()
                boxes[box].append((label, focal))
            else:
                found = False
                for i, (other_label, other_focal) in enumerate(boxes[box]):
                    if label == other_label:
                        boxes[box].insert(i, (label, focal))
                        boxes[box].remove((other_label, other_focal))
                        found = True
                        break
                if not found:
                    boxes[box].append((label, focal))
        else:
            if box in boxes:
                for i, (other_label, other_focal) in enumerate(boxes[box]):
                    if label == other_label:
                        boxes[box].remove((other_label, other_focal))
                        break

    return score(boxes)

if __name__ == "__main__":
    print("Program Start")
    use_sample = False

    #use_sample = True

    if use_sample:
        input_data_file = open("sample15.txt", "r")
    else:
        input_data_file = open("input15.txt", "r")

    input_data_text = input_data_file.read()

    input_data_file.close()

    ans1 = solve1(input_data_text)
    ans2 = solve2(input_data_text)

    print(f"Part 1: {ans1}")
    print(f"Part 2: {ans2}")