import numpy as np

def shift_stones(row):
    for idx, _ in enumerate(row):
        if row[-idx-1] == "O":
            right = row[-idx:]
            for i, _ in enumerate(right):
                if right[i+1] == "#" or right[i+1] == "O":
                    right[i] = "O"
                    new_row = row[-idx-2] + "." + right
                    row = new_row
                    break
                elif i == len(right):
                    right[i] = "O"
                    new_row = row[-idx-2] + "." + right
                    row = new_row
                    break
                else:
                    continue
    return row


def main():
    with open("inputs/14_test.txt", "r") as file:
        lines = file.readlines()
    platform = []
    for line in lines:
        row = line.strip("\n").split() 
        platform.append([*row[0]])
    print(platform)
    platform = np.array(platform)

    for row in platform:
        row = shift_stones(row)


if __name__ == "__main__":
    main()