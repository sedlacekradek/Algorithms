"""
Alice has some number of cards and she wants to rearrange the cards into groups so that each group
is of size groupSize, and consists of groupSize consecutive cards.
Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize,
return true if she can rearrange the cards, or false otherwise.

Example 1:
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

Example 2:
Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.
"""


def isNStraightHand(hand, groupSize):
    # Input: hand = [1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize = 3
    # Output: true
    hand.sort()
    n = len(hand)
    hash_map = {}

    # create hash_map with all numbers in hand and their count
    for number in hand:
        hash_map[number] = hash_map.get(number, 0) + 1

    # iterate through the hashmap
    for i in range(n):
        # if counter is not 0, reduce the count by 1
        # we know that any number with counter > 0 must be the first number of the group
        # because immediately after we find it we reduce all the following numbers in the group by 1
        # see the steps below
        if hash_map[hand[i]] != 0:
            hash_map[hand[i]] -= 1
            # go through all numbers that should follow in the group after this number
            for j in range(hand[i] + 1, hand[i] + groupSize):
                # if the number is not found or the count is 0 - return false
                if j not in hash_map or hash_map[j] == 0:
                    return False
                # if found reduce count by 1
                hash_map[j] -= 1
    return True



print(isNStraightHand(hand = [1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize = 3))
print(isNStraightHand(hand = [1,2,3,4,5], groupSize = 4))
print(isNStraightHand(hand = [1], groupSize = 1))
print(isNStraightHand(hand = [8,10,12], groupSize = 3))
print(isNStraightHand(hand = [2,1], groupSize = 2))
print(isNStraightHand(hand = [9,13,15,23,22,25,4,4,29,15,8,23,12,19,24,17,18,11,22,24,17,17,10,23,21,18,14,18,7,6,3,6,19,11,16,11,12,13,8,26,17,20,13,19,22,21,27,9,20,15,20,27,8,13,25,23,22,15,9,14,20,10,6,5,14,12,7,16,21,18,21,24,23,10,21,16,18,16,18,5,20,19,20,10,14,26,2,9,19,12,28,17,5,7,25,22,16,17,21,11], groupSize = 10))
# 1 2 2 3 3 4 6 7 8
# group 1 2 3 /