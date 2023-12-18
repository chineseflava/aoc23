import numpy as np

class Beam():
    def __init__(self, direction, pos):
        self.pos = pos
        self.direction = direction

    def traverse(self):
        if self.direction == "north":
            pos = (pos[0], pos[1]-1)
        elif self.direction == "east":
            pos = (pos[0]+1, pos[1])
        elif self.direction == "south":
            pos = (pos[0], pos[1]+1)
        elif self.direction == "west":
            pos = (pos[0]-1, pos[1])

def energize(grid, beams):
    y_size = len(grid)
    x_size = len(grid[0])
    egrid = np.zeros((y_size, x_size))
    for beam in beams:
        if beam.pos[0] < 0 or beam.pos[0] > x_size or beam.pos[1] < 0 or beam.pos[1] > y_size:
            return
    

    return egrid

def main():
    with open("inputs/16_test.txt", "r") as file:
        lines = file.readlines()
    grid = []
    for line in lines:
        row = line.strip("\n") 
        grid.append([*row])
    #print(grid)
    start = Beam("east", (0,0))
    energized_grid = energize(grid, start)

if __name__ == "__main__":
    main()