def is_prime(number):
    for n in range(2, number // 2 + 1):
        if number % n == 0:
            return False
    return True

def find_divisors(number):
    res = []
    for n in range(1, int(number ** 0.5) + 1):
        if number % n == 0:
            res.append(n)
            res.append(number // n)
    return res

def common_divs(high_divs, low):
    for n in high_divs:
        if low % n != 0:
            return False
    return True

def solution(a, b):
    # scores 38 %
    # revisit https://www.youtube.com/watch?v=F_th-1Rza_s&ab_channel=CodeTrading
    res =0
    for i in range(len(a)):
        high_divs = []
        high = max(a[i], b[i])
        divisors = find_divisors(high)
        for n in divisors:
            if is_prime(n):
                high_divs.append(n)
        low = (min(a[i], b[i]))
        if common_divs(high_divs, low):
            res += 1
    return res

print(solution([2, 1, 2], [1, 2, 2]))