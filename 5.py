
def process_input(lines):
    data = []
    seeds = [eval(i) for i in lines[0].strip("\n").split()[1:]]

    for idx, line in enumerate(lines):
        if line == "\n":
            name = lines[idx+1][:-6]
            items = []
            map = {}
            idx += 1
            while not lines[idx+1] == "\n":
                values = lines[idx+1].strip("\n").split()
                for i in range(int(values[2])):
                    map[int(values[0])+i] = int(values[1])+i
                
                idx += 1
                if idx+1 == len(lines):
                    break
            # print(map)
            data.append(map)
    #print(data)
    return seeds, data

def main():
    with open("inputs/5_test.txt", "r") as file:
        lines = file.readlines()
    seeds, maps = process_input(lines)
    print(seeds)
    locations = []
    for seed in seeds:
        for map in maps:
            print(map)
            if seed in map:
                seed = map[seed]
            else:
                continue
            #print(seed)
        locations.append(seed)
    print(locations)

if __name__ == "__main__":
    main()
