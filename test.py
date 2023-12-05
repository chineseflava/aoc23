seeds, *maps = open('inputs/5.txt').read().split('\n\n')
seeds = [int(i) for i in seeds.split()[1:]]
maps = [[[int(i) for i in line.split()] for line in m.splitlines()[1:]] for m in maps]

# part 1
def map_seed(s, m):
    for md, ms, ml in m:
        if s >= ms and s < ms + ml:
            return s + md - ms
    return s


# part 2
ranges = list(zip(seeds[::2], seeds[1::2]))
for m in maps:
    new_ranges = []
    for rs, rl in ranges:
        for md, ms, ml in m:
            if rs < ms + ml and ms < rs + rl:
                os = max(rs, ms)
                ol = min(rs + rl, ms + ml) - os
                new_ranges += [(os - ms + md, ol)]
                if os > rs or os + ol < rs + rl: 
                    ranges += [(rs, os - rs), (os + ol, rs + rl - os - ol)]
                break
            else: new_ranges += [(rs, rl)]
    ranges = new_ranges
print(min(r[0] for r in ranges))