
class Hand:
    def __init__(self, line):
        self.cards, self.sorted_cards = self.sort_cards(line[0])
        self.bet = int(line[1])
        self.type, self.type_val = self.determine_type()

    def sort_cards(self, string):
        sorted_cards = [0]*15
        cards = []
        card_translator = {"T":10, "J":11, "Q":12, "K":13, "A":14}
        for letter in string:
            if letter.isdigit(): 
                sorted_cards[int(letter)] += 1
                cards.append(int(letter))
            else: 
                sorted_cards[card_translator[letter]] += 1
                cards.append(card_translator[letter])
        return cards, sorted_cards
    
    # Return type and the card value of type.
    def determine_type(self):
        if 5 in self.sorted_cards:
            return 7, self.sorted_cards.index(5)
        elif 4 in self.sorted_cards:
            return 6, self.sorted_cards.index(4)
        elif 3 in self.sorted_cards:
            # Add case with full house.
            if 2 in self.sorted_cards:
                return 5, [self.sorted_cards.index(3), self.sorted_cards.index(2)]
            else: 
                return 4, self.sorted_cards.index(3)
        elif 2 in self.sorted_cards:
            indices = [i for i, value in enumerate(self.sorted_cards) if value == 2]
            # Add case with two pairs.
            if len(indices) > 1: 
                return 3, indices
            # One pair
            else: 
                return 2, self.sorted_cards.index(2)
        else:
            # High card
            return 1, None

    def compare_hands(self, hand):
        # Start with comparing type
        if self.type > hand.type: return True
        # Make cases for comparing types if they are the same.
        if self.type == hand.type:
            for i, _ in enumerate(self.cards):
                if self.cards[i] != hand.cards[i]:
                    return self.cards[i] > hand.cards[i]
        else:
            return False
        
        
    

def main():
    with open("inputs/7.txt", "r") as file:
        lines = file.readlines()
    hands = []
    for line in lines:
        game = line.strip("\n").split()
        hands.append(Hand(game))
    ranking = []
    for hand in hands:
        if not ranking:
            ranking = [hand]
        else:
            for idx, rank in enumerate(ranking):
                # Place before if rank hand is lesser that rank.
                if not hand.compare_hands(rank):
                    ranking.insert(idx, hand)
                    break
                if idx == len(ranking)-1:
                    ranking.append(hand)
                    break
    print([rank.type for rank in ranking])
    total_winnings = 0
    for i, hand in enumerate(ranking):
        total_winnings += hand.bet*(i+1)
    print(total_winnings)


if __name__ == "__main__":
    main()
