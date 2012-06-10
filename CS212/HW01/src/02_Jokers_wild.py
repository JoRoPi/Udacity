# CS 212, hw1-2: Jokers Wild
#
# -----------------
# User Instructions
#
# Write a function best_wild_hand(hand) that takes as
# input a 7-card hand and returns the best 5 card hand.
# In this problem, it is possible for a hand to include
# jokers. Jokers will be treated as 'wild cards' which
# can take any rank or suit of the same color. The 
# black joker, '?B', can be used as any spade or club
# and the red joker, '?R', can be used as any heart 
# or diamond.
#
# The itertools library may be helpful. Feel free to 
# define multiple functions if it helps you solve the
# problem. 
#
# -----------------
# Grading Notes
# 
# Muliple correct answers will be accepted in cases 
# where the best hand is ambiguous (for example, if 
# you have 4 kings and 3 queens, there are three best
# hands: 4 kings along with any of the three queens).

import itertools
import time

def best_wild_hand(hand):
    "Try all values for jokers in all 5-card selections."
    result = None
    range_cards_value = '23456789TJQKA'
    wilds = {'?B' : ['S', 'C'], '?R' : ['H', 'D']}
    
    def check_against_result(result, hand):
        if not result: return hand
        else : return max([result, hand], key=hand_rank)
        
    def expand_wild_and_check_result(result, hand):
        if all((card != wild) for card in hand for wild in wilds):
            return check_against_result(result, hand)
        else:
            for wild in wilds:
                if wild in hand:
                    hand = hand[:hand.index(wild)] + hand[hand.index(wild)+1:] # remove wild
                    for card in [value + suit for value in range_cards_value for suit in wilds[wild]]:
                        if not card in hand: 
                            result = expand_wild_and_check_result(result, hand + (card,))
            return result
   
    for h in itertools.combinations(hand, 5):
        result = expand_wild_and_check_result(result, h)
    
    return result

def test_best_wild_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_wild_hand passes'

# ------------------
# Provided Functions
# 
# You may want to use some of the functions which
# you have already defined in the unit to write 
# your best_hand function.

def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand) 
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)
    
def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def straight(ranks):
    """Return True if the ordered 
    ranks form a 5-card straight."""
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def kind(n, ranks):
    """Return the first rank that this hand has 
    exactly n-of-a-kind of. Return None if there 
    is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def two_pair(ranks):
    """If there are two pair here, return the two 
    ranks of the two pairs, else None."""
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None 

def test_best_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C JS".split()))
            == ['6C', '7C', '8C', '9C', 'TC'])
    assert (sorted(best_wild_hand("TD TC TH 7C 7D 8C 8S".split()))
            == ['8C', '8S', 'TC', 'TD', 'TH'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_hand passes'

print test_best_wild_hand()

def test_best_wild_hand2():
    start = time.clock()
    print (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split())), ['7C', '8C', '9C', 'JC', 'TC'])
    print(time.clock() - start)

    start = time.clock()
    print (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split())), ['7C', 'TC', 'TD', 'TH', 'TS'])
    print(time.clock() - start)
    
    start = time.clock()
    print (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split())), ['7C', '7D', '7H', '7S', 'JD'])
    print(time.clock() - start)
    
    start = time.clock()
    print (sorted(best_wild_hand("JD TD TH 7C 7D ?B ?B".split())), ['JD', 'TC', 'TD', 'TH', 'TS'])
    print(time.clock() - start)
    
    start = time.clock()
    print (sorted(best_wild_hand("JD TD TH 7C ?R ?R ?R".split())), ['AD', 'JD', 'KD', 'QD', 'TD'])
    print(time.clock() - start)
    
    start = time.clock()
    print (sorted(best_wild_hand("JD TD TH 2C ?B ?R ?R".split())), ['2C', '2D', '2H', '2S', 'JD'])
    print(time.clock() - start)

    start = time.clock()
    print best_wild_hand("6H 7C ?R ?R ?R ?R ?R".split())
    print(time.clock() - start)
    
#    start = time.clock()
#    print (sorted(best_wild_hand("JD TD TH ?B ?B ?R ?R".split())), ['AC', 'AD', 'AH', 'AS', 'JD'])
#    print(time.clock() - start)
    
    return 'test_best_wild_hand passes'

print test_best_wild_hand2()

