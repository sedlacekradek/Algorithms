def solution(n, m):
    # scores 87%

    chocolates = n
    movement = m

    # find the smallest common multiple
    while chocolates % movement != 0:
        chocolates += n
    # divide it by the movement
    return chocolates // movement

print(solution(5,6)) # 5
print(solution(2,1)) # 2
print(solution(1,2)) # 1