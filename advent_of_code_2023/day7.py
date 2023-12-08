# Part 1 logic : Each hand and bid in a tuple. Then iterate and find the score of each hand.
# We used counter and most common, returns a list of tuples where we unpack only the counts.
# Then we find the "strongest" card per hand by assigning it the index of orders.
# We append each card with its score, strength and bid.
# Reverse this in descending order. Then we just do math. This was hard.

# Part 2: create a cartesian product of n repated K's of all available cards besides K. Get the min score replaing
# K's with the subed products. Do the rest the same.

from collections import Counter
from itertools import product
filename = "file7.txt"

with open(filename) as file:
    data = file.read().split()

order = "AKQJT98765432"
order2 = "AKQT98765432J"
hands_bids = [(data[i],int(data[i +1]))for i in range(0,len(data),2)]
p1 = []
result_for_p1 = 0
p2 = []
result_for_p2 = 0 

def getScore(hand):
    match [num for _, num in Counter(hand).most_common()]:
        case[5,*_]:
            return 1
        case[4, *_]:
            return 2
        case[3,2, *_]:
            return 3
        case[3, *_]:
            return 4
        case[2,2, *_]:
            return 5
        case[2, *_]:
            return 6
        case _:
            return 7 

for hand, bid in hands_bids:
    score_of_hand = getScore(hand)
    strong = [order.index(card) for card in hand]
    p1.append((score_of_hand, strong, int(bid)))
p1.sort(reverse=True)

for i, val in enumerate(p1):
    result_for_p1 += (i + 1) * val[-1]
print(result_for_p1)

for hand, bid in hands_bids:
    score_of_hand2 = getScore(hand)
    strong2 = [order2.index(card) for card in hand]
    for sub in product(order2[:-1], repeat=hand.count("J")):
        score_of_hand2 = min(score_of_hand2, getScore(hand.replace("J", "") + "".join(sub)))
    p2.append((score_of_hand2, strong2, int(bid)))
p2.sort(reverse=True)

for i, val in enumerate(p2):
    result_for_p2 += (i + 1) * val[-1]
print(result_for_p2)
