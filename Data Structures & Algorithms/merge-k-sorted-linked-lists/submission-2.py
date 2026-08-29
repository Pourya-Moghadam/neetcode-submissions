# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        heap = []

        for i, node in enumerate(lists):
            if node:
                heap.append((node.val, i, node))
        
        heapq.heapify(heap)

        while heap:
            val, i, node = heapq.heappop(heap)
            head.next = node
            head = head.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        
        return dummy.next