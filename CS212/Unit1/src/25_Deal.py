# -----------
# User Instructions
# 
# Write a function, deal(numhands, n=5, deck), that 
# deals numhands hands with n cards each.
#

import random # this will be a useful library for shuffling

# This builds a deck of 52 cards. If you are unfamiliar
# with this notation, check out Andy's supplemental video
# on list comprehensions (you can find the link in the 
# Instructor Comments box below).

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 

def deal(numhands, n=5, deck=mydeck):
    hands = []
    
    for x in range(numhands):
        hand = []
        for y in range(n):
            if len(mydeck) == 0: break
#            card = mydeck[int(random.random() * len(mydeck))]
            card = mydeck[random.randint(0, len(mydeck)-1)]
            hand.append(card)
            mydeck.remove(card)
        if len(hand) == n:
            hands.append(hand)
        else:
            deck += hand
    
    return hands

print deal(11)
print mydeck
            