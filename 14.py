import numpy as np

def shift_stones(platform):
    shifted_platform = []
    for row in platform:
        for i, _ in enumerate(row):
            if row[-i-1] == "O":
                right = row[-i-1:]
                for j, _ in enumerate(right):
                    if j == 0 and i == 0:
                        continue
                    elif j == len(right)-1:
                        row[-i-1] = "."
                        right[j] = "O"
                        
                        new_row = new_row = np.concatenate([row[:-i],right[-i:]])
                        row = new_row
                        break
                    elif right[j+1] == "#" or right[j+1] == "O":
                        row[-i-1] = "."
                        right[j] = "O"
                        
                        new_row = np.concatenate([row[:-i],right[-i:]])
                        row = new_row
                        break
                    else:
                        continue
        shifted_platform.append(list(row))
    return shifted_platform

def get_load(pl):
    total_load = 0
    for row in pl:
        for i, pos in enumerate(row):
            if pos == "O":
                total_load += i+1
    return total_load

def perform_cycle(pl):
    for i in range(4):
        pl = np.rot90(pl, k=-1)
        pl = shift_stones(pl)
    return pl
        



def main():
    with open("inputs/14.txt", "r") as file:
        lines = file.readlines()
    platform = []
    for line in lines:
        row = line.strip("\n").split() 
        platform.append([*row[0]])
    #print(platform)
    platform = np.array(platform)
    shifted_platform = shift_stones(np.rot90(platform, k=-1))#platform[::-1].T)

    for row in shifted_platform:
        print(row)
    print(get_load(shifted_platform))

    # Part 2
    for i in range(10000):
        platform = perform_cycle(platform)
        print(f"Load: {get_load(np.rot90(platform, k=-1))}, cycle: {i+1}")
    # Write some code to detect the repeating pattern...
    # I found that the pattern repeats every 17th cycle after about 100 loops.
    # (1000000000-109)%17 = 0 so answer is same as after 109 cycles.


if __name__ == "__main__":
    main()