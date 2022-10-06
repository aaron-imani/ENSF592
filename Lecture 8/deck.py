import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        delimiter = '\n'
        return delimiter.join(res)
    
    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())
    
if __name__ == 'main':
    deck = Deck()
    print(deck)
    # Ace of Clubs
    # 2 of Clubs
    # 3 of Clubs
    # ...
    # 10 of Spades
    # Jack of Spades
    # Queen of Spades
    # King of Spades