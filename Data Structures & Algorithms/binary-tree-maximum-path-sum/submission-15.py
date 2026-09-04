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
                return float("-inf")
            
            left = dfs(node.left)
            right = dfs(node.right)
            self.res = max(self.res, node.val, node.val + left, node.val + right, node.val + right + left)

            return max(node.val, node.val + right, node.val + left)
        
        dfs(root)

        return self.res