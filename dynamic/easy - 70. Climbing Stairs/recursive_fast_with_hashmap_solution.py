"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

def climbStairs(n):
    """
    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
    """
    memo = {}
    memo[1] = 1
    memo[2] = 2

    def climb(n):
        if n in memo:  # if the recursion already done before first take a look-up in the look-up table
            return memo[n]
        else:  # Store the recursion function in the look-up table and return the stored look-up table function
            memo[n] = climb(n - 1) + climb(n - 2)
            return memo[n]

    return climb(n)

# print(climbStairs(3))
print(climbStairs(2))



