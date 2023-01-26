def solution(S, P, Q):

    # create a list for each possible letter in "S", this list will keep track of how many times
    # this letter occurred  in "S" so far (when iterating from left to right)
    a_list = [0] * len(S)
    a = 0
    c_list = [0] * len(S)
    c = 0
    g_list = [0] * len(S)
    g = 0
    t_list = [0] * len(S)
    t = 0

    res = []

    # populate the lists with correct values
    for i in range(0, len(S)):

        if S[i] == "A":
            a += 1
        if S[i] == "C":
            c += 1
        if S[i] == "G":
            g += 1
        if S[i] == "T":
            t += 1

        a_list[i] = a
        c_list[i] = c
        g_list[i] = g
        t_list[i] = t

    for i in range(0, len(P)):
        i1 = P[i]
        i2 = Q[i]

        # order is important here
        # compare the number of occurrences at index given by P with the number at index from [Q]
        # if the number increased, it means that this sublist contains the element
        # also check the left index (P) for the element
        if a_list[i1] < a_list[i2] or S[i1] == "A":
            res.append(1)
        elif c_list[i1] < c_list[i2] or S[i1] == "C":
            res.append(2)
        elif g_list[i1] < g_list[i2] or S[i1] == "G":
            res.append(3)
        elif t_list[i1] < t_list[i2] or S[i1] == "T":
            res.append(4)

    return res


S = 'CAGCCTA'
P = [2, 5, 0]
Q = [4, 5, 6]
print(solution(S, P, Q))  # Output: [2, 4, 1]
