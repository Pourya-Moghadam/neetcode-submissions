# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float("-inf")

        def dfs(node):
            if node is None:
                return float('-inf')
            
            left = dfs(node.left)
            right = dfs(node.right)
            val = node.val
            self.res = max(self.res, val, val + left + right, val + left, val + right)

            return max(val, val + left, val + right)
        
        dfs(root)

        return self.res