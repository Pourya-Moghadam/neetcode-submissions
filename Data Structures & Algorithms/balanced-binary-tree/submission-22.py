# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True

        def dfs(node):

            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) >= 2:
                self.res = False
            
            return 1 + max(left, right)
        
        dfs(root)

        return self.res