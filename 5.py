
def process_input(lines):
    maps = []
    seeds = [eval(i) for i in lines[0].strip("\n").split()[1:]]
    #seeds_part2 = []
    # for idx, seed in enumerate(seeds):
    #     if idx%2 == 0:
    #         seeds_part2.append(range(seeds[idx], seeds[idx]+seeds[idx+1]))
    #print(seeds_part2)

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

"""
(destination, source, range length)
"""
# Get only overlap of range [ss,se] and the leftover parts.
def get_overlap(ss, se, ms, me):
    if ss < me and se > ms:
        unedited_range = []
        # Also adjust the seeds to new destination, maybe do this somewhere else more fitting later...
        overlap_range = (max(ss, ms), min(se, me))
        left_range = (ss, overlap_range[0]-1)
        right_range = (overlap_range[1]+1, se)
        if left_range[0] < left_range[1]:
            unedited_range.append(left_range)
        if right_range[0] < right_range[1]:
            unedited_range.append(right_range)
        
        return overlap_range, unedited_range
    else:
        return None, [(ss, se)]
    
def source_to_dest(seeds, map):
    unedited_seeds = []
    new_seeds = []
    for seed in seeds:
        ss = seed[0]
        se = seed[1]
        ms = map[1]
        map_range = map[2]
        me = ms+map_range
        map_diff = map[0] - map[1]
        new_range, unedited_range = get_overlap(ss, se, ms, me)
        if new_range:
            new_seeds.append((new_range[0]+map_diff, new_range[1]+map_diff))
        for range in unedited_range:
            unedited_seeds.append(range)
    return new_seeds, unedited_seeds
                 
def main():
    with open("inputs/5_test.txt", "r") as file:
        lines = file.readlines()
    seeds, maps = process_input(lines)
    
    #print(seeds)
    #Part 1
    locations = []
    for seed in seeds:
        for map in maps:
            #print(map)
            for item in map:
                if seed >= item[1] and seed <= item[1]+item[2]:
                    seed = seed+(item[0]-item[1])
                    break
        locations.append(seed)
    #print(locations)
    print(min(locations))

    #Part 2
    seeds = [(left, left + right) for left, right in zip(seeds[::2], seeds[1::2])]
    #print(seeds)
    locations = []
    next_seeds = []
    for map in maps:
        this_seeds = seeds
        next_seeds = []
        for item in map:
            new_seeds, unedited_seeds = source_to_dest(this_seeds, item)
            if new_seeds:
                next_seeds.append(new_seeds)
                this_seeds = unedited_seeds
        next_seeds.append(this_seeds)
    print(next_seeds)
        
    # print(locations)
    # print(min(locations))


if __name__ == "__main__":
    #print(get_overlap(3,12, 5,10))
    main()
