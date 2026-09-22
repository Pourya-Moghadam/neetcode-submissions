# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(next=head)
        prevGroup = dummy
        
        while True:

            kth = prevGroup
            for i in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next
            
            nextGroup = kth.next
            cur = prevGroup.next
            prev = nextGroup

            while cur != nextGroup:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            tmp = prevGroup.next
            prevGroup.next = kth
            prevGroup = tmp
        
        return dummy.next