def minCostClimbingStairs(cost):
    cost_sum = []

    for i in range(len(cost)):
        if len(cost_sum) < 2:
            cost_sum.append(cost[i])
        else:
            cost_sum.append(cost[i] + min(cost_sum[i - 1], cost_sum[i - 2]))

    print(cost_sum)
    return min(cost_sum[-2], cost_sum[-1])