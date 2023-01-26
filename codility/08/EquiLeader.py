def solution(A):
    hash_map = {}
    max_freq = 0
    leader = None
    res = 0

    # count the number of each element in A
    for n in A:
        hash_map[n] = hash_map.get(n, 0) + 1

    # find the most frequent element and how many times it occurs
    for key, val in hash_map.items():
        if val > max_freq:
            max_freq = val
            leader = key

    # create a list with 1 for most frequent element and 0 for any other element
    # [4, 3, 4, 4, 4, 2] -> [1, 0, 1, 1, 1, 0]
    for i in range(len(A)):
        if A[i] == leader:
            A[i] = 1
        else:
            A[i] = 0

    # iterate through the list and count the number of EquiLeaders
    counter = 0
    for i in range(len(A)):
        if A[i] == 1:
            counter += 1
        # Equileader if element most frequent in the part of array we have already iterated through
        # AND most frequent in the rest of the array we have not seen yet
        if counter > ((i + 1) // 2) and (max_freq - counter) > ((len(A) - i - 1) // 2):
           res += 1

    return res

print(solution([4,3,4,4,4,2])) # 2
print(solution([4,0,4,4])) # 2
print(solution([1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0])) # 10
print(solution([1, 2, 3, 4, 5])) # 0
print(solution([1, 2, 2, 3, 1, 1])) # 0
print(solution([1])) # 0
print(solution([4, 4, 4, 4, 4])) #4
