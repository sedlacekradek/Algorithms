def coinChange(coins, amount):
    # greedy solution does not work - see case [1,3,4,5], 7: greedy solution will find 5+1+1 -> 3 coins
    # but correct solution should be 3+4 -> 2 coins
    # to solve we use bottom up approach -> we solve the problem for all amounts from 0 to amount

    # create a list to store results for all amounts
    subres = [amount + 1 for _ in range(amount + 1)]
    # the amount for 0 will always be 0
    subres[0] = 0

    # go through all the amounts
    for i in range(1, amount + 1):
        min_coins = amount + 1
        # calc possible res for all coins
        for c in coins:
            # if coin is too big
            if i - c < 0:
                continue
            # if coin is not too big, calc AMOUNT - COIN and look up in previous results the least possible
            # number of coins needed to solve it
            else:
                min_coins = min(min_coins, subres[i - c] + 1)
        # save best found result in our list of previous results
        subres[i] = min_coins

    # last amount in our list of subres is the wanted amount
    # if it is bigger than wanted amount, it means that no solution was found and the program kept the value
    # it was initiated with (amount+1)
    # which means that we should return -1 as per instructions
    if subres[-1] > amount:
        return -1
    # if a possible solution foundm return the solution
    return subres[-1]

print(coinChange(coins=[186,419,83,408], amount=6249)) # 20