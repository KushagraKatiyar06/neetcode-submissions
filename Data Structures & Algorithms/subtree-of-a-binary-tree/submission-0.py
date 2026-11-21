# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def checkSubTree(root, subRoot):
            if root == None and subRoot == None:
                return True

            if root and not subRoot or subRoot and not root:
                return False

            if root.val != subRoot.val:
                return False
                
            return (checkSubTree(root.left, subRoot.left) and checkSubTree(root.right, subRoot.right))

        def findSubTree(node):
            if not node:
                return False
            
            if node.val == subRoot.val:
                if checkSubTree(node, subRoot):
                    return True
                    
            return findSubTree(node.left) or findSubTree(node.right)
                

        return findSubTree(root)

        

            
        