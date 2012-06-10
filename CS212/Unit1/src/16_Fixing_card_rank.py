# -----------
# User Instructions
# 
# Modify the card_ranks() function so that cards with
# rank of ten, jack, queen, king, or ace (T, J, Q, K, A)
# are handled correctly. Do this by mapping 'T' to 10, 
# 'J' to 11, etc...

def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
#    cards_value = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
#    ranks = [cards_value.index(r)+1 for r,s in cards]
    # Version mejorada
    ranks = ['--23456789TJQKA'.index(r) for r,s in cards]
    
    
    ranks.sort(reverse=True)
    return ranks

print card_ranks(['AC', '3D', '4S', 'KH']) #should output [14, 13, 4, 3]
print card_ranks(['AC', '2D', '3S', '4H']) #should output [14, 13, 4, 3]
    