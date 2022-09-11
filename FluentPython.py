# import collections

# Card = collections.namedtuple('Card', ['rank', 'suit'])

# class FrenchDeck:
#     ranks = [str(n) for n in range(2,11)] + list('JQKA')
#     suits = 'spades diamonds clubs hearts'.split()
    
    
#     def __init__(self):
#         self._cards= [Card(rank, suit) for suit in self.suits
#                      for rank in self.ranks]
        
#     def __len__(self):
#         return len(self._cards)
    
#     def __getitem__(self, position):
#         return self._cards[position]
    
# beer_card = Card('7', 'diamonds')
# print(beer_card)

# deck = FrenchDeck()
# print(len(deck))

# #  We use Random for random values 
# from random import choice
# print(choice(deck))

# print(deck[:3])
# print(deck[12::13])

# for card in deck:
#     print(card) 
    
# for card in reversed(deck):
#     print(card)
   
   
# # if a collection has no __contains__ method, the in operator  does a sequential scan...
 
# print(Card('Q', 'hearts') in deck)
# print(Card('7', 'beasts') in deck)


# #  we use sorting here

# suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

# def spades_high(card):
#     rank_value = FrenchDeck.ranks.index(card.rank)
#     return rank_value * len(suit_values) + suit_values[card.suit]


# for card in sorted(deck, key=spades_high):
#     print(card)

from math import hypot

class Vector:
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y =y
        
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y) # using %r to obtain standard representation of the attributes to be displayed.
    
    def __abs__(self):
        return hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self)) # here i convert the magnitude to a Boolean by using abs(self)..
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    

    

    