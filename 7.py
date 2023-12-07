
class Hand:
    def __init__(self, line):
        self.cards = self.sort_cards(line[0])
        self.bet = int(line[1])
        self.type = self.determine_type(self.cards)

   

    def sort_cards(self, string):
        cards = {}
        card_translator = {"T":10, "J":11, "Q":12, "K":13, "A":14}
        for letter in string:
            if letter.isdigit():
                cards[letter] += 1
            else:
                cards[card_translator[letter]] += 1

        return
    
    def determine_type(self):
        return

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
