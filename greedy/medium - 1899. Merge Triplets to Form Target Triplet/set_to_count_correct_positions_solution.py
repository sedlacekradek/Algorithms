"""
A triplet is an array of three integers. You are given a 2D integer array triplets,
where triplets[i] = [ai, bi, ci] describes the ith triplet. You are also given an integer
array target = [x, y, z] that describes the triplet you want to obtain.
To obtain target, you may apply the following operation on triplets any number of times (possibly zero):
Choose two indices (0-indexed) i and j (i != j) and update triplets[j] to become [max(ai, aj),
max(bi, bj), max(ci, cj)].
For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5], triplets[j] will be updated to [max(2, 1),
max(5, 7), max(3, 5)] = [2, 7, 5].
Return true if it is possible to obtain the target triplet [x, y, z] as an element of triplets, or false otherwise.

Example 1:
Input: triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
Output: true
Explanation: Perform the following operations:
- Choose the first and last triplets [[2,5,3],[1,8,4],[1,7,5]]. Update the last triplet to be
[max(2,1), max(5,7), max(3,5)] = [2,7,5]. triplets = [[2,5,3],[1,8,4],[2,7,5]]
The target triplet [2,7,5] is now an element of triplets.

Example 2:
Input: triplets = [[3,4,5],[4,5,6]], target = [3,2,5]
Output: false
Explanation: It is impossible to have [3,2,5] as an element because there is no 2 in any of the triplets.

Example 3:
Input: triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]
Output: true
Explanation: Perform the following operations:
- Choose the first and third triplets [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]. Update the third triplet to be
[max(2,1), max(5,2), max(3,5)] = [2,5,5]. triplets = [[2,5,3],[2,3,4],[2,5,5],[5,2,3]].
- Choose the third and fourth triplets [[2,5,3],[2,3,4],[2,5,5],[5,2,3]]. Update the fourth triplet to be
 [max(2,5), max(5,2), max(5,3)] = [5,5,5]. triplets = [[2,5,3],[2,3,4],[2,5,5],[5,5,5]].
The target triplet [5,5,5] is now an element of triplets.
"""


def mergeTriplets(triplets, target):
    # Input: triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]], target = [2, 7, 5]
    # Output: true
    matching_values = set()

    # if any value in a triplet is > than corresponding value in target, we cannot use this triplet to form our
    # solution -> skip
    for triplet in triplets:
        if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
            continue
        # if in the rest of the triplets, we can find a solution for each index of the target
        # we can return True
        # we use set() to avoid duplicates, if the length of set is 3, we know we have a solution for all 3 positions
        for i, v in enumerate(triplet):
            if v == target[i]:
                matching_values.add(i)
    return len(matching_values) == 3



print(mergeTriplets(triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]], target = [2, 7, 5]))
print(mergeTriplets(triplets = [[3,4,5],[4,5,6]], target = [3,2,5]))
print(mergeTriplets(triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]))
print(mergeTriplets(triplets = [[1,3,1]], target = [1,3,1]))
print(mergeTriplets(triplets = [[5,7,6],[7,5,9],[3,4,7],[7,3,10],[10,5,7],[9,1,5],[5,4,7],[10,10,6],[8,8,8],[4,9,8],[3,2,5],[9,10,6],[2,4,5],[4,4,3],[1,1,4],[8,10,2],[8,7,10],[4,7,8],[7,4,3],[1,2,7]], target = [3,9,8]))

