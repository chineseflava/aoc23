import re

class Card:
    def __init__(self, line):
        split_line = line.strip("\n").split()
        break_index = split_line.index("|")
        self.name = int(split_line[1][:-1])
        self.winning_numbers = split_line[2:break_index]
        self.numbers = split_line[break_index+1:]
        self.score, self.wins = self.get_score()
        self.count = 1
    
    def increment(self, value):
        self.count += value

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
        return score, score_count
    
        
def main():
    with open("inputs/4.txt", "r") as file:
        lines = file.readlines()
    scores = []
    cards = []
    for line in lines:
        card = Card(line)
        if card.score:
            scores.append(card.score)
        cards.append(card)
    print(f"Answer 1: {sum(scores)}")

    # Part 2
    for card in cards:
        if card.score:
            for i in range(0,card.wins):
                pos = card.name+i
                if pos < len(cards):
                    cards[pos].increment(card.count)
    card_count = 0
    for card in cards:
        card_count += card.count
    print(f"Answer 2: {card_count}")


if __name__ == "__main__":
    main()