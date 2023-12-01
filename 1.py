def main1():
    with open("inputs/1.txt", "r") as file:
        lines = file.readlines()

    numbers = []
    for line in lines:
        #print(line)
        digits = []
        for item in line:
            if item.isdigit():
                #print(item)
                digits.append(item)
            
        numbers.append(int(digits[0]+digits[-1]))
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

def main2():
    with open("inputs/1.txt", "r") as file:
        lines = file.readlines()

    numbers = []
    for line in lines:
        line = text_to_digit(line)
        #print(line)
        digits = []
        for item in line:
            if item.isdigit():
                #print(item)
                digits.append(item)
            
        numbers.append(int(digits[0]+digits[-1]))
    print(sum(numbers))


if __name__ == "__main__":
    main1()
    main2()