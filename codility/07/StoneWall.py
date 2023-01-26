def solution(H):
    blocks = set()
    blocks.add(H[0])
    res = 1
    block_min = H[0]
    previous = H[0]

    for n in H[1:]:
        if n > previous:
            res += 1
        elif n in blocks:
            pass
        elif n not in blocks:
            res += 1

        previous = n

        if n > block_min:
            blocks.add(n)
        if n <= block_min:
            block_min = n
            blocks = set()
            blocks.add(n)

    return res

print(solution([5,3,4,6,5,4,3,2,5,3,5,3,1]))