"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station
to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
Given two integer arrays gas and cost, return the starting gas station's index if you can travel around
the circuit once in the clockwise direction, otherwise return -1.
If there exists a solution, it is guaranteed to be unique


Example 1:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
"""


def canCompleteCircuit(gas, cost):

    # create a table of gas - cost, if sum of this table is positive, we know there must be a valid result
    sum_table = []
    for i in range(0, len(gas)):
        sum_table.append(gas[i] - cost[i])
    # if negative, return -1
    if sum(sum_table) < 0:
        return -1

    total = 0
    start = 0
    # go through all values, if total sum gets negative, we know that the starting index(start) is not correct
    for i in range(0, len(sum_table)):
        total += sum_table[i]
        if total < 0:
            total = 0
            start = i+1
    return start




print(canCompleteCircuit( gas = [1,2,3,4,5], cost = [3,4,5,1,2])) # 3
print(canCompleteCircuit( gas = [2,3,4], cost = [3,4,3])) # -1
print(canCompleteCircuit( gas = [3,3,4], cost = [3,4,4])) # -1
print(canCompleteCircuit( gas = [5,8,2,8], cost = [6,5,6,6])) # 3
print(canCompleteCircuit( gas = [4,5,2,6,5,3], cost = [3,2,7,3,2,9])) # -1
print(canCompleteCircuit( gas = [3,1,1], cost = [1,2,2])) # 0

