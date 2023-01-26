class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        prev = None
        for val in freq.values():
            if val != prev and prev is not None:
                return False
            else:
                prev = val

        return True