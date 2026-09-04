# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode()
        head = dummy

        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))
        
        while heap:
            val, index, node = heapq.heappop(heap)
            head.next = node
            head = head.next

            if node.next:
                heapq.heappush(heap, (node.next.val, index, node.next))

        return dummy.next