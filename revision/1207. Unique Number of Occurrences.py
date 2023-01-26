class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}

        for n in arr:
            freq[n] = freq.get(n, 0) + 1

        duplicates = set()

        for val in freq.values():
            if val not in duplicates:
                duplicates.add(val)
            else:
                return False

        return True