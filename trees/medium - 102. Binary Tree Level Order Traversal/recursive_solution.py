# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result

        def recursion(root, level):
            # base ase
            if not root:
                return
            # if no list created for current level; create a new list inside a list
            if len(result) <= level:
                result.append([root.val])
            # else, append to the list with level index
            else:
                result[level].append(root.val)
            # iterate recursively through the tree, increase level
            recursion(root.left, level + 1)
            recursion(root.right, level + 1)

        recursion(root, 0)
        return result
