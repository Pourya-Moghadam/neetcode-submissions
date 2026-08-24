# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        if p and q and ((p.val <= root.val <= q.val) or (q.val <= root.val <= p.val)):
            return root
        
        if p and q and ((p.val <= q.val < root.val) or (q.val <= q.val < root.val)):
            return self.lowestCommonAncestor(root.left, p, q)
        
        if p and q and ((p.val >= q.val > root.val) or (q.val >= p.val > root.val)):
            return self.lowestCommonAncestor(root.right, p, q)
        
        return False