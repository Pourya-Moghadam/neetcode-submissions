# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {inorder[i]:i for i in range(len(inorder))}
        self.rootIndex = 0

        def solve(l, r):
            if l > r:
                return None
            
            rootVal = preorder[self.rootIndex]
            self.rootIndex += 1
            root = TreeNode(rootVal)
            m = indices[rootVal]
            root.left = solve(l, m - 1)
            root.right = solve(m + 1, r)
            return root
        
        return solve(0, len(inorder) - 1)