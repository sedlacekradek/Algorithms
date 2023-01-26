"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas
and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead
and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23
"""

def minEatingSpeed(piles, h):

    # time complexity O(log(max(piles) * len(piles))
    # len(piles) because we iterate through the array when calculating the time

    import math

    min_speed = 1
    max_speed = max(piles)

    def calc_time(speed, piles):
        res = 0
        for pile in piles:
            res += math.ceil(pile / speed)
        return res

    while min_speed <= max_speed:
        speed = (min_speed + max_speed) // 2
        time_needed = calc_time(speed=speed, piles=piles)
        if time_needed == h:
            return speed
        if time_needed > h:
            min_speed = speed + 1
        if time_needed < h:
            max_speed = speed - 1
    return speed

print(minEatingSpeed(piles = [3, 6, 7, 11], h = 8))
print(minEatingSpeed(piles = [30,11,23,4,20], h = 5))
print(minEatingSpeed(piles = [30,11,23,4,20], h = 6))
print(minEatingSpeed(piles = [30], h = 6))


