import re

class Card:
    def __init__(self, line):
        split_line = line.strip("\n").split()
        self.name = split_line[1][:-1]
        self.winning_numbers = split_line[2:12]
        self.numbers = split_line[13:]
        self.score = self.get_score()

    def get_score(self):
        win_set = set()
        score_count = 0
        score = None
        points_card = False
        for number in self.winning_numbers:
            win_set.add(number)
        for number in self.numbers:
            if number in win_set:
                score_count += 1
                points_card = True
        if points_card:
            score = 2**(score_count-1)
        return score
        

def main():
    with open("inputs/4.txt", "r") as file:
        lines = file.readlines()
    scores = []
    for line in lines:
        card = Card(line)
        print(f"Card {card.name}")
        print(card.winning_numbers)
        print(card.numbers)
        print(f"Score {card.score}\n")
        if card.score:
            scores.append(card.score)
    print(sum(scores))
        


if __name__ == "__main__":
    main()