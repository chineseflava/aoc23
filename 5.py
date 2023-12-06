
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
def split_ranges(seeds, map):
    new_seeds = []
    unedited_seeds = []
    for seed in seeds:
        seed_start = seed[0]
        seed_end = seed[1]
        
        map_source = map[1]
        map_range = map[2]
        map_end = map_source+map_range
        map_diff = map[0] - map[1]

        # Determine the order of ranges
        if seed_start <= map_source:
            smaller_range_start, smaller_range_end = seed_start, seed_end
            larger_range_start, larger_range_end = map_source, map_end
        else:
            smaller_range_start, smaller_range_end = map_source, map_end
            larger_range_start, larger_range_end = seed_start, seed_end
        
        # Check if the ranges overlap
        if smaller_range_end < larger_range_start:
            # No overlap
            return None, None
        
        # Determine the overlap range
        overlap_start = max(smaller_range_start, larger_range_start) + map_diff
        overlap_end = min(smaller_range_end, larger_range_end) + map_diff
        
        # Determine the non-overlapping ranges
        non_overlap1_start = smaller_range_start
        non_overlap1_end = min(smaller_range_end, overlap_start - 1)
        non_overlap2_start = max(larger_range_start, overlap_end + 1)
        non_overlap2_end = larger_range_end
        
        new_seed = (overlap_start, overlap_end)
        unedited_seed = [(non_overlap1_start, non_overlap1_end), (non_overlap2_start, non_overlap2_end)]
        new_seeds.append(new_seed)
        for item in unedited_seed:
            unedited_seeds.append(item)
        #unedited_seeds.append(unedited_seed)
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
    print(locations)
    print(min(locations))

    #Part 2
    seeds = [(left, left + right) for left, right in zip(seeds[::2], seeds[1::2])]
    print(seeds)
    locations = []
    for map in maps:
        this_seeds = seeds
        next_seeds = []
        for item in map:
            new_seeds, unedited_seeds = split_ranges(this_seeds, item)
            if new_seeds:
                next_seeds.append(new_seeds)
                this_seeds = unedited_seeds
            

                
            


    # for map in maps:
    #     new_seeds = []
    #     for seed_start, seed_range in seeds2:
    #         print(map)
    #         for md, ms, ml in map:
    #             if seed_start < ms + ml and ms < seed_start + seed_range:
    #                 os = max(seed_start, ms)
    #                 ol = min(seed_start + seed_range, ms+ml) - os
    #                 new_seeds += [(os - ms + md, ol)]
    #                 if os > seed_start or os + ol < seed_start + seed_range: 
    #                     ranges += [(seed_start, os - seed_start), (os + ol, seed_start + seed_range - os - ol)]
    #                 break
    #         else: new_seeds += [(seed_start, seed_range)]
    #     seeds = new_seeds


    # for seeds in seeds2:
    #     for seed in seeds:
    #         for map in maps:
    #         #print(map)
    #             for item in map:
    #                 if seed >= item[1] and seed <= item[1]+item[2]:
    #                     #print(f"mapped to{map[seed]}")
    #                     seed = seed+(item[0]-item[1])
    #                     break
    #         locations.append(seed)
    print(locations)
    print(min(locations))


if __name__ == "__main__":
    main()
