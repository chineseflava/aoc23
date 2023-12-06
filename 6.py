from sympy import *
import math

def intersects(t,d):
    h = symbols('h')
    intersects = solve(int(t)*h-h**2-int(d)-1, h)
    win_count = floor(intersects[1])-math.ceil(intersects[0])+1
    return win_count

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
        win_count = intersects (t,d)
        wins *= win_count
    print(f"Answer 1: {wins}")

    # Part 2
    # Clump times and distances together.
    t = ''.join(times)
    d = ''.join(distances)
    win_count = intersects(t,d)
    print(f"Answer 2: {win_count}")

if __name__ == "__main__":
    main()
