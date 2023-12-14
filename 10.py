import numpy as np

def traverse(grid, pos):
    return

def main():
    with open("inputs/10_test.txt", "r") as file:
        lines = file.readlines()
    grid = np.array([[e for e in line.strip("\n")] for line in lines], dtype='U25')
    print(grid)
    start = np.where(grid == 'S')
    print(start)

if __name__ == "__main__":
    main()