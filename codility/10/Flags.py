from math import ceil

def solution(A):
    n = len(A)
    peaks = []
    # find the peaks
    for i in range(1, n-1):
        if A[i-1] < A[i] > A[i+1]:
            peaks.append(i)
    # return 0 if there are no peaks
    if not peaks:
        return 0
    # return 1 if there are only three elements and there is a peak
    if n == 3:
        return 1
    # binary search for the maximum number of flags
    low = 0
    high = len(peaks)
    while low <= high:
        mid = (low + high) // 2
        pos = peaks[0]
        flag_count = 1
        for i in range(1, len(peaks)):
            if peaks[i] - pos >= mid:
                pos = peaks[i]
                flag_count += 1
        if flag_count >= mid:
            low = mid + 1
            result = mid
        else:
            high = mid - 1
    return result

solution([1,5,3,4,3,4,1,2,3,4,6,2])