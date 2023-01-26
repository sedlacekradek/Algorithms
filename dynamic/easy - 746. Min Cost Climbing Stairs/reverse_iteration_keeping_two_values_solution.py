""""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
"""

def minCostClimbingStairs(cost):
    length = len(cost)
    one = cost[length - 2]
    two = cost[length - 1]

    # iterate in reverse order, start at length -3 because we already calculated steps one and two
    # IMPORTANT, the second value in range is always not included (even when reversed) therefore if we want
    # to include i = 0, we need to set the value to -1
    for i in range(length-3, -1, -1):
        temp = two
        two = one
        one = cost[i] + min(temp, one)

    # because we can decide to start from index 1 instead of index 0 as per instructions
    # we can return the smaller of these two values
    res = min(one, two)

    return res

print(minCostClimbingStairs(cost = [10,15,20]))
print(minCostClimbingStairs(cost = [10,10]))
print(minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1]))