# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.result = True

        def getHeight(root):
            if root is None:
                return 0
            
            right = getHeight(root.right)
            left = getHeight(root.left)

            if abs(right - left) > 1:
                self.result = False
                        
            return max(right, left) + 1

        getHeight(root)
        return self.result

        
        