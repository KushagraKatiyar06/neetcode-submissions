# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.largest = 0

        def getHeight(root):
            if root is None:
                return 0

            right = getHeight(root.right)
            left = getHeight(root.left)
            diameter = right + left
            self.largest = max(diameter, self.largest)
            return max(right, left) + 1

        getHeight(root)
        return self.largest