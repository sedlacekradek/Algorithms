def solution(A, B):
    # VARIABLES
    moving_left = -1  # max val of live fish moving left
    moving_right = -1  # max val of live fish moving right
    res = 0

    # COUNT LIVE FISH MOVING LEFT
    for i in range(0, len(A)):
        if B[i] == 0:
            if A[i] > moving_right:
                res += 1
                moving_right = -1
        if B[i] == 1:
            moving_right = max(moving_right, A[i])

    # COUNT LIVE FISH MOVING RIGHT
    for i in range(len(A) - 1, -1, -1):
        if B[i] == 1:
            if A[i] > moving_left:
                res += 1
                moving_left = -1
        if B[i] == 0:
            moving_left = max(moving_left, A[i])

    return res
