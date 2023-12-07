
class Hand:
    def __init__(self, line):
        self.cards = self.sort_cards(line[0])
        self.bet = int(line[1])
        self.type = self.determine_type(self.cards)

    def sort_cards(self, string):
        cards = [0]*14
        card_translator = {"T":10, "J":11, "Q":12, "K":13, "A":14}
        for letter in string:
            if letter.isdigit(): cards[int(letter)] += 1
            else: cards[card_translator[letter]] += 1
        return cards
    
    # Return type and the card value of type.
    def determine_type(self):
        if 5 in self.cards:
            return 7, self.cards.key()
        if 4 in self.cards.values():
            return 6
        elif 3 in self.cards.values():
            # Add case with full house.
            return 5
            return 4
        elif 2 in self.cards.value():
            # Add case with two pairs.
            return 3
            # One pair
            return 2
        else:
            # High card
            return 1

    def compare_hands(self, hand):
        # Start with comparing type
        # Make cases for comparing types if they are the same.
        return -1
    

def main():
    with open("inputs/7_test.txt", "r") as file:
        lines = file.readlines()
    hands = []
    for line in lines:
        game = line.strip("\n").split()
        hands.append(Hand(game))
    ranking = []
    for hand in hands:
        for idx, rank in enumerate(ranking):
            if hand.compare_hands(rank) == -1:
                ranking.inser(idx, hand)
                break


if __name__ == "__main__":
    main()
