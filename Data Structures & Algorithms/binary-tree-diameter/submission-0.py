# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        largest = [0]

        def getHeight (root):
            if root is None:
                return 0

            right_height = getHeight(root.right)
            left_height = getHeight(root.left)
            currentDiameter = right_height + left_height
        
            largest[0] = max(largest[0], currentDiameter)
            return 1 + max(right_height, left_height)
        
        getHeight(root)
        return largest[0]
        
        