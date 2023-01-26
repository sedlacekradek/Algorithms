""""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""


def groupAnagrams(strs):
    result = []
    hash_map = {}

    for i in range(len(strs)):
        key_val = ''.join(sorted(strs[i]))  # sorted returns a list -> convert to string using ''.join
        # time complexity:
        # soring -> n log n (n - average length of word)
        # this has to be done for each word in list
        # so: m * n log n; where m is number of items and n is the average length of an item

        # create a hash map
        # key is the sorted string, value is a list of associated items from strs
        if key_val in hash_map:
            hash_map[key_val] = hash_map[key_val] + [strs[i]]
        else:
            hash_map[key_val] = [strs[i]]

    # convert hash map values to a list and return it
    for key in hash_map:
        result.append(hash_map[key])
    return result

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))

