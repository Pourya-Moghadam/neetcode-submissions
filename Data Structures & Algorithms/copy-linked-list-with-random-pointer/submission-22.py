"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}

        def dfs(node):
            if node in oldToCopy:
                return oldToCopy[node]
            
            copy = Node(node.val)
            oldToCopy[node] = copy
            copy.next = dfs(node.next)
            copy.random = dfs(node.random)

            return oldToCopy[node]
        
        dfs(head)

        return oldToCopy[head]