# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def findGoodNodes(root, rollingMax):
            if not root:
                return 0

            if root.val >= rollingMax:
                rollingMax = max(rollingMax, root.val)
                return (1 + findGoodNodes(root.right, rollingMax) + findGoodNodes(root.left, rollingMax)) 
            return (findGoodNodes(root.right, rollingMax) + findGoodNodes(root.left, rollingMax)) 

        return findGoodNodes(root, root.val)
        