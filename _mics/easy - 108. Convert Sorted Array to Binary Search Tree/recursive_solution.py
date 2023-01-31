# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None

        def recurs(low, high, nums=nums):

            if low > high:
                return None
            mid = (low + high) // 2
            node = TreeNode(val=nums[mid])
            node.left = recurs(low=low, high=mid - 1)
            node.right = recurs(low=mid + 1, high=high)
            return node

        return recurs(low=0, high=len(nums) - 1)