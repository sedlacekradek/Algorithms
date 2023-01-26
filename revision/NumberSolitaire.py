def solution(A):
    from collections import deque
    q = deque([A[0]])

    for n in A[1:]:
        q.append(max(q) + n)
        if len(q) > 6:
            q.popleft()
    return q[-1]