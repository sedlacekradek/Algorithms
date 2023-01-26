def solution(nums):
    hash_table = set()
    for n in nums:
        if n in hash_table:
            return True
        else:
            hash_table.add(n)
    return False