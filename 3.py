import re
import numpy as np

def contains_symbols(input_string, symbols="+$*#@/&-%="):
    for char in input_string:
        if char in symbols:
            return True
    return False

def main():
    with open("inputs/3.txt", "r") as file:
        lines = file.readlines()
    schematic = []
    errors = []
    #numbers = []
    #remove_symbols = "+$*#"
    for idx, line in enumerate(lines):
        if idx == 0:
            schematic.append("."*len(line))
        # for x in [x for x in re.split(r"[*.#+$]",line.strip("\n")) if x]:
        #     numbers.append(int(x))
        schematic_line = line.strip("\n").split()
        schematic.append("."+schematic_line[0]+".")
        if idx == len(lines)-1:
            schematic.append("."*len(line))
    print(schematic)
    #print(numbers)
    for j, y in enumerate(schematic):
        skip = 0
        for i, x in enumerate(y):
            if skip != 0:
                skip -= 1
                continue
            if x.isdigit():
                number = x
                i += 1
                while y[i].isdigit():
                    number += y[i]
                    i += 1
                # Replace the part of the schematic with erroneous numbers.
                char_list = list(schematic[j])
                char_list[i-len(number):i] = "."*len(number)
                schematic[j] = ''.join(char_list)
                skip = len(number)

                # Check surrounding elements for symbols
                above = schematic[j-1][i-len(number)-1:i+1]
                middle = schematic[j][i-len(number)-1:i+1]
                below = schematic[j+1][i-len(number)-1:i+1]
                print(above, middle, below)
                if contains_symbols(above+middle+below,"+$*#@/&-%="):
                    errors.append(int(number))                     
    # print(schematic)
    # print(errors)
    print(f"Answer: {sum(errors)}")

if __name__ == "__main__":
    main()