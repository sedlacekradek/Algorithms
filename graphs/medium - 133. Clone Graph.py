"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        old_to_new = {}

        def clone(node):
            if node in old_to_new:
                return old_to_new[node]

            new = Node(node.val)
            old_to_new[node] = new  # important - this has to be placed before the for loop below
            for n in node.neighbors:
                new.neighbors.append(clone(n))
            return new

        if not node:
            return None

        return clone(node)