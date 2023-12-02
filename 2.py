import re
"""
Part 1:
which games would have been possible if the bag contained 
only 12 red cubes, 13 green cubes, and 14 blue cubes?
"""
def main():
    with open("inputs/2.txt", "r") as file:
        lines = file.readlines()
    possible_games = []
    powers = []
    for line in lines:
        game = Game(line, 12,13,14)
        if game.is_possible:
            possible_games.append(game.number)
        powers.append(game.power)
        
    print(f"Part 1: {sum(possible_games)}")
    print(f"Part 2: {sum(powers)}")

class Game:
    def __init__(self, line, red_lim, green_lim, blue_lim):
        line = line.rstrip("\n")
        split_line = re.split(": |, |; ", line)
        #print(split_line)
        reds = 0
        greens = 0
        blues = 0

        max_red = 0
        max_green = 0
        max_blue = 0

        is_possible = True
        for item in split_line[1:]:
            if "red" in item:
                amount = int(item[:-4])
                if amount <= red_lim:
                    reds += amount
                else:
                    is_possible = False

                max_red = amount if amount > max_red else max_red
            if "green" in item:
                amount = int(item[:-6])
                if amount <= green_lim:
                    greens += amount
                else:
                    is_possible = False
                
                max_green = amount if amount > max_green else max_green
            if "blue" in item:
                amount = int(item[:-5])
                if amount <= blue_lim:
                    blues += amount
                else:
                    is_possible = False
                
                max_blue = amount if amount > max_blue else max_blue

        self.number = int(split_line[0][4:])    
        self.is_possible = is_possible
        self.power = max_red*max_green*max_blue

if __name__ == "__main__":
    main()