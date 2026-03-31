"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, 0))

        events.sort()
        res = 0
        cur = 0
        for event in events:
            if event[1] == 0: # observ end
                res = max(cur, res)
                cur -= 1
            else:
                cur += 1 

        return res