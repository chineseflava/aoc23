from sympy import *
import math

def main():
    with open("inputs/6.txt", "r") as file:
        lines = file.readlines()
    times = lines[0].strip("\n").split()[1:]
    distances = lines[1].strip("\n").split()[1:]

    # Part 1
    wins = 1
    h = symbols('h')
    for t, d in zip(times, distances):
        # Solve t*h-h**2-d-1 = 0
        intersects = solve(int(t)*h-h**2-int(d)-1, h)
        win_count = floor(intersects[1])-math.ceil(intersects[0])+1
        wins *= floor(intersects[1])-math.ceil(intersects[0])+1
    print(f"Answer 1: {wins}")

    # Part 2
    wins = 1
    # Clump times and distances together.
    t = ''.join(times)
    d = ''.join(distances)
    intersects = solve(int(t)*h-h**2-int(d)-1, h)
    win_count = floor(intersects[1])-math.ceil(intersects[0])+1
    print(win_count)
    wins *= floor(intersects[1])-math.ceil(intersects[0])+1.
    print(f"Answer 2: {wins}")

if __name__ == "__main__":
    main()
