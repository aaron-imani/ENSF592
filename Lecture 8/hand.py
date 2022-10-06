from deck import Deck

class Hand(Deck):
    """Represents a hand of playing cards."""
    def __init__(self, label=''):
        self.cards = []
        self.label = label


hand = Hand('new hand')
print(hand.cards)
# []
print(hand.label)
# 'new hand'

deck = Deck()
card = deck.pop_card()
hand.add_card(card)
print(hand)
# King of Spades