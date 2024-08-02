class Card:
    """Represents a standard playing card."""
    # class attributes
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', 
              '8', '9', '10', 'Jack', 'Queen', 'King']
    
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
    #Print Card()
    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])
    
    # __lt__ less than opperator override

    """def __lt__(self, other):
        # check the suits
        if self.suit < other.suit: return True
        if self.suit > other.suit: return False

        # suits are the same... check ranks
        return self.rank < other.rank"""
    # a more concice version, using a tuple
    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

class Deck:
    """represents a deck of playing cards
    attributes are cards"""

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
    
    #Print Deck()
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    #Remove last card from Deck:
    def pop_card(self):
        return self.cards.pop()
    
    #Add card to the Deck:
    def add_card(self, card):
        self.cards.append(card)
    
    # Shuffle Deck using random sort - Import Random Library:
    def shuffle(self):
        random.shuffle(self.cards)
    #Sorts the Deck
    def sort(self):
        self.cards.sort()
    
    #move_cards deals num cards to hand:
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())


    def deal_hands(self, hands, cards):
        hand=[]
        assert len(self.cards)>= hands*cards, 'not enough cards'
        for h in range(hands):
            hand.append(Hand())
        #The nested loop allows cards to be dealt to each hand in turn, 
            #although move_cards would return a random set of cards it is not authentic
        for i in range(cards):
            for h in range(hands):
                deal=self.pop_card()
                hand[h].add_card(deal)

        return hand


class Hand(Deck):
    """Represents a hand of playing cards.
    attributes cards and label"""

    # initialising Hand
    def __init__(self, label=''):
        self.cards = []
        self.label = label




#main
import random
#example of a card code
queen_of_diamonds = Card(1, 15)
#card1 = Card(2, 11)
#print(Card1)

pack=Deck()
#print(pack)
pack.shuffle()
#print(pack)

hands = pack.deal_hands(4,15)
h= len(hands)
print(h)
for i in range(len(hands)):
    label= i+1
    print('Hand %d' %label)
    print(hands[i])
    print()