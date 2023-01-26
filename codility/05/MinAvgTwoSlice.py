def solution(A):
    # the slices are never going to be bigger than two or three because mathematically,
    # anything bigger than three can just be split evenly or into two and three collectively.

    result = 0  # starting index
    min_avg = float("inf")

    # only compute twos and threes slicing
    for i in range(0, len(A)):
        # calc for two slicing
        if i + 1 < len(A):
            temp_avg = (A[i] + (A[i + 1])) / 2
            if temp_avg < min_avg:
                min_avg = temp_avg
                result = i

        # calc for three slicing
        if i + 2 < len(A):
            temp_avg = (A[i] + (A[i + 1]) + (A[i + 2])) / 3
            if temp_avg < min_avg:
                min_avg = temp_avg
                result = i

    return result

print(solution([4, 2, 2, 5, 1, 5, 8]))