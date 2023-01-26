def solution(A):

    # get frequency of all digits in A
    freq = {}
    for n in A:
        freq[n] = freq.get(n, 0) + 1


    # get all divisors for all digits
    divisors = {}
    for key in freq:
        divs_set = set()
        for n in range(1, int(key ** 0.5) + 1):
            if key % n == 0:
                divs_set.add(n)
                divs_set.add(key // n)
        divisors[key] = [d for d in divs_set]

    # count non-divs in A
    res = []
    non_divs = {}
    # iterate through A
    for n in A:
        # if we already have a result for given digit, update result
        if n in non_divs:
            res.append(non_divs[n])
        else:
            # max number of non-divisors is len(A)
            n_non_divs = len(A)
            # from len(A) subtract the frequency of each divisor of given digit
            for divs in divisors[n]:
                if divs in freq:
                    n_non_divs -= freq[divs]
            # update res and non_divs dict to improve time complexity
            non_divs[n] = n_non_divs
            res.append(n_non_divs)

    return res