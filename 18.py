import numpy as np
from skimage.morphology import binary_closing, binary_erosion
from skimage.segmentation import find_boundaries

class Digger():
    def __init__(self):
        self.coords = [(0,0)]
        self.max_x = 0
        self.max_y = 0

    def process_line(self, line):
        for _ in range(int(line[1])):
            last_pos = self.coords[-1]
            if line[0] == "R":
                self.coords.append((last_pos[0]+1, last_pos[1]))
            if line [0] == "D":
                self.coords.append((last_pos[0], last_pos[1]+1))
            if line [0] == "U":
                self.coords.append((last_pos[0], last_pos[1]-1))
            if line [0] == "L":
                self.coords.append((last_pos[0]-1, last_pos[1]))
            
            # Increase range
            if self.coords[-1][0] > self.max_x:
                self.max_x = self.coords[-1][0]
            if self.coords[-1][1] > self.max_y:
                self.max_y = self.coords[-1][1]
            
def fill_trench(diglet):
    trench = np.zeros((diglet.max_x+1, diglet.max_y+1))
    for coord in diglet.coords:
        trench[coord] = 1
    
    def fill(trench):
        bounds = find_boundaries(trench, connactivity=1, mode='inner')
        closed_bounds = binary_closing(bounds, binary_erosion(bounds))
        result = trench.copy()
        result[closed_bounds] = 1
        return result

    trench = fill(trench)
    return trench

def main():
    with open("inputs/18_test.txt", "r") as file:
        lines = file.readlines()
    dig_plan = [line.strip("\n").split() for line in lines]

    diglet = Digger()
    for line in dig_plan:
        diglet.process_line(line)
    
    trench = fill_trench(diglet)
    print(sum(sum(trench)))
if __name__ == "__main__":
    main()