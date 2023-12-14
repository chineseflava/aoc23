import numpy as np
import math


def find_symmetry(pattern):
    #horizontal
    for i, _ in enumerate(pattern):
        if i < len(pattern)/2:
            top = pattern[:i]
            bottom = np.flip(pattern[i:i*2], axis=0)
        else:
            bottom = np.flip(pattern[i:], axis=0)
            top = pattern[i-len(bottom):i]
        if np.array_equal(top, bottom) and i != 0:
            return i*100
    #vertical
    hpattern = pattern.T

    for i, _ in enumerate(hpattern):
        if i < len(hpattern)/2:
            top = hpattern[:i]
            bottom = np.flip(hpattern[i:i*2], axis=0)
        else:
            bottom = np.flip(hpattern[i:], axis=0)
            top = hpattern[i-len(bottom):i]
        if np.array_equal(top, bottom) and i != 0:
            return i
        
def all_versions(pattern):
    versions = []

    r, c = len(pattern), len(pattern[0])

    for i in range(r):
        for j in range(c):
            smudged_pattern = [row.copy() for row in pattern]
            smudged_pattern[i][j] = "#" if pattern[i][j] == "." else "."

            versions.append(smudged_pattern)
    return versions


def main():
    with open("inputs/13.txt", "r") as file:
        lines = file.readlines()
    patterns = []
    pattern = []
    for i, line in enumerate(lines):
        if i == len(lines)-1:
                pattern.append(line.strip("\n"))
                patterns.append(np.array([list(map(str, row)) for row in pattern])) 
        if line == "\n":
            patterns.append(np.array([list(map(str, row)) for row in pattern]))    
            pattern = []
        else:
            pattern.append(line.strip("\n"))
    scores = []
    #find_symmetry(patterns[2])
    for pattern in patterns:
        score = find_symmetry(pattern)
        if score:
            scores.append(score)
    print(len(scores))
    print(sum(scores))

    #part 2

    extended_patterns = []
    for pattern in patterns:
        extended_pattern = all_versions(pattern)
        
        extended_patterns += extended_pattern
        #print(extended_pattern)
    
    scores2 = []
    for pattern in extended_patterns:
        
        score = find_symmetry(pattern)
        if score:
            scores2.append(score)
    print(len(scores2))
    print(sum(scores2))
    
    #print(patterns)
if __name__ == "__main__":
    main()