import numpy as np


def find_symmetry(pattern):
    #horizontal
    for i, row in enumerate(pattern):
        top = pattern[:i]
        bottom = np.flip(pattern[i:i*2], axis=0)
        if np.array_equal(top, bottom) and i != 0:
            return i, "horizontal"
    for j, _ in enumerate(pattern[0]):
        left = pattern[:,:j]
        right = np.flip(pattern[:, j:j*2], axis=0)
        print(left, right)
        if np.array_equal(left, right) and j != 0:
            return j, "vertical"


def main():
    with open("inputs/13_test.txt", "r") as file:
        lines = file.readlines()
    patterns = []
    pattern = []
    for i, line in enumerate(lines):
        if line == "\n" or i == len(lines)-1:
            patterns.append(np.array([list(map(str, row)) for row in pattern]))
            pattern = []
        else:
            pattern.append(line.strip("\n"))
    find_symmetry(patterns[0])
        
    
    #print(patterns)
if __name__ == "__main__":
    main()