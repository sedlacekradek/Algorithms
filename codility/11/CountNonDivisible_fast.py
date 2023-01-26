def solution(a):
    count_dic = {}
    factors_dic = {}
    non_div_dic = {}
    res = []

    # make a dic of count of each element in the array
    for number in a:
        count_dic[number] = count_dic.get(number, 0) + 1

    # make a dic of all factors of each of the numbers
    for number in a:
        if number not in factors_dic:
            factors = set()
            for n in range(1, int(number ** 0.5) + 1):
                if number % n == 0:
                    factors.add(n)
                    factors.add(int(number / n))
            factors_dic[number] = factors


    # goal is to count number of non-divisors in array for each number
    # maximum possible number is len(a)
    # look at all the possible factors for each number in factors_dic
    # and from len(a) subtract the count of each of these factors in the array
    # append the result
    for number in a:
        # check if we have already encountered this number before
        if number not in non_div_dic:
            non_div_count = len(a)
            for factor in factors_dic[number]:
                non_div_count -= count_dic.get(factor, 0)
            non_div_dic[number] = non_div_count
            res.append(non_div_count)
        else:
            res.append(non_div_dic[number])


    return res

print(solution([3, 1, 2, 3, 6]))