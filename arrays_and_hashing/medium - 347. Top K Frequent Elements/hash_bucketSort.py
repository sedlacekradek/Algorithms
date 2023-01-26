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


def topKFrequent(nums, k):

    hash_map = {}  # to count number of times an element is present
    # list that will be used to retrieve k most frequest elements -> bucket sort used, avoid sorting dict, which would
    # be O(n log n)
    # index in list will indicate the frequency and value will be the numbers with this frequency (could be multiple)
    freq_list = [[] for _ in range(0, len(nums)+1)]
    result = []

    # count the number if instances of int in k
    for item in nums:
        hash_map[item] = hash_map.get(item, 0) + 1

    # populate the freq_list
    for key, value in hash_map.items():
        freq_list[value].append(key)

    # iterate through freq_list in reversed order -> most frequent element have the highest index -> we do not have to
    # iterate through the whole list and can stop when K number of elements reached
    for n in freq_list[::-1]:
        for val in n:
            result.append(val)
            if len(result) == k:
                return result


print(topKFrequent(nums=[2, 2, 3,3,3, 1, 1, 1, 1], k=2))
print(topKFrequent(nums = [1], k = 1))
print(topKFrequent(nums = [-1,-1], k = 1))

