def solution(A):

    if len(A) == 0:
        return 0

    lowest_price = A[0]
    max_profit = 0

    for price in A[1:]:
        profit = price - lowest_price
        max_profit = max(max_profit, profit)
        lowest_price = min(lowest_price, price)

    return max_profit



print(solution([9,3,6,7,4,8]))
print(solution([8,4,7,6,3,9]))
print(solution([23171,21011,21123,21366,21013,21367]))
print(solution([8,3]))
print(solution([1, 2, 3, 4, 5, 6]))
print(solution([6,5,4,3,2,1,0]))
print(solution([]))
print(solution([9,2,8,1,3,2,1,0]))
print(solution([7,1,5,3,6,4]))
print(solution([7,6,4,3,1]))
print(solution([8, 9, 3, 6, 1, 2]))

