"""
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""

from operator import itemgetter

def topKFrequent(nums, k):

    hash_map = {}
    result = []

    # count the number if instances of int in k
    for item in nums:
        hash_map[item] = hash_map.get(item, 0) + 1

    # sort dict by value in reverse order
    hash_map = sorted(hash_map.items(), key=itemgetter(1), reverse=True)

    # append and return result
    for key, value in hash_map:
        result.append(key)
        if len(result) == k:
            return result


print(topKFrequent(nums=[2, 2, 3,3,3, 1, 1, 1, 1], k=2))
print(topKFrequent(nums = [1], k = 1))
print(topKFrequent(nums = [-1,-1], k = 1))

