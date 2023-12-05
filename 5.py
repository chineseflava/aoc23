
def process_input(lines):
    maps = []
    seeds = [eval(i) for i in lines[0].strip("\n").split()[1:]]
    seeds_part2 = []
    for idx, seed in enumerate(seeds):
        if idx%2 == 0:
            seeds_part2.append(range(seeds[idx], seeds[idx]+seeds[idx+1]))
    print(seeds_part2)

    for idx, line in enumerate(lines):
        if line == "\n":
            map = []
            name = lines[idx+1][:-6]

            idx += 1
            while not lines[idx+1] == "\n":
                values = lines[idx+1].strip("\n").split()
                # for i in range(int(values[2])):
                #     map[int(values[1])+i] = int(values[0])+i
                values = [int(i) for i in values]
                map.append(values)
                idx += 1
                if idx+1 == len(lines):
                    break
            maps.append(map)
            #print(map)
            
    #print(data)
    return seeds, maps

def main():
    with open("inputs/5.txt", "r") as file:
        lines = file.readlines()
    seeds, maps = process_input(lines)
    #print(seeds)
    locations = []
    for seed in seeds:
        for map in maps:
            #print(map)
            for item in map:
                if seed >= item[1] and seed <= item[1]+item[2]:
                    #print(f"mapped to{map[seed]}")
                    seed = seed+(item[0]-item[1])
                    break
                
            
            #print(f"Seed:{seed}")
        locations.append(seed)
    print(locations)
    print(min(locations))


if __name__ == "__main__":
    main()
