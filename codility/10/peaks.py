def solution(A):
    # scores 72%

    # find peaks and their index
    peaks = []
    for i in range(1, len(A) - 1):
        if A[i] > A[i - 1] and A[i] < A[i + 1]:
            peaks.append(i)
    # print(peaks)

    # divide into as many parts as possible (max len of peaks) and check if each part contains a peak
    for n in range(len(peaks), 0, -1):
        if len(A) % n == 0:
            for j in range(0, len(peaks)):
                # if part does not contain a peak, break loop
                if peaks[j] <= (j * (len(A) / n)) or peaks[j] > (j * (len(A) / n)) + (len(A) / n):
                    break
                # if loop has not been broken, return n
                return n

    return 1

solution([1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2])