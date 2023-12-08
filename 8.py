import math

def main():
    with open("inputs/8.txt", "r") as file:
        lines = file.readlines()
    instructions = {}
    move_pattern = lines[0].strip("\n")

    for line in lines[2:]:
        split_line = line.strip("\n").split()
        instructions[split_line[0]]=(split_line[2][1:-1], split_line[3][:-1])
    #print(instructions)
    
    # # Part 1
    # curr = "11A"
    # i = 0
    # while not curr.endswith("Z"):
    #     idx = i % len(move_pattern)
    #     if move_pattern[idx] == "R":
    #         curr = instructions[curr][1]
    #     if move_pattern[idx] == "L":
    #         curr = instructions[curr][0]
    #     i += 1
    
    # print(i)


    #¤ Part 2

    curr = [key for key in instructions.keys() if key.endswith("A")]
    #i = 0
    cycles = []
    for c in curr:
        i = 0
        while not c.endswith("Z"):
            idx = i % len(move_pattern)
            if move_pattern[idx] == "R":
                c = instructions[c][1]
            if move_pattern[idx] == "L":
                c = instructions[c][0]
            i += 1
        cycles.append(i)
    print(cycles)
    print(math.lcm(*cycles))


    #     for j, _ in enumerate(curr):
    #         if move_pattern[idx] == "R":
    #            curr[j] = instructions[curr[j]][1]
    #         if move_pattern[idx] == "L":
    #            curr[j] = instructions[curr[j]][0]
    #     i += 1
    #     if all (c.endswith("Z") for c in curr):
    #         break
    # while True:
    #     idx = i % len(move_pattern)
    #     for j, _ in enumerate(curr):
    #         if move_pattern[idx] == "R":
    #            curr[j] = instructions[curr[j]][1]
    #         if move_pattern[idx] == "L":
    #            curr[j] = instructions[curr[j]][0]
    #     i += 1
    #     if all (c.endswith("Z") for c in curr):
    #         break
    #     #print(curr)
    #     print(i)
    # print(i)
        

if __name__ == "__main__":
    main()