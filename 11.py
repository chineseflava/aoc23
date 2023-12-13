import numpy as np

def expand_universe(uni):
    expand_row_idxs = []
    expand_col_idxs = []
    
    for idx, row in enumerate(uni):
        if all(x == "." for x in row):
            expand_row_idxs.insert(0, idx)
    
    for idx, _ in enumerate(uni[0]):
        col = uni[:,idx]
        if all(x == "." for x in col):
            expand_col_idxs.insert(0,idx)
    
    for i in expand_col_idxs:
        uni = np.insert(uni, i, ".", axis=1)
    for i in expand_row_idxs:
        uni = np.insert(uni, i, ".", axis=0)
    
    return uni, expand_col_idxs, expand_row_idxs

def min_dist(uni, source, dest):
    source_idx = np.where(uni == source)
    dest_idx = np.where(uni == dest)

    row_range = [source_idx[0], dest_idx[0]]
    col_range = [source_idx[1], dest_idx[1]]

    row_range.sort()
    col_range.sort()

    dist = abs(source_idx[0]-dest_idx[0])+abs(source_idx[1]-dest_idx[1])
    #print(source)
    return int(dist), row_range, col_range
    

def main():
    with open("inputs/11.txt", "r") as file:
        lines = file.readlines()
    universe = np.array([[e for e in line.strip("\n")] for line in lines], dtype='U25')
    star_count = 1
    for row in range(universe.shape[0]):
        for col in range(universe.shape[1]):
            
            if universe[row, col] == "#":
                universe[row,col] = str(star_count)
                star_count += 1


    expanded_universe, expanded_cols, expanded_rows = expand_universe(universe)
    print(universe)
    dists = []
    # Part 1
    # for i in range(star_count):
    #     for j in range(i+1,star_count):
    #         dist, _, _ = min_dist(expanded_universe, f"{i+1}", f"{j}")
    #         dists.append(dist)
    # print(sum(dists))

    # Part 2
    dists2 = []
    for i in range(star_count):
        for j in range(i+1,star_count):
            dist, row_range, col_range = min_dist(universe, f"{i+1}", f"{j}")
            
            for m in expanded_cols:
                if m < col_range[1] and m > col_range[0]:
                    dist += 999999
            for m in expanded_rows:
                if m < row_range[1] and m > row_range[0]:
                    dist += 999999
            dists2.append(dist)
    
    print(sum(dists2))

    #print(min_dist(universe, "5", "9"))



if __name__ == "__main__":
    main()