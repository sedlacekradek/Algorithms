class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []
        for char in s:
            res.append(char)
            while len(res) > 1 and res[-1] == res [-2]:
                res.pop()
                res.pop()
        return "".join(res)