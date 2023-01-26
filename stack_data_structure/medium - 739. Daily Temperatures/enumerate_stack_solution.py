"""
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have
to wait after the ith day to get a warmer temperature. If there is no future day
for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
"""

def dailyTemperatures(temperatures):
    # initiate result list with 0s as default values -> no need to add them later in the function as
    result = [0] * len(temperatures)
    # helper stack list
    stack = []

    for i, t in enumerate(temperatures):
        # if a higher number is found, go through the stack and calc the difference in index between
        # the found value and the temperature in stack
        while stack and t > stack[-1][1]:
            index, temp = stack.pop()
            # update result list with the difference between two indices
            result[index] = (i - index)
        # always append current t to stack
        stack.append([i, t])
    return result


print(dailyTemperatures([30,40,50,60]))
print(dailyTemperatures([73,74,75,71,69,72,76,73]))