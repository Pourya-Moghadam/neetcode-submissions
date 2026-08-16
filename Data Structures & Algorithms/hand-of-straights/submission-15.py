class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        heap = list(count.keys())
        heapq.heapify(heap)
        if len(hand) % groupSize != 0:
            return False
        
        while heap:
            first = heap[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                
                count[i] -= 1
                if count[i] == 0:
                    if i != heap[0]:
                        return False
                    
                    heapq.heappop(heap)
        
        return True