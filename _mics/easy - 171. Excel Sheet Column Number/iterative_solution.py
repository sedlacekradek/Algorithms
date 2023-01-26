class Solution:
    def titleToNumber(self, S: str) -> int:
        from string import ascii_lowercase
        letters = ascii_lowercase
        # print(letters)
        letter_vals = {}
        for val, letter in enumerate(letters):
            letter_vals[letter] = val + 1
        # print(letter_vals)

        res = 0
        for char in S:
            res = res * 26 + letter_vals[char.lower()]
        return res
