def solution(A):
    # Implement your solution here
    current_sum = sum(A)
    helper_sum = 0

    for n in range(1, len(A) + 2):
        helper_sum += n

    result = helper_sum - current_sum
    return result
