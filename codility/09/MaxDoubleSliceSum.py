def solution(A):
    # Initialize variables to store the maximum sum and the prefix and suffix sums
    max_sum = 0
    prefix_sums = [0] * len(A)
    suffix_sums = [0] * len(A)

    # Calculate the prefix sums
    for i in range(1, len(A)):
        prefix_sums[i] = max(0, prefix_sums[i-1] + A[i])

    # Calculate the suffix sums
    for i in range(len(A)-2, -1, -1):
        suffix_sums[i] = max(0, suffix_sums[i+1] + A[i])

    # Find the maximum sum by iterating over all possible values of Y
    for y in range(1, len(A)-1):
        max_sum = max(max_sum, prefix_sums[y-1] + suffix_sums[y+1])

    return max_sum