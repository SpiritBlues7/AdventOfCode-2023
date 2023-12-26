
def get_sym_coords(sections: set, section_total: int, section_indexed: dict, original=-1):
    for section_num, section_data in sections:
        if section_num == 0:
            continue
        if (section_num - 1, section_data) in sections:
            adjusted_section = section_num - 1
            for adjusted_amount in range(1, section_num + 1):
                if (section_num + adjusted_amount == section_total
                    or section_num - adjusted_amount == 0):
                    if section_num == original:
                        break
                    return section_num, section_num + 1
                new_match_num = section_num + adjusted_amount
                new_match_data = section_indexed[new_match_num]
                adjusted_section = section_num - adjusted_amount - 1
                if (adjusted_section, new_match_data) not in sections:
                    break

def solve1(input_data):
    maps = input_data.split("\n\n")
    t = 0
    for cur_map in maps:
        cur_map = cur_map.split("\n")
        r_total = len(cur_map)
        c_total = len(cur_map[0])
        rows = set()
        cols = set()
        rows_indexed = {}
        cols_indexed = {}
        for r in range(r_total):
            rows.add((r,cur_map[r]))
            rows_indexed[r] = cur_map[r]

        for c in range(c_total):
            c_cur = ""
            for r in range(r_total):
                c_cur += cur_map[r][c]
            cols.add((c, c_cur))
            cols_indexed[c] = c_cur
    


        col_result = get_sym_coords(cols, c_total, cols_indexed)
        if col_result is not None:
            col1, col2 = col_result
            t += col1
        row_result = get_sym_coords(rows, r_total, rows_indexed)
        if row_result is not None:
            row1, row2 = row_result
            t += 100*row1
        # print()
        # for r in cur_map:
        #     for c in r:
        #         print(c, end="")
        #     print()
        assert col_result is not None or row_result is not None

    return t


def solve2(input_data):
    maps = input_data.split("\n\n")
    t = 0
    for cur_map in maps:
        cur_map = cur_map.split("\n")
        r_total = len(cur_map)
        c_total = len(cur_map[0])
        hashes = set()
        for r in range(r_total):
            for c in range(c_total):
                if cur_map[r][c] == "#":
                    hashes.add((r,c))

        rows = set()
        cols = set()
        rows_indexed = {}
        cols_indexed = {}
        for r in range(r_total):
            rows.add((r,cur_map[r]))
            rows_indexed[r] = cur_map[r]

        for c in range(c_total):
            c_cur = ""
            for r in range(r_total):
                c_cur += cur_map[r][c]
            cols.add((c, c_cur))
            cols_indexed[c] = c_cur

        original_c = -1
        original_r = -1
        found = False
        col_result = get_sym_coords(cols, c_total, cols_indexed)
        if col_result is not None:
            col1, col2 = col_result
            original_c = col1
        row_result = get_sym_coords(rows, r_total, rows_indexed)
        if row_result is not None:
            row1, row2 = row_result
            original_r = row1

        for h_r, h_c in hashes:
            new_cur_map = cur_map.copy()
            new_cur_map[h_r] = new_cur_map[h_r][:h_c] + "." + new_cur_map[h_r][h_c+1:]
            rows = set()
            cols = set()
            rows_indexed = {}
            cols_indexed = {}
            for r in range(r_total):
                rows.add((r,new_cur_map[r]))
                rows_indexed[r] = new_cur_map[r]

            for c in range(c_total):
                c_cur = ""
                for r in range(r_total):
                    c_cur += new_cur_map[r][c]
                cols.add((c, c_cur))
                cols_indexed[c] = c_cur

            if h_r == 6 and h_c == 8:
                print("here")
            col_result = get_sym_coords(cols, c_total, cols_indexed, original_c)
            if col_result is not None:
                col1, col2 = col_result
                t += col1
                assert not found
                found = True
                break
            row_result = get_sym_coords(rows, r_total, rows_indexed, original_r)
            if row_result is not None:
                row1, row2 = row_result
                t += 100*row1
                assert not found
                found = True
                break
        print()
        for r in cur_map:
            for c in r:
                print(c, end="")
            print()
        assert found
        
    return t


if __name__ == "__main__":
    print("Program Start")
    use_sample = False

    #use_sample = True

    if use_sample:
        input_data_file = open("sample13.txt", "r")
    else:
        input_data_file = open("input13.txt", "r")

    input_data_text = input_data_file.read()

    input_data_file.close()

    ans1 = solve1(input_data_text)
    ans2 = solve2(input_data_text)

    print(f"Part 1: {ans1}")
    print(f"Part 2: {ans2}")