# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevGroup = dummy

        while True:
            kth = prevGroup
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            
            nextGroup = kth.next
            prev, cur = nextGroup, prevGroup.next
            while cur != nextGroup:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            old_start = prevGroup.next
            prevGroup.next = kth
            prevGroup = old_start