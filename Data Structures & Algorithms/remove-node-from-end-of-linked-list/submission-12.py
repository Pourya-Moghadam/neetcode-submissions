# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        while n > 0:
            slow = slow.next
            n -= 1
        
        dummy = ListNode(next=head)
        first = dummy
        second = slow

        while second:
            first = first.next
            second = second.next
        
        first.next = first.next.next

        return dummy.next