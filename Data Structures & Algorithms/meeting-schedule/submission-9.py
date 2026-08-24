"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i:i.start)
        curEnd = float("-inf")
        for i in intervals:
            if i.start < curEnd:
                return False
            
            curEnd = i.end
        
        return True