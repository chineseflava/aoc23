def get_first_and_last_digits(lines, part2 = False):
    numbers = []
    for line in lines:
        if part2 == True:
           line = text_to_digit(line)
        digits = []
        for item in line:
            if item.isdigit():
                digits.append(item)
            
        numbers.append(int(digits[0]+digits[-1]))
    return numbers

def part1():
    with open("inputs/1.txt", "r") as file:
        lines = file.readlines()
    numbers = get_first_and_last_digits(lines)
    print(sum(numbers))

def text_to_digit(line):
    line = line.replace("one", "on1e")
    line = line.replace("two", "tw2o")
    line = line.replace("three", "thr3ee")
    line = line.replace("four", "fo4ur")
    line = line.replace("five", "fi5ve")
    line = line.replace("six", "si6x")
    line = line.replace("seven", "se7en")
    line = line.replace("eight", "ei8ght")
    line = line.replace("nine", "ni9ne")
    line = line.replace("zero", "ze0ro")
    return line

def part2():
    with open("inputs/1.txt", "r") as file:
        lines = file.readlines()
    numbers = get_first_and_last_digits(lines, True)
    print(sum(numbers))


if __name__ == "__main__":
    part1()
    part2()