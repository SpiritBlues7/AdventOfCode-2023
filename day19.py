from queue import deque

class Instruct:
    def __init__(self, param, less, v, dest):
        self.param = param
        self.less = less
        self.v = v
        self.dest = dest

    def __str__(self):
        return f"INSTRUCTION: {self.param} {"<" if self.less else ">"} {self.v} : {self.dest}"

    def __hash__(self):
        return hash(self.param)

    def __eq__(self, other):
        return (self.param == other.param 
            and self.less == other.less 
            and self.v == other.v 
            and self.dest == other.dest)

def solve1(input_data):
    workflow_data, cog_data = input_data.split("\n\n")
    parts = workflow_data.split("\n")
    workflows = {}
    rejects = {}
    params = ['x','m','a','s']
    for part in parts:
        label, instructs_raw = part.split("{")
        instructs_raw.replace("}", "")
        instructs = instructs_raw.split(",")
        instructs_found = []
        for single_instruct in instructs:
            if len(single_instruct) > 2 and (single_instruct[1] == "<" or single_instruct[1] == ">"):
                clause, dest = single_instruct.split(":")
                param = clause[0]
                less = (clause[1] == "<")
                
                v = int(clause[2:])
                instructs_found.append(Instruct(param, less, v, dest))
            else:
                rejects[label] = single_instruct[:-1]
        workflows[label] = instructs_found
    
    cogs_data = cog_data.split("\n")
    cogs = []
    for cog_data in cogs_data:
        cog = {}
        cog_data = cog_data[1:-1].split(",")
        for dat in cog_data:
            param, v = dat.split("=")
            cog[param] = int(v)
        cogs.append(cog)


    t = 0
    for cog in cogs:
        current_w_param = "in"
        cog_accept = False
        while True:
            if current_w_param == "A":
                cog_accept = True
                break
            elif current_w_param == "R":
                assert cog_accept == False
                cog_accept = False
                break
            current_w = workflows[current_w_param]
            clause_found = False
            for i in current_w:
                if (i.less and cog[i.param] < i.v) or (not i.less and cog[i.param] > i.v):
                    current_w_param = i.dest
                    clause_found = True
                    break
            if not clause_found:
                current_w_param = rejects[current_w_param]
        
        if cog_accept:
            t += cog["x"] + cog["m"] + cog["a"] + cog["s"]

    return t


def solve2(input_data):
    workflow_data, cog_data = input_data.split("\n\n")
    parts = workflow_data.split("\n")
    workflows = {}
    rejects = {}
    params = ['x','m','a','s']
    for part in parts:
        label, instructs_raw = part.split("{")
        instructs_raw.replace("}", "")
        instructs = instructs_raw.split(",")
        instructs_found = []
        for single_instruct in instructs:
            if len(single_instruct) > 2 and (single_instruct[1] == "<" or single_instruct[1] == ">"):
                clause, dest = single_instruct.split(":")
                param = clause[0]
                less = (clause[1] == "<")
                
                v = int(clause[2:])
                instructs_found.append(Instruct(param, less, v, dest))
            else:
                rejects[label] = single_instruct[:-1]
        workflows[label] = instructs_found
    
    current_ranges = []
    upper = 4000
    initial_range = ("in", 0, {'x': (1,upper), 'm':(1,upper), 'a':(1,upper), 's':(1,upper)})
    current_ranges.append(initial_range)

    t = 0
    while len(current_ranges) > 0:
        current_w_param, current_instruct, current_range = current_ranges.pop()

        if current_w_param == "A":
            t += ((current_range['x'][1]-current_range['x'][0] + 1) 
                * (current_range['m'][1]-current_range['m'][0] + 1) 
                * (current_range['a'][1]-current_range['a'][0] + 1) 
                * (current_range['s'][1]-current_range['s'][0] + 1))
            continue
        elif current_w_param == "R":
            continue

        current_w = workflows[current_w_param]
        if current_instruct >= len(current_w):
            current_w_param = rejects[current_w_param]
            current_instruct = 0
            current_ranges.append((current_w_param, current_instruct, current_range.copy()))
            continue
        
        i = current_w[current_instruct]
        if i.less:
            if current_range[i.param][0] < i.v and current_range[i.param][1] < i.v:
                current_ranges.append((i.dest, 0, current_range.copy()))
            elif current_range[i.param][0] > i.v and current_range[i.param][1] > i.v:
                current_ranges.append((current_w_param, current_instruct + 1, current_range.copy()))
            elif current_range[i.param][0] < i.v and current_range[i.param][1] > i.v:
                accepted_range = current_range.copy()
                rejected_range = current_range.copy()
                accepted_range[i.param] = (current_range[i.param][0], i.v - 1)
                rejected_range[i.param] = (i.v, current_range[i.param][1])
                current_ranges.append((i.dest, 0, accepted_range))
                current_ranges.append((current_w_param, current_instruct + 1, rejected_range))
            else:
                assert False
        else:
            if current_range[i.param][0] > i.v and current_range[i.param][1] > i.v:
                current_ranges.append((i.dest, 0, current_range.copy()))
            elif current_range[i.param][0] < i.v and current_range[i.param][1] < i.v:
                current_ranges.append((current_w_param, current_instruct + 1, current_range.copy()))
            elif current_range[i.param][0] < i.v and current_range[i.param][1] > i.v:
                accepted_range = current_range.copy()
                rejected_range = current_range.copy()
                rejected_range[i.param] = (current_range[i.param][0], i.v)
                accepted_range[i.param] = (i.v + 1, current_range[i.param][1])
                current_ranges.append((i.dest, 0, accepted_range))
                current_ranges.append((current_w_param, current_instruct + 1, rejected_range))
            else:
                assert False    
    
    return t

if __name__ == "__main__":
    print("Program Start")
    use_sample = False

    #use_sample = True

    if use_sample:
        input_data_file = open("sample19.txt", "r")
    else:
        input_data_file = open("input19.txt", "r")

    input_data_text = input_data_file.read()

    input_data_file.close()

    ans1 = solve1(input_data_text)
    ans2 = solve2(input_data_text)

    print(f"Part 1: {ans1}")
    print(f"Part 2: {ans2}")