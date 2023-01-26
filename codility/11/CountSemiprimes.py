def is_prime(number):
    for j in range(2, int(number ** 0.5) + 1):
        if number % j == 0:
            return False
    return True

def solution(N, P, Q):
    # scores 44% :(
    # 100% correctness, 0% time complexity

    low = min(P)
    high = max(Q)
    high2 = max(Q) // 2
    primes = []
    subprimes = set()
    res = []

    for i in range(low, high2 + 1):
        if is_prime(i):
            primes.append(i)

    #print(primes)

    for i in range(1, len(primes)):
        for j in range(i, len(primes)):
            product = primes[i] * primes[j]
            if product > high:
                break
            if product >= 4 and product <= high:
                subprimes.add(product)

    #print(subprimes)

    for i in range(len(P)):
        counter = 0
        for number in subprimes:
            if number >= P[i] and number <= Q[i]:
                counter += 1
        res.append(counter)


    return res