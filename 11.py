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
    
    return uni

def min_dist(uni, source, destination):
    return

def main():
    with open("inputs/11_test.txt", "r") as file:
        lines = file.readlines()
    universe = np.array([[e for e in line.strip("\n")] for line in lines])

    universe = expand_universe(universe)


if __name__ == "__main__":
    main()