import re
import numpy as np

def is_symbol(x):
    symbols = "+$#@/&-%=*"
    if x in symbols:
        return True
    return False

def main():
    with open("inputs/3.txt", "r") as file:
        lines = file.readlines()
    schematic = []
    part_numbers = []
    gear_ratios = []

    for idx, line in enumerate(lines):
        if idx == 0:
            schematic.append("."*(len(line)+2))

        schematic_line = line.strip("\n").split()
        schematic.append("."+schematic_line[0]+".")
        if idx == len(lines)-1:
            schematic.append("."*(len(line)+2))

    for j, y in enumerate(schematic):
        for i, x in enumerate(y):
            if is_symbol(x):
                # Part 1
                numbers = []
                for n in range(j-1,j+2):
                    for m in range(i-1,i+2):
                         pos = schematic[n][m]
                         #print(pos)
                         if pos.isdigit():
                            number = pos
                            idx = m-1
                            #start = idx
                            while schematic[n][idx].isdigit():
                                number = schematic[n][idx] + number
                                idx -= 1
                                
                                
                            idx = m+1
                            while schematic[n][idx].isdigit():
                                number = number + schematic[n][idx]
                                idx += 1
                            start = idx-len(number)
                            numbers.append(number)

                            # Remove number from schematic.
                            print(schematic[n])
                            char_list = list(schematic[n])
                            char_list[start:start+len(number)] = "."*len(number)
                            schematic[n] = ''.join(char_list)
                part_numbers.append(int(number))   

                # Part 2
                if x == "*" and len(numbers)>1:
                    gear_ratio = int(numbers[0])*int(numbers[1])
                    gear_ratios.append(int(gear_ratio))
                    #print(part_number)

                
            
    for item in schematic:
        print(item)
    print(part_numbers)
    print(f"Answer 1: {sum(part_numbers)}")
    print(f"Answer 2: {sum(gear_ratios)}")

if __name__ == "__main__":
    main()